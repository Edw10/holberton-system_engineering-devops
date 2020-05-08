#!/usr/bin/python3
"""number of suscriptors by subreddit"""
import requests


def number_of_subscribers(subreddit):
    """get the number of subscribers"""
    user = {}
    user["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    data = requests.get(
        "http://www.reddit.com/r/{}/about.json".format(subreddit),
        headers=user
    )
    if data.status_code == 200:
        data = data.json()
        return data["data"]["subscribers"]
    return data.status_code
