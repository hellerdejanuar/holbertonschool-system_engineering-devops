#!/usr/bin/python3
"""
    API requests module
    this module fetches data from API
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    n_tasks_total = 0
    n_tasks_done = 0

    user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id)).json()
    user_name = requests.get(
               'https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).json()['name']

    # Write data in csv format
    with open('{}.csv'.format(user_id), 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            row = [task.get('userId'),
                   user_name,
                   task.get('completed'),
                   task.get('title')]
            writer.writerow(row)
