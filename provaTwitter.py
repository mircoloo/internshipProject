#!python3
import pandas as pd
import tweepy
import pyScripts.ApiKeys.apiKey as k

client = tweepy.Client(bearer_token=k.BEARER_TOKEN)

query = "SMS truffa"

response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang', 'context_annotations', 'entities', 'public_metrics'])

columns = ['Time', 'Tweet', 'Lang']
data = []
for tweet in response.data:
    data.append([tweet.created_at, tweet.text, tweet.lang])#tweet.entities['mentions']  if 'mentions' in tweet.entities else "--"])

df = pd.DataFrame(data,columns=columns)
print(df)

df.to_json('twi.json', orient='records', lines=True)