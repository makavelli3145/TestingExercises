from app.user_service import *
import sqlite3
import pytest

'''
Q2: Mocking an Internal Call
'''
def test_process_user_exists():
    db_result = process_user(1)
    assert db_result is not None

def test_process_user_returns_valid_type():
    db_result = process_user(1)
    assert type(db_result) == str

def test_process_user_returns_valid_output_format():
    db_result = process_user(1)
    assert "User " in db_result

'''
Q4: Mocking Database Operations
'''
@pytest.fixture(scope="function")
def db_connection():
    conn = sqlite3.connect(":memory:")  # In-memory DB for testing
    yield conn
    conn.close()

def test_add_user_success(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    db_connection.commit()

    user = {"name": "Alice"}
    add_user(db_connection, user)

    cursor.execute("SELECT name FROM users WHERE id = 1")
    result = cursor.fetchone()
    assert result[0] == user["name"]

def test_add_user_already_exists(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    db_connection.commit()

    add_user(db_connection, {"name": "Makaveli"})
    result = add_user(db_connection, {"name": "Makaveli"})
    assert result[0] == 0

def test_add_user_fail(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    db_connection.commit()

    user = {"name": 123}

    with pytest.raises(ValueError):
        add_user(db_connection, user)

