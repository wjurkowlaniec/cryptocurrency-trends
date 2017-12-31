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
    sub = reddit.subreddit(subreddit_name)
    return sub.subscribers


def get_subreddit_active_users(subreddit_name):
    sub = reddit.subreddit(subreddit_name)
    return sub.accounts_active


def get_crypto_popularity(crypto):
    total_users = 0
    active_users = 0
    for subreddit in config.coins_info[crypto]['subreddits']:
        total_users += get_subreddit_user_count(subreddit)
        active_users += get_subreddit_active_users(subreddit)
    return total_users


def get_all_crypto_info():
    output = {}
    for coin in config.coins_info.keys():
        output[coin] = {'total_users': get_crypto_popularity(coin), 'active_users': get_subreddit_active_users(coin)}
    return output


if __name__ == "__main__":
    init_reddit()
    print(get_all_crypto_info())
