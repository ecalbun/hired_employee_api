from flask import Flask, jsonify, request
import hired_employee_controller
from db import create_tables
import pdb
import logging


app = Flask(__name__)

#HIRED_EMPLOYEES
@app.route('/hired_employees', methods=["GET"])
def get_hired_employees():
    hired_employees = hired_employee_controller.get_hiredemployees()
    return jsonify(hired_employees)



#DEPARTMENTS ACTION
@app.route('/departments', methods=["GET"])
def get_departments():
    departments = hired_employee_controller.get_departments()
    return jsonify(departments)

@app.route("/departments/<id>", methods=["DELETE"])
def delete_department(id):
    result = hired_employee_controller.delete_department(id)
    return jsonify(result)

@app.route("/departments/<id>", methods=["GET"])
def get_department_by_id(id):
    result = hired_employee_controller.get_department_by_id(id)
    return jsonify(result)

@app.route("/departments", methods=["PUT"])
def update_department():
    department = request.get_json()
    id = department["id"]
    name = department["name"]
    result = hired_employee_controller.update_department(id, name)
    return jsonify(result)



#JOBS
@app.route('/jobs', methods=["GET"])
def get_jobs():
    jobs = hired_employee_controller.get_jobs()
    return jsonify(jobs)


@app.route("/job", methods=["POST"])
def insert_job():
    job_data = request.get_json()
    name = job_data["name"]

    if name.strip() == '':
        #no se inserta
        with open('jobs_unregistered.txt', 'a') as file:
            file.write(f'{name}\n')
        return jsonify({'error': 'Missing required field "Name"'}), 400
    else:
        result = hired_employee_controller.insert_job(name)
        return jsonify(result)
    
    

if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)