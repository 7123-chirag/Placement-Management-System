from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
from utils.placement_db import (
    save_prediction,
    get_latest_prediction,
    get_prediction_data,
    prediction_exists
)
from utils.resume_db import (
    save_resume_analysis,
    get_latest_resume
)
from utils.login_required import login_required

import os
import joblib
import numpy as np
from flask import jsonify
from utils.auth import register_user, login_user

from utils.ats import ats_score
from utils.company_recommender import recommend_companies
from utils.interview_engine import (
    get_questions,
    get_companies_by_branch,
    get_roles_by_branch
)
app = Flask(__name__)
app.secret_key = "placementguide_secret_key_2026"
# ================= Upload Folder ================= #

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= Load ML Model ================= #

placement_model = joblib.load("models/placement_model.pkl")

# ================= Global Storage ================= #


# ==================================================
# Home
# ==================================================

@app.route("/")
def home():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")

# ==================================================
# Authentication
# ==================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = login_user(email, password)

        if user:

            session["user_id"] = user.UserID
            session["full_name"] = user.FullName
            session["email"] = user.Email
            session["branch"] = user.Branch

            return redirect(url_for("dashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form["full_name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        branch = request.form["branch"]
        college = request.form["college"]

        # Password Match Check
        if password != confirm_password:
            return "Passwords do not match."

        success = register_user(
            full_name,
            email,
            password,
            branch,
            college
        )

        if success:
            return redirect(url_for("login"))
        else:
            return "Email already exists."

    return render_template("register.html")


# ==================================================
# Dashboard
# ==================================================

@app.route("/dashboard")
@login_required
def dashboard():

    # -------- Resume Data --------
    resume = get_latest_resume(session["user_id"])

    if resume:
        ats_score = resume.ATSScore
        resume_uploaded = "Yes"
        found = resume.FoundSkills.split(",") if resume.FoundSkills else []
        missing = resume.MissingSkills.split(",") if resume.MissingSkills else []
        filename = resume.ResumeFile
    else:
        ats_score = 0
        resume_uploaded = "No"
        found = []
        missing = []
        filename = ""

    # -------- Placement Prediction --------
    prediction = get_latest_prediction(session["user_id"])

    if prediction:
        placement = prediction.PlacementChance
    else:
        placement = 0

    return render_template(

        "dashboard.html",

        user_name=session["full_name"],

        score=ats_score,

        placement=placement,

        companies=0,

        resume_uploaded=resume_uploaded,

        found=found,

        missing=missing,

        filename=filename

    )


# ==================================================
# Resume Upload
# ==================================================

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        branch = request.form["branch"]

        file = request.files.get("resume")

        if file and file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            # ATS Analysis
            score, found, missing, category_scores = ats_score(filepath, branch)

            # Save ATS Analysis to SQL Server
            save_resume_analysis(
                session["user_id"],
                file.filename,
                score,
                found,
                missing
            )

            return redirect(url_for("ats"))

    return render_template("upload.html")
# ==================================================
# ATS
# ==================================================

@app.route("/ats")
@login_required
def ats():

    resume = get_latest_resume(session["user_id"])

    if resume is None:
        return redirect(url_for("upload"))

    return render_template(
        "ats.html",
        score=resume.ATSScore,
        found=resume.FoundSkills.split(",") if resume.FoundSkills else [],
        missing=resume.MissingSkills.split(",") if resume.MissingSkills else [],
        filename=resume.ResumeFile,
        category_scores={},
        branch=session.get("branch","")
    )


# ==================================================
# Placement Predictor
# ==================================================

@app.route("/predictor", methods=["GET", "POST"])
@login_required
def predictor():


    if request.method == "POST":

        cgpa = float(request.form["cgpa"])
        ats = float(request.form["ats"])
        skills = int(request.form["skills"])
        projects = int(request.form["projects"])
        internships = int(request.form["internships"])
        certifications = int(request.form["certifications"])
        coding = float(request.form["coding"])
        communication = float(request.form["communication"])
        dsa = int(request.form["dsa"])
        backlogs = int(request.form["backlogs"])

        features = np.array([[
            cgpa,
            ats,
            skills,
            projects,
            internships,
            certifications,
            coding,
            communication,
            dsa,
            backlogs
        ]])

        probability = placement_model.predict_proba(features)[0][1]

        prediction = round(probability * 100, 2)

        save_prediction(
            session["user_id"],
            cgpa,
            skills,
            projects,
            internships,
            certifications,
            coding,
            communication,
            dsa,
            backlogs,
            prediction
        )


        # Store CGPA
       

        return redirect(url_for("dashboard"))

    # GET request: determine ATS score to show on form
    try:
        resume = get_latest_resume(session.get("user_id"))
    except Exception:
        resume = None

    if resume:
        ats_score = getattr(resume, "ATSScore", 0)
    else:
        ats_score = 0

    return render_template(
        "predictor.html",
        ats_score=ats_score
    )


# ==================================================
# Company Recommendation
# ==================================================

@app.route("/recommender")
@login_required
def recommender():

    prediction = get_prediction_data(session["user_id"])
    resume = get_latest_resume(session["user_id"])

    if prediction is None:
        flash("Please generate your placement prediction first.", "warning")
        return redirect(url_for("predictor"))

    if resume is None:
        flash("Please upload your resume first.", "warning")
        return redirect(url_for("upload"))

    cgpa = prediction.CGPA

    branch = session["branch"]

    skills = resume.FoundSkills.split(",") if resume.FoundSkills else []

    companies = recommend_companies(
        branch,
        cgpa,
        skills
    )

    return render_template(
        "recommender.html",
        companies=companies.to_dict(orient="records")
    )


# ==================================================
# Interview
# ==================================================

@app.route("/interview", methods=["GET", "POST"])
@login_required
def interview():

    questions = []

    if request.method == "POST":

        branch = request.form["branch"]
        company = request.form["company"]
        role = request.form["role"]
        interview_type = request.form["interview_type"]
        difficulty = request.form["difficulty"]

        questions = get_questions(
            branch,
            company,
            role,
            interview_type,
            difficulty
        )

    return render_template(
        "interview.html",
        questions=questions
    )
@app.route("/get_branch_data/<branch>")
@login_required
def get_branch_data(branch):

    companies = get_companies_by_branch(branch)
    roles = get_roles_by_branch(branch)

    return jsonify({
        "companies": companies,
        "roles": roles
    })
# ==================================================
# About
# ==================================================

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect(url_for("login"))
# ==================================================
# Run App
# ==================================================

if __name__ == "__main__":
    app.run(debug=True)
