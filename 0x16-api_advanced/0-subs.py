#!/usr/bin/python3
""" Reddit API module """


def number_of_subscribers(subreddit):
    """ Returns number of suscribers of a subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    return resp.json().get('data').get('subscribers') or 0
