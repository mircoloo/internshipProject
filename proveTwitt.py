#!python3

from xml.etree.ElementInclude import include
import tweepy
import Prove.pyScripts.ApiKeys.apiKey as k

#https://twitter.com/consumatorirt/status/

query = 'covid lang:it has:images'    #from:____   #has:_____
client = tweepy.Client(bearer_token=k.BEARER_TOKEN, consumer_key=k.API_KEY, consumer_secret=k.API_SECRET_KEY, access_token=k.ACCESS_TOKEN, access_token_secret=k.ACCESS_SECRET_TOKEN)
response = client.search_recent_tweets(query=query, tweet_fields=['geo', 'created_at', 'attachments', 'id', 'author_id', 'lang', 'public_metrics','source'],  media_fields=['preview_image_url', 'media_key', 'url'],expansions=['attachments.media_keys', 'geo.place_id', 'author_id'], max_results=10, user_fields=['profile_image_url'])
#response = client.get_tweet(id='1506556446279970816', tweet_fields=['geo', 'created_at', 'attachments', 'id', 'author_id', 'lang', 'public_metrics','source'],  media_fields=['preview_image_url', 'media_key', 'url'],expansions=['attachments.media_keys'],user_fields=['profile_image_url'])

 
#imgs = {u['url']: u for u in response.includes['media']}

for i, img in enumerate(response.includes['media']):
    #print(i, img.url)
    #print(response.includes['media'])
    pass
for tweet in response:
    print(tweet)

#print(imgs)

