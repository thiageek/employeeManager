# Employee Manager

This application was built as an experiment to practice Python with Django as a web framework.

It allows you to manage employee's information through an admin panel or an API integration.

An employee have a name, an e-mail and belongs to a department.
A department have a name and contains none or many employees.

Create an user to access the admin panel:
`python3 manage.py createsuperuser`

To start the server run:
`python3 manage.py runserver`


## Admin Panel
`http://localhost:8000/admin`

## API integration
- List all employees: [`GET`] `http://localhost:8000/employees`
- Add an employee: [`POST`] `http://localhost:8000/employees/add`
  - `name`: string, required
  - `email`: string, required
  - `department`: integer, required
- Detail an employee: [`GET`] `http://localhost:8000/employees/x`
  - `x` is the employee's ID
- Update an employee: [`POST`] `http://localhost:8000/employees/update/x`
  - `x` is the employee's ID
  - `name`: string
  - `email`: string
  - `department`: integer
- Remove an employee: [`GET`] `http://localhost:8000/employees/remove/x`
  - `x` is the employee's ID
- List all departments and their employees: [`GET`] `http://localhost:8000/departments`
- Add an department: [`POST`] `http://localhost:8000/departments/add`
  - `name`: string, required
- Detail an department by ID or name and its employees: [`GET`] `http://localhost:8000/departments/x`
  - `x` is the department's ID or name
- Update an department: [`POST`] `http://localhost:8000/departments/update/x`
  - `x` is the department's ID
  - `name`: string
- Remove an department: [`GET`] `http://localhost:8000/departments/remove/x`
  - `x` is the department's ID

## Tests

Install Coverage:
`pip3 install coverage`

Run the tests:
`coverage run manage.py test employees -v 2`

After run the tests you can see the results in `htmlcov/index.html`.
