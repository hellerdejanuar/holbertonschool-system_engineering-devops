#!/usr/bin/python3
""" Reddit API module """


def top_ten(subreddit):
    """ Returns top 10 hot post titles of a subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code != 200:
        print('None')
    else:
        data = resp.json().get('data').get('children')
        i = 0
        for elem in data:
            if i >= 10:
                break
            print(elem.get('data').get('title'))
            i = i + 1
