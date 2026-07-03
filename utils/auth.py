from database.db_connection import get_connection
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


# ===========================================
# Register User
# ===========================================

def register_user(full_name,
                  email,
                  password,
                  branch,
                  college):

    conn = get_connection()

    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute(
        "SELECT * FROM Users WHERE Email = ?",
        (email,)
    )

    user = cursor.fetchone()

    if user:

        conn.close()

        return False

    password_hash = generate_password_hash(password)

    cursor.execute("""

        INSERT INTO Users
        (FullName,
         Email,
         PasswordHash,
         Branch,
         College)

        VALUES
        (?, ?, ?, ?, ?)

    """,

    (
        full_name,
        email,
        password_hash,
        branch,
        college
    ))

    conn.commit()

    conn.close()

    return True


# ===========================================
# Login User
# ===========================================

def login_user(email, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM Users WHERE Email=?",

        (email,)

    )

    user = cursor.fetchone()

    conn.close()

    if user is None:

        return None

    if check_password_hash(user.PasswordHash, password):

        return user

    return None