import sqlite3
DATABASE_NAME = "employees.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS hired_employees(
	        id INTEGER NOT NULL ,
	        name TEXT NOT NULL ,
	        datetime STRING NOT NULL ,
	        department_id INTEGER NOT NULL ,
	        job_id INTEGER NOT NULL 
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS departments(
            id INTEGER NOT NULL,
            department TEXT NOT NULL 
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS jobs(
            id INTEGER NOT NULL,
            job STRING NOT NULL
        )
        """
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)