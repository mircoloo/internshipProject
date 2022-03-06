#!python3
import ApiKeys.apiKey as k
import tweepy
import pandas as pd

def getClient():
    client = tweepy.Client(bearer_token=k.BEARER_TOKEN, consumer_key=k.API_KEY, consumer_secret=k.API_SECRET_KEY, access_token=k.ACCESS_TOKEN, access_token_secret=k.ACCESS_SECRET_TOKEN)
    return client

def searchTweets(query, maxResults=10):
    client = getClient()
    tweets = client.search_recent_tweets(query=query, max_results=maxResults)
    #tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations','created_at'],media_fields=['preview_image_url'], max_results=maxResults)
    tweet_data = tweets.data
    result = []
    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {}
            obj['ID'] = tweet.id
            obj['text'] = tweet.text
            result.append(obj)
    else:
        return ''
    return result

for x in searchTweets("truffa sms"):
    print(x)

#prove conversione to JSON 
""" json_file = df.to_json(orient='records')
fileHandler = open("tweet_json.json", "a+")
fileHandler.write(json_file) """

    







