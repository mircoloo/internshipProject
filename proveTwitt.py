#!python3
import tweepy
import Prove.pyScripts.ApiKeys.apiKey as k

#https://twitter.com/consumatorirt/status/

query = 'SMS truffa'    #from:____   #has:_____
client = tweepy.Client(bearer_token=k.BEARER_TOKEN, consumer_key=k.API_KEY, consumer_secret=k.API_SECRET_KEY, access_token=k.ACCESS_TOKEN, access_token_secret=k.ACCESS_SECRET_TOKEN)
response = client.search_recent_tweets(max_results=10, query=query, tweet_fields= ['created_at', 'attachments', 'id', 'public_metrics'],  media_fields=['url'],expansions=['attachments.media_keys'])
#response = client.get_tweet(id='1506556446279970816', tweet_fields=['entities','geo', 'created_at', 'attachments', 'id', 'author_id', 'lang', 'public_metrics','source', 'possibly_sensitive'],  media_fields=['preview_image_url', 'media_key', 'url'],expansions=['attachments.media_keys', 'geo.place_id', 'author_id'], user_fields=['profile_image_url'])

 
#imgs = {u['url']: u for u in response.includes['media']}



for i, tweet in enumerate(response.data):
    print(i, tweet.id)
    if(tweet.attachments):
        media_key = tweet.attachments['media_keys']
        for el in response.includes['media']:
            if media_key[0] == el.media_key and el.type == 'photo':
                print(i, el.url)




