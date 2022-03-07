#!python3
import pandas as pd
import tweepy
import ApiKeys.apiKey as k

client = tweepy.Client(bearer_token=k.BEARER_TOKEN)

query = "SMS truffa"

response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang', 'context_annotations', 'entities', 'public_metrics'])

columns = ['Time', 'Tweet', 'Lang']
data = []
for tweet in response.data:
    data.append([str(tweet.created_at)[:10], str(tweet.text), tweet.lang])#tweet.entities['mentions']  if 'mentions' in tweet.entities else "--"])
    print(tweet.text)
df = pd.DataFrame(data,columns=columns)
print(df)



df.to_json('tweets.json', orient='records', lines=True)