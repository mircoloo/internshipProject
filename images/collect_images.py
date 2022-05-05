#!python3
import tweepy
import numpy as np
import sys
import requests
#from ...internshipProject.pyscripts.ApiKeys import apiKey as k

 
#BEARER_TOKEN = k.BEARER_TOKEN
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGRQZwEAAAAAMnK1TY6ZC94273gk7RKpChaOgvs%3DhZpnlRaLB7Qa74sfoeCc3R8Pn47PDoQt6dgxk9YKUMxhPiUgeR"
MAX_RESULTS = 100

client = tweepy.Client(bearer_token=BEARER_TOKEN)
    #query = 'sms truffa -is:retweet has:media'
query = 'SMS truffa -retweet'

    #results of the query
results = client.search_recent_tweets(query=query,  tweet_fields=['geo', 'created_at', 'attachments', 'id', 'entities'], 
                                media_fields=['preview_image_url', 'url'],expansions=['attachments.media_keys', 'author_id'], max_results=MAX_RESULTS)

urls = {u.url for u in results.includes['media'] if u.type == 'photo'}


for i,url in enumerate(urls):
        req = requests.get(url)
        file = open(f"images/sample_image{i}.png", "wb")
        file.write(req.content)
        file.close()
