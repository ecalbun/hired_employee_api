import sqlite3
import fastavro 
from fastavro import writer, reader, parse_schema
import datetime
import os
from db import get_db


def insert_job(id,name,datetime,department_id,job_id):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO hired_employees(id,name,datetime,department_id,job_id) VALUES (?,?,?,?,?)"
    cursor.execute(statement, [id,name,datetime,department_id,job_id])
    db.commit()
    return True


def restore_bkp_hired_employees(path):
    with open(f'{path}/hired_employees.avro', 'rb') as fo:
        for record in reader(fo):
            insert_job(record['id'],record['name'],record['datetime'],record['department_id'],record['job_id'])



def get_current_date():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return year, month, day

def save_sqlite_table_to_avro():
    # 
    conn = sqlite3.connect('employees.db')
    
    # 
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM hired_employees")
    data = cursor.fetchall()
    schema = {
        'type': 'record',
        'name': 'hired_employees',
        'fields': [
            {'name': 'id', 'type': 'int'},
            {'name': 'name', 'type': 'string'},
            {'name': 'datetime', 'type': 'string'} ,
            {'name': 'department_id', 'type': 'int'} ,
            {'name': 'job_id', 'type': 'int'} 
            ]
    }

    records = []
    for index in data:
        record = {
        "id": index[0],
        "name": index[1],
        "datetime": index[2],
        "department_id": index[3],
        "job_id": index[4]
        }
        records.append(record)
    

    year, month, day = get_current_date()
    path = f'BKP/hired_employees/year={year}/month={month}/day={day}/'
    os.makedirs(path)

    #
    with open(f'{path}/hired_employees.avro', 'wb') as f:
        fastavro.writer(f, schema, records)
    
    # Close connection to SQLite database
    conn.close()

if __name__ == "__main__":
    save_sqlite_table_to_avro()

    #path='BKP/hired_employees/year=2023/month=4/day=28'
    #restore_bkp_hired_employees(path)
   