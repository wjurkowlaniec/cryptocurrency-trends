# Import the required modules
from twython import Twython
from datetime import date, timedelta

import config

tweetsXiteration = 100  # Where 100 is the max
dateTo = str(date.today())  # Inclusive (YYYY-MM-DD)
dateFrom = str(date.today() - timedelta(days=1))  # Exclusive (YYYY-MM-DD)


def get_twitter_mention_count(keyword):
    done = False  # Must be false
    tw = Twython(config.secrets['twitter']['consumer_key'], config.secrets['twitter']['consumer_secret'],
                 config.secrets['twitter']['access_token'], config.secrets['twitter']['access_token_secret'])
    results = tw.cursor(tw.search, q=keyword, count=tweetsXiteration, since=dateFrom, until=dateTo, result_type='mixed')
    count = 0
    for res in results:
        count += 1
    return count

    # TODO twython.exceptions.TwythonRateLimitError: Twitter API returned a 429 (Too Many Requests), Rate limit exceeded


if __name__ == "__main__":
    print(get_twitter_mention_count('raiblocks'))
