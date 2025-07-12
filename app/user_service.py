'''
Q2: Mocking an Internal Call
'''

def fetch_user_from_db(user_id: int) -> dict:
    return {
        "status": "success",
        "user_id": user_id,
        "username": "Mak"
    }

def process_user(user_id: int) -> str:
    db_result = fetch_user_from_db(user_id)
    return "User " + db_result["username"]

'''
Q4: Mocking Database Operations
'''
def add_user(db_conn, user: dict) -> bool:
    if not isinstance(user["name"], str):
        raise ValueError("User name must be a string")

    try:
        cursor = db_conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (user["name"],))
        db_conn.commit()
        return True

    except Exception as e:
        db_conn.rollback()
        print(f"Database error: {e}")
        raise