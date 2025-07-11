def fetch_user_from_db(user_id: int) -> dict:
    return {
        "status": "success",
        "user_id": user_id,
        "username": "Mak"
    }

def process_user(user_id: int) -> str:
    db_result = fetch_user_from_db(user_id)
    return "User " + db_result["username"]
