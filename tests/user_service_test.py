from app.user_service import *

def test_process_user_exists():
    db_result = process_user(1)
    assert db_result is not None

def test_process_user_returns_valid_type():
    db_result = process_user(1)
    assert type(db_result) == str

def test_process_user_returns_valid_output_format():
    db_result = process_user(1)
    assert "User " in db_result