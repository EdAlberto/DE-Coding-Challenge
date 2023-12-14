This repository is a code challenge (section 1 API and section 2 SQL). The programming language is Python.

It has the scope to create a REST API to load data in a SQLite database tables from csv files and get two queries results based in the data of those tables.

The file are:
- create_db.py : Where the SQLite database and the three tables are created
- api.py : Where the REST API is created with Flask for loading data in the three tables and get the result of two queries(endpoints).
- insert_get_data.py : Where the API is invoqued and executes the processes to load the data in the three tables from three csv files and get the queries results.
- read_data.py : For print data to verify loading processes.

