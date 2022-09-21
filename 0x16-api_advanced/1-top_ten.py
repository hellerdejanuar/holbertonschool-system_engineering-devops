#!/usr/bin/python3
""" Reddit API module """


def top_ten(subreddit):
    """ Returns number of suscribers of a subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)

    data = resp.json().get('data').get('children')
    print(data)
    for count, elem in enumerate(data):
        if count >= 10:
            break
        print(elem.get(count).get('title'))
    