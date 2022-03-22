#!python3
import pandas as pd
import ApiKeys.apiKey as k
import json
import tweepy


client = tweepy.Client(bearer_token=k.BEARER_TOKEN)

r = client.get_tweet(id='1503723497356509188',media_fields=['preview_image_url'],expansions=['attachments.media_keys'])


def getTweets(maxResults=10):

    query = "SMS truffa -isRetweet"
    response = client.search_recent_tweets(query=query, max_results=maxResults, tweet_fields=['created_at', 'lang', 'context_annotations', 'entities', 'public_metrics', 'attachments'])
    return response
def dFtoJSON(file_name: str, df):
    df.to_json(file_name, orient='records', lines=True, force_ascii=True)


# columns = ['Time', 'Tweet', 'Lang']
# data = []
# response = getTweets()
# for tweet in response.data:
#     data.append([str(tweet.created_at)[:10], str(tweet.text), tweet.lang])#tweet.entities['mentions']  if 'mentions' in tweet.entities else "--"])
#     #print(tweet.text)
# df = pd.DataFrame(data,columns=columns)



#dFtoJSON('tweets.json', df""" )
#print(df)
"""
risposta = client.search_recent_tweets("SMS Truffa")
with open('tweets.txt', 'a+') as fh:
    for r in risposta.data:
        print(r.text)
        fh.write(r.text) """

print(r.includes['media'])