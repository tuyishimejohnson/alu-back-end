#!/usr/bin/python3

import sys
import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todos_data if task.get("completed")]

        # Display progress
        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos_data)}):")
        for task in completed_tasks:
            print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
