import pdfplumber
from docx import Document

# ==========================
# Branch-wise Keywords
# ==========================

BRANCH_KEYWORDS = {

"CSE": {

    # ================= Programming Languages =================

    "Programming": [

        "c",
        "c++",
        "java",
        "python",
        "javascript",
        "typescript",
        "go",
        "golang",
        "rust",
        "kotlin",
        "swift",
        "php",
        "r",
        "matlab"

    ],

    # ================= Web Development =================

    "Web Development": [

        "html",
        "css",
        "bootstrap",
        "tailwind",
        "sass",
        "jquery",

        "react",
        "next.js",
        "angular",
        "vue",

        "node.js",
        "express",

        "django",
        "flask",
        "fastapi",

        "spring",
        "spring boot",

        "laravel"

    ],

    # ================= Databases =================

    "Database": [

        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "sqlite",
        "firebase",
        "oracle",
        "redis"

    ],

    # ================= Data Science =================

    "Data Science": [

        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "plotly",
        "scipy",
        "statistics",
        "data analysis",
        "eda"

    ],

    # ================= Artificial Intelligence =================

    "AI / ML": [

        "machine learning",
        "deep learning",
        "artificial intelligence",

        "tensorflow",
        "keras",
        "pytorch",

        "opencv",

        "scikit-learn",

        "xgboost",
        "lightgbm",

        "cnn",
        "rnn",
        "lstm",
        "transformer"

    ],

    # ================= NLP =================

    "Natural Language Processing": [

        "nlp",
        "bert",
        "gpt",
        "word2vec",
        "tokenization"

    ],

    # ================= Computer Vision =================

    "Computer Vision": [

        "computer vision",
        "image processing",
        "object detection",
        "yolo"

    ],

    # ================= Core CS =================

    "Core CS": [

        "data structures",
        "algorithms",
        "dsa",

        "operating systems",

        "computer networks",

        "dbms",

        "software engineering",

        "object oriented programming"

    ],

    # ================= Cloud =================

    "Cloud": [

        "aws",
        "azure",
        "gcp",
        "cloud computing"

    ],

    # ================= DevOps =================

    "DevOps": [

        "docker",
        "kubernetes",
        "jenkins",
        "terraform",
        "github actions"

    ],

    # ================= Version Control =================

    "Version Control": [

        "git",
        "github",
        "gitlab"

    ],

    # ================= APIs =================

    "API Development": [

        "rest api",
        "restful api",
        "graphql",
        "postman"

    ],

    # ================= Mobile Development =================

    "Mobile Development": [

        "android",
        "android studio",
        "flutter",
        "react native"

    ],

    # ================= Cyber Security =================

    "Cyber Security": [

        "cyber security",
        "ethical hacking",
        "penetration testing",
        "network security"

    ],

    # ================= Testing =================

    "Testing": [

        "selenium",
        "pytest",
        "junit"

    ],

    # ================= Development Tools =================

    "Tools": [

        "vs code",
        "visual studio",
        "colab",
        "jupyter notebook",
        "anaconda"

    ],

    # ================= Data Engineering =================

    "Data Engineering": [

        "hadoop",
        "spark",
        "kafka",
        "airflow"

    ],

    # ================= Operating Systems =================

    "Platforms": [

        "linux",
        "windows",
        "bash",
        "shell scripting"

    ],

    # ================= Problem Solving =================

    "Problem Solving": [

        "dynamic programming",
        "greedy algorithm",
        "backtracking",
        "binary search",

        "linked list",
        "stack",
        "queue",
        "tree",
        "graph",
        "heap",
        "hashmap",
        "trie",

        "multithreading",
        "concurrency",
        "socket programming"

    ],

    # ================= Resume Strength =================

    "Experience": [

        "project",
        "internship",
        "hackathon",
        "leetcode",
        "codechef",
        "codeforces",
        "github profile"

    ]

},

"ECE": [
        "verilog","vhdl","fpga","rtl","vivado","vitis","xilinx",
        "matlab","simulink","ltspice","pspice","kicad","eagle",

        "embedded",
        "embedded systems",
        "embedded c",

        "arduino",
        "esp32",
        "stm32",

        "pcb",
        "pcb design",
        "pcb fabrication",

        "microcontroller",
        "8051",
        "arm",

        "uart",
        "spi",
        "i2c",
        "can",

        "adc",
        "dac",

        "vlsi",
        "asic",
        "soc",

        "iot",

        "digital electronics",
        "analog electronics",

        "signal processing",

        "hardware accelerator",

        "hardware/software co-design",

        "communication systems",

        "wireless communication"
    ],

    "Mechanical": [
        "autocad","solidworks","catia","ansys",
        "creo","manufacturing","thermodynamics",
        "fluid mechanics","cad","cam",
        "cnc","automobile","robotics"
    ],

    "Civil": [
        "autocad","staad","etabs","revit",
        "surveying","structural analysis",
        "construction","geotechnical",
        "transportation engineering"
    ],

    "Electrical": [
        "power systems","electrical machines",
        "protection","relay","matlab",
        "pscad","simulink","transformer",
        "motor","plc","scada"
    ]
}

