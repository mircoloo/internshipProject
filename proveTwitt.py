#!python3

import tweepy
import Prove.pyScripts.ApiKeys.apiKey as k



query = 'SMS truffa'
client = tweepy.Client(bearer_token=k.BEARER_TOKEN)
response = client.search_recent_tweets(query=query)

print(response)



