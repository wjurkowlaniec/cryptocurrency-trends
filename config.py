import json

secret_file_location = "secrets.json"

secrets = {}
with open(secret_file_location, 'r') as f:
    secrets = json.load(f)

coins_info = {
    'eth': {
        'display_name': 'Etherum',
        'subreddits': ['etherium']
    }
}

reddit = {
    'crypto_subs': ['darknetmarkets', 'bitcoin', 'ethereum', 'dogecoin', 'cryptocurrency', 'btc', 'bitcoinmarkets']
}
