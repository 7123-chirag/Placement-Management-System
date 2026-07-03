from database.db_connection import execute_non_query, execute_query


# ==========================================================
# Save Placement Prediction
# ==========================================================

def save_prediction(
    user_id,
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
):

    query = """
    INSERT INTO PlacementPredictions
    (
        UserID,
        CGPA,
        Skills,
        Projects,
        Internships,
        Certifications,
        Coding,
        Communication,
        DSA,
        Backlogs,
        PlacementChance
    )
    VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    execute_non_query(
        query,
        (
            user_id,
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
    )


# ==========================================================
# Get Latest Prediction
# ==========================================================

def get_latest_prediction(user_id):

    query = """
    SELECT TOP 1 *
    FROM PlacementPredictions
    WHERE UserID = ?
    ORDER BY CreatedAt DESC
    """

    rows = execute_query(query, (user_id,))

    if rows:
        return rows[0]

    return None


# ==========================================================
# Get Prediction Data
# ==========================================================

def get_prediction_data(user_id):

    query = """
    SELECT TOP 1
        CGPA,
        Skills,
        Projects,
        Internships,
        Certifications,
        Coding,
        Communication,
        DSA,
        Backlogs,
        PlacementChance
    FROM PlacementPredictions
    WHERE UserID = ?
    ORDER BY CreatedAt DESC
    """

    rows = execute_query(query, (user_id,))

    if rows:
        return rows[0]

    return None


# ==========================================================
# Check if Prediction Exists
# ==========================================================

def prediction_exists(user_id):

    query = """
    SELECT COUNT(*)
    AS Total
    FROM PlacementPredictions
    WHERE UserID = ?
    """

    rows = execute_query(query, (user_id,))

    if rows:
        return rows[0].Total > 0

    return False