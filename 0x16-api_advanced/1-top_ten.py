#!/usr/bin/python3
""" Reddit API module """


def top_ten(subreddit):
    """ Returns number of suscribers of a subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp is None:
        print('None')
    else:
        data = resp.json().get('data').get('children')
        for count, elem in enumerate(data):
            if count >= 10:
                break
            print(elem.get('data').get('title'))
            
