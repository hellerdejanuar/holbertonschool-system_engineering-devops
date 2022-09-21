#!/usr/bin/python3
""" Reddit API module """


def recurse(subreddit, hot_list=[], after=None):
    """ Returns top 10 hot post titles of a subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        print(None)
    else:
        data = resp.json().get('data').get('children')
        for elem in data:
            hot_list.append((elem.get('data').get('title')))

        after = resp.json().get('data').get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
