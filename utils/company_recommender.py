import pandas as pd
companies = pd.read_csv("data/placement_company_dataset_1000.csv")


def recommend_companies(branch, cgpa, skills):

    df = companies.copy()

    # Branch Filter
    df = df[
        df["Eligible Branches"].str.contains(
            branch,
            case=False,
            na=False
        )
    ]

    # CGPA Filter
    df = df[
        df["Minimum CGPA"] <= cgpa
    ]

    skills = [s.strip().lower() for s in skills]

    match_scores = []

    for _, row in df.iterrows():

        company_skills = [
            s.strip().lower()
            for s in row["Required Skills"].split(",")
        ]

        score = len(
            set(skills).intersection(company_skills)
        )

        match_scores.append(score)

    df["Match Score"] = match_scores

    df = df.sort_values(
        "Match Score",
        ascending=False
    )

    return df.head(15)