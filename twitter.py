# Import the required modules
from twython import Twython
from datetime import date, timedelta

import config

tweetsXiteration = 100  # Where 100 is the max
dateTo = str(date.today())  # Inclusive (YYYY-MM-DD)
dateFrom = str(date.today() - timedelta(days=7))  # Exclusive (YYYY-MM-DD)


def get_twitter_mention_count(keyword):
    done = False  # Must be false
    tw = Twython(config.secrets['twitter']['consumer_key'], config.secrets['twitter']['consumer_secret'],
                 config.secrets['twitter']['access_token'], config.secrets['twitter']['access_token_secret'])

    response = tw.search(q=keyword, count=tweetsXiteration, since=dateFrom, until=dateTo, result_type='mixed')
    countTweets = len(response['statuses'])
    if not ('next_results' in response['search_metadata']):
        done = True

    while not done:
        # Parsing information for maxID
        parse1 = response['search_metadata']['next_results'].split("&")
        parse2 = parse1[0].split("?max_id=")
        parse3 = parse2[1]
        maxID = parse3

        # Twitter is queried (again, this time with the addition of 'max_id')
        response = tw.search(q=keyword, count=tweetsXiteration, since=dateFrom, until=dateTo, max_id=maxID,
                             include_entities=1, result_type='mixed')

        countTweets = countTweets + len(response['statuses'])

        if not ('next_results' in response['search_metadata']):
            done = True
    return countTweets


if __name__ == "__main__":
    print(get_twitter_mention_count('raiblocks'))
