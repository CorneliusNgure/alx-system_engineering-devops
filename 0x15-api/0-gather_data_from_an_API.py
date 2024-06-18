#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id))

    if user_response.status_code != 200:
        sys.exit(1)

    user = user_response.json()

    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task))
