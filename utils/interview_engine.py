import pandas as pd

# ============================================
# Load Interview Dataset (Only Once)
# ============================================

interview_df = pd.read_csv("dataset/interview_questions_1000.csv")

# Remove extra spaces from column names
interview_df.columns = interview_df.columns.str.strip()

# Remove extra spaces from string values
for col in interview_df.columns:
    if interview_df[col].dtype == "object":
        interview_df[col] = interview_df[col].astype(str).str.strip()

print(interview_df.columns.tolist())
print(interview_df.head())


# ============================================
# Get Companies According to Branch
# ============================================

def get_companies_by_branch(branch):

    branch = branch.strip()

    companies = sorted(
        interview_df.loc[
            interview_df["branch"] == branch,
            "company"
        ].dropna().unique().tolist()
    )

    print(f"Branch: {branch}")
    print(f"Companies: {companies}")

    return companies


# ============================================
# Get Roles According to Branch
# ============================================

def get_roles_by_branch(branch):

    branch = branch.strip()

    roles = sorted(
        interview_df.loc[
            interview_df["branch"] == branch,
            "role"
        ].dropna().unique().tolist()
    )

    print(f"Roles: {roles}")

    return roles


# ============================================
# Get Interview Questions
# ============================================

def get_questions(
    branch,
    company,
    role,
    interview_type,
    difficulty,
    n_questions=10
):

    branch = branch.strip()
    company = company.strip()
    role = role.strip()
    interview_type = interview_type.strip()
    difficulty = difficulty.strip()

    all_questions = interview_df.drop_duplicates(
        subset=["question"]
    ).copy()

    # Level 1 : Exact Match
    result = all_questions[
        (all_questions["branch"] == branch) &
        (all_questions["company"] == company) &
        (all_questions["role"] == role) &
        (all_questions["interview_type"] == interview_type) &
        (all_questions["difficulty"] == difficulty)
    ]

    # Level 2 : Same Company
    if len(result) < n_questions:
        company_df = all_questions[
            (all_questions["branch"] == branch) &
            (all_questions["company"] == company)
        ]
        result = pd.concat([result, company_df])

    # Level 3 : Same Branch
    if len(result) < n_questions:
        branch_df = all_questions[
            all_questions["branch"] == branch
        ]
        result = pd.concat([result, branch_df])

    # Level 4 : Any Question
    if len(result) < n_questions:
        result = pd.concat([result, all_questions])

    result = (
        result
        .drop_duplicates(subset=["question"])
        .sample(frac=1, random_state=42)
        .head(n_questions)
    )

    return result.to_dict(orient="records")