# ==========================
# Skill Aliases
# ==========================

SKILL_ALIASES = {

    "machine learning": [
        "machine learning",
        "ml"
    ],

    "artificial intelligence": [
        "artificial intelligence",
        "ai"
    ],

    "operating systems": [
        "operating systems",
        "os"
    ],

    "computer networks": [
        "computer networks",
        "cn"
    ],

    "object oriented programming": [
        "object oriented programming",
        "oop",
        "oops"
    ],

    "database management system": [
        "database management system",
        "dbms"
    ],

    "javascript": [
        "javascript",
        "js"
    ],

    "tensorflow": [
        "tensorflow",
        "tf"
    ],

    "node.js": [
        "node.js",
        "nodejs",
        "node"
    ],

    "c++": [
        "c++",
        "cpp"
    ]
}
# ==========================
# Extract Resume Text
# ==========================

def extract_text(path):

    text = ""

    if path.endswith(".pdf"):

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:
                text += page.extract_text() or ""

    elif path.endswith(".docx"):

        doc = Document(path)

        for para in doc.paragraphs:
            text += para.text

    return text.lower()


# ==========================
# ATS Score
# ==========================

# ==========================
# ATS Score
# ==========================

# ==========================
# ATS Score
# ==========================

def ats_score(path, branch):

    resume = extract_text(path)

    branch_keywords = BRANCH_KEYWORDS.get(branch, {})

    found = []
    missing = []
    category_scores = {}

    total_found = 0
    total_skills = 0

    # --------------------------
    # Category-based branches
    # --------------------------

    if isinstance(branch_keywords, dict):

        for category, skills in branch_keywords.items():

            category_found = []
            category_missing = []

            for skill in skills:

                aliases = SKILL_ALIASES.get(skill, [skill])

                skill_found = False

                for alias in aliases:

                    if alias.lower() in resume:

                        skill_found = True
                        break

                if skill_found:

                    category_found.append(skill)
                    found.append(skill)

                else:

                    category_missing.append(skill)
                    missing.append(skill)

            total_found += len(category_found)
            total_skills += len(skills)

            if len(skills) > 0:

                category_scores[category] = round(
                    (len(category_found) / len(skills)) * 100,
                    1
                )

            else:

                category_scores[category] = 0

    # --------------------------
    # Old list-based branches
    # --------------------------

    else:

        for skill in branch_keywords:

            aliases = SKILL_ALIASES.get(skill, [skill])

            skill_found = False

            for alias in aliases:

                if alias.lower() in resume:

                    skill_found = True
                    break

            if skill_found:

                found.append(skill)

            else:

                missing.append(skill)

        total_found = len(found)
        total_skills = len(branch_keywords)

    # --------------------------
    # Final ATS Score
    # --------------------------

    if total_skills == 0:

        score = 0

    else:

        score = round((total_found / total_skills) * 100)

    return score, found, missing, category_scores