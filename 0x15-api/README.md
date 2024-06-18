# API

This is a practice project consisting of a couple of tasks to demonstrate my understanding of working with APIs.

The data used is collected from [JSONPlaceholder REST API](https://jsonplaceholder.typicode.com/). 
The tasks demonstrate my understanding of exporting data as is from the site, exporting using CSV, and using JSON formats.

## TASKS
### Task 0: Gather data from an API
  * Write a Python script using the [JSONPlaceholder REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

  * Requirements:
      * You must use urlib or requests module
      * The script must accept an interger as a parameter, which is the employee ID.
      * The script must display on the standard output the employee TODO list progress.

### Task 1: Export to CSV
  * Using what you did in the task #0, extend your Python script to export data in the CSV format.

  * Requirements:
    * Records all tasks that are owned by this employee
    * Format must be: __"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"__
    * File name must be: __USER_ID.csv__

### Task 2: Export to JSON
  * Using what you did in the task #0, extend your Python script to export data in the JSON format.

  Requirements:
    * Records all tasks that are owned by this employee
    * Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    * File name must be: USER_ID.json

### Task 3: Dictionary of list of dictionaries
  * Using what you did in the task #0, extend your Python script to export data in the JSON format.

  Requirements:
    * Records all tasks from all employees
    * Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    * File name must be: todo_all_employees.json
