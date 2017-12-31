import json

import praw

import config

reddit = None


def init_reddit():
    global reddit
    with open(config.secret_file_location, 'r') as f:
        secrets = json.load(f)
        reddit_auth = secrets['reddit']
    reddit = praw.Reddit(client_id=reddit_auth['client_id'], client_secret=reddit_auth['client_secret'],
                         user_agent=reddit_auth['user_agent'])
    assert reddit.read_only


def get_subreddit_user_count(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit.accounts_active
