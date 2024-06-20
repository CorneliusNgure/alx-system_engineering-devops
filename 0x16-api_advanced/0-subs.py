#!/usr/bin/python3
"""Queries about the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
        Queries the Reddit API and returns the number of subscribers
        (not active users, total subscribers) for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Google Chrome Version 126.0.6478.115'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        if response == 404:
            return 0
    except Exception:
        return 0
