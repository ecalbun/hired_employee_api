import sqlite3
import fastavro 
from fastavro import writer, reader, parse_schema
import datetime
import os
from db import get_db


def insert_job(id,name):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO jobs(id,job) VALUES (?,?)"
    cursor.execute(statement, [id,name])
    db.commit()
    return True

def restore_bkp_jobs(path):
    
    with open(f'{path}/jobs.avro', 'rb') as fo:
        for record in reader(fo):
            insert_job(record['id'],record['job'])



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
    cursor.execute(f"SELECT * FROM jobs")
    data = cursor.fetchall()
    schema = {
        'type': 'record',
        'name': 'jobs',
        'fields': [
            {'name': 'id', 'type': 'int'},
            {'name': 'job', 'type': 'string'} 
            ]
    }

    records = []
    for index in data:
        record = {
        "id": index[0],
        "job": index[1]
        }
        records.append(record)
    

    year, month, day = get_current_date()
    path = f'BKP/jobs/year={year}/month={month}/day={day}/'
    #os.makedirs(path)

    #
    with open(f'{path}/jobs.avro', 'wb') as f:
        fastavro.writer(f, schema, records)
    
    # Close connection to SQLite database
    conn.close()

if __name__ == "__main__":
    save_sqlite_table_to_avro()
    #path='BKP/jobs/year=2023/month=4/day=27'
    #restore_bkp_jobs(path)
   