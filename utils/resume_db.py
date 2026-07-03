from database.db_connection import execute_query, execute_non_query

# ==========================================
# Save Resume Analysis
# ==========================================

def save_resume_analysis(
    user_id,
    resume_file,
    ats_score,
    found_skills,
    missing_skills
):

    query = """
    INSERT INTO ResumeAnalysis
    (
        UserID,
        ResumeFile,
        ATSScore,
        FoundSkills,
        MissingSkills
    )
    VALUES (?, ?, ?, ?, ?)
    """

    execute_non_query(
        query,
        (
            user_id,
            resume_file,
            ats_score,
            ",".join(found_skills),
            ",".join(missing_skills)
        )
    )


# ==========================================
# Get Latest Resume Analysis
# ==========================================

def get_latest_resume(user_id):

    query = """
    SELECT TOP 1 *
    FROM ResumeAnalysis
    WHERE UserID=?
    ORDER BY UploadDate DESC
    """

    rows = execute_query(query, (user_id,))

    if len(rows) == 0:
        return None

    return rows[0]
def get_latest_resume(user_id):

    query = """
    SELECT TOP 1
        ATSScore,
        ResumeFile,
        FoundSkills,
        MissingSkills
    FROM ResumeAnalysis
    WHERE UserID=?
    ORDER BY UploadDate DESC
    """

    rows = execute_query(query, (user_id,))

    if rows:
        return rows[0]

    return None