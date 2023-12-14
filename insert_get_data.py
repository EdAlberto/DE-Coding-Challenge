import pandas as pd
from json import loads
import requests

#Read data from three csv files
departments = pd.read_csv('data/departments.csv',names=["id", "department"])
hired_employees = pd.read_csv('data/hired_employees.csv',names=["id", "name","datetime","department_id","job_id"])
jobs = pd.read_csv('data/jobs.csv',names=["id", "job"])

#Cast from dataframe to JSON structure
departments_r = departments.to_json(orient="records")
hired_employees_r = hired_employees.to_json(orient="records")
jobs_r = jobs.to_json(orient="records")

departments_parsed = loads(departments_r)
hired_employees_parsed = loads(hired_employees_r)
jobs_parsed = loads(jobs_r)

#print(departments_parsed)

#Insert data in the database by API REST


for i in departments_parsed:
    requests.post('http://127.0.0.1:5000/api/departments/add', json=i)

for i in hired_employees_parsed:
    requests.post('http://127.0.0.1:5000/api/employees/add', json=i)

for i in jobs_parsed:
    requests.post('http://127.0.0.1:5000/api/jobs/add', json=i)

# Get queries results from section 2 from endpoints

#Query 1
query1 = requests.get('http://127.0.0.1:5000/api/get_query1').json()
print(query1)

#Query 2
query2 = requests.get('http://127.0.0.1:5000/api/get_query2').json()
print(query2)