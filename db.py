import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
USERS_DB = BASE_DIR / "users.db"

BASE_DIR = Path(__file__).resolve().parent
NOTES_DB = BASE_DIR / "notes.db"

def get_connection_users():
    return sqlite3.connect(USERS_DB)

def get_connection_notes():
    return sqlite3.connect(NOTES_DB)

