#!/usr/bin/python3
"""return all hot psot recursively"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """get hot post"""
    user = {}
    user["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    data = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
            subreddit, after
        ),
        headers=user
    )
    if data.status_code != 200:
        return None

    data = data.json()
    for posts in data["data"]["children"]:
        hot_list.append(posts["data"]["title"])

    after = data["data"]["after"]

    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
