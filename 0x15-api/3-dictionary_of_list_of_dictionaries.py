#!/usr/bin/python3
"""
    API requests module
    this module fetches data from API
"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    n_tasks_total = 0
    n_tasks_done = 0
    tasks_dict = {}

    tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos'
                ).json()
    users_info = requests.get(
               'https://jsonplaceholder.typicode.com/users'
               ).json()

    # Write data in json format
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:

        for task in tasks:
            user_id = task.get('userId')
            for user in users_info:
                if user['id'] == user_id:
                    username = user['username']
                    break

            row = {'task': task.get('title'),
                   'completed': task.get('completed'),
                   'username': username}

            if not str(user_id) in tasks_dict.keys():
                tasks_dict[str(user_id)] = []
            tasks_dict[str(user_id)].append(row)
        json.dump(tasks_dict, f)
