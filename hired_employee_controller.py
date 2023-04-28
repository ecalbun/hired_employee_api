from db import get_db
import datetime



# HIRED EMPLOYEES ACTIONS
def get_last_id_hired_employees():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT MAX(id)+1 as id_hired_employees from hired_employees"
    cursor.execute(statement)
    row = cursor.fetchone()
    if row[0] is None:
        return 1
    else:
        return row[0]
    

def get_hiredemployees():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * from hired_employees"
    cursor.execute(query)
    return cursor.fetchall()

def insert_hired_employee(name,department_id,job_id):
    db = get_db()
    cursor = db.cursor()
    hired_id =get_last_id_hired_employees()
    current_date = datetime.date.today().isoformat()
    statement = f"INSERT INTO hired_employees (id,name,datetime,department_id,job_id) values ({hired_id},'?','{current_date}',?,?);"
    cursor.execute(statement, [name,department_id,job_id])
    db.commit()
    return True

#def delete_hired_employee():
    #todo

#def get_hired_employee_by_id():
    #todo

#def update_hired_employee():
    #todo


## DEPARTMENTS ACTIONS    
def get_last_id_department():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT MAX(id)+1 as id_department from departments"
    cursor.execute(statement)
    row = cursor.fetchone()
    if row[0] is None:
        return 1
    else:
        return row[0]
    
def get_departments():
    db = get_db()
    cursor = db.cursor()
    query = "select * from departments"
    cursor.execute(query)
    return cursor.fetchall()

def insert_department(name):
    db = get_db()
    cursor = db.cursor()
    id = get_last_id_job()
    print(id)
    statement = f"INSERT INTO departments(id,department) VALUES ({id},?)"
    cursor.execute(statement, [name])
    db.commit()
    return True

def delete_department(id):
    db = get_db()
    cursor = db.cursor()
    sql_statement = "DELETE FROM departments WHERE id = ?"
    cursor.execute(sql_statement, [id])
    db.commit()
    return True

def get_department_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name FROM departments WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def update_department(id,name):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE departments SET name = ? WHERE id = ?"
    cursor.execute(statement, [name, id])
    db.commit()
    return True


## JOBS ACTIONS
def get_last_id_job():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT MAX(id)+1 as id_hired_employees from jobs"
    cursor.execute(statement)
    row = cursor.fetchone()
    if row[0] is None:
        return 1
    else:
        return row[0]


def get_jobs():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM jobs"
    cursor.execute(query)
    return cursor.fetchall()
    

def get_last_id_job():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT MAX(id)+1 as id_job from jobs"
    cursor.execute(statement)
    row = cursor.fetchone()
    if row[0] is None:
        return 1
    else:
        return row[0]

def insert_job(name):
    db = get_db()
    cursor = db.cursor()
    id = get_last_id_job()
    print(id)
    statement = f"INSERT INTO jobs(id,job) VALUES ({id},?)"
    cursor.execute(statement, [name])
    db.commit()
    return True

#def delete_job():
    #todo

#def get_job_by_id():
    #todo

#def update_job():
    #todo