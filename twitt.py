#!python3
import pandas as pd
import Prove.pyScripts.ApiKeys.apiKey as k
import tweepy


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



client = tweepy.Client(bearer_token=k.BEARER_TOKEN)
#query = 'sms truffa -is:retweet has:media'
query = 'SMS truffa'

#results of the query
results = client.search_recent_tweets(query=query,  tweet_fields=['geo', 'created_at', 'attachments', 'id', 'entities'], 
                            media_fields=['preview_image_url', 'url'],expansions=['attachments.media_keys'], max_results=15)

#iterate from all the tweet and retrieve information | twitter comment | tweet id | tweet image text | ... | time | image url 
data = []


for i,tweet in enumerate(results.data):
    inserted = False
    if(tweet.attachments):
        media_key = tweet.attachments['media_keys']
        for el in results.includes['media']:
            if media_key[0] == el.media_key and el.type == 'photo':
                data.append([tweet.id, tweet['text'], tweet.data['created_at'][:-14], el.url])
                inserted=True
    if not inserted:
        data.append([tweet.id, tweet['text'], tweet.data['created_at'][:-14], 'NI'])


df = pd.DataFrame(data, columns=['ID', 'Comment', 'Creation', 'ImageUrl'])
print(df)

