from sqlite3 import Cursor
from xmlrpc import client

import ApiKeys.apiKey as k
import tweepy

def verifyCred(api):
    try:
        api.verify_credentials()
        print("Authenicated properly!")
    except:
        print("Something wrong in authentication...")


client = tweepy.Client(bearer_token=k.BEARER_TOKEN)

query = "SMS truffa"

response = client.search_recent_tweets(query=query, tweet_fields=['created_at', 'lang'], max_results=12)

for tweet in response.data:
    print(tweet.created_at)
    print(f"{tweet.text}\n")
