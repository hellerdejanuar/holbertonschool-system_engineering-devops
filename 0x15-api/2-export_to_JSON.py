#!/usr/bin/python3
"""
    API requests module
    this module fetches data from API
"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    n_tasks_total = 0
    n_tasks_done = 0
    task_list = []

    user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id)).json()
    user_info = requests.get(
               'https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).json()

    # Write data in json format
    with open('{}.json'.format(user_id), 'w', encoding='utf-8') as f:
        for task in user_tasks:
            row = {'task':task.get('title'),
                   'completed':task.get('completed'),
                   'username':user_info.get('username')}
            task_list.append(row)

        usr_task_dict = {str(user_id) : task_list}
        json.dump(usr_task_dict, f)
