#!/usr/bin/python3
"""return all hot psot recursively"""
import requests
import operator

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

def count_words(subreddit, word_list, i=0, hot_list=[], res={}):

    after = ''
    subs = word_list[i].split(',')[0]
    patterns = []
    if len(hot_list) == 0:
        hot_list = recurse(subreddit, hot_list, after)

    for el in hot_list:
        split_line = el.split(' ')
        for w in split_line:
            if subs == w or subs.capitalize() == w:
                patterns.append(w)

    res[subs] = len(patterns)
    i += 1

    if i != len(word_list):
        count_words(subreddit, word_list, i, hot_list, res)
    else:
        sort_res = {}
        sort_res = dict(sorted(res.items(), key=operator.itemgetter(1),
                               reverse=True)
        )
        for k,v in  sort_res.items():
            if v > 0:
                print('{}: {}'.format(k, v))
