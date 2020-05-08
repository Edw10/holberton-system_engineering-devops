#!/usr/bin/python3
"""top 10"""
import requests


def top_ten(subreddit):
    """get the top 10"""
    user = {}
    user["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    data = requests.get(
        "http://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers=user
    )
    if data.status_code == 200:
        data = data.json()
        for posts in data["data"]["children"]:
            print(posts["data"]["title"])
    else:
        print(None)
