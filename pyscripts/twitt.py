#!python3
import pandas as pd
import ApiKeys.apiKey as k
import tweepy
import pytesseract
import cv2
import urllib.request
import numpy as np
import requests

#number of maxResults from the query (min:10 - max:100)
MAX_RESULTS = 15
ORGANIZATIONS = ['UNICREDIT', 'POSTEID', 'POSTEINFO', 'AMAZON']
#DATAFRAME PRINTING OPTION 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def extract_data(maxResults: int=10) -> pd.DataFrame: 

    client = tweepy.Client(bearer_token=k.BEARER_TOKEN)
    #query = 'sms truffa -is:retweet has:media'
    query = 'SMS truffa -retweet'

    #results of the query
    results = client.search_recent_tweets(query=query,  tweet_fields=['geo', 'created_at', 'attachments', 'id', 'entities'], 
                                media_fields=['preview_image_url', 'url'],expansions=['attachments.media_keys', 'author_id'], max_results=maxResults)
    #data list with | tweetID | tweetComment | tweetCreationTime | imgUrl | imgText |
    data = []

    #build the set of media_key -> url in order to use it later for a faster research
    imgUrls = {u['media_key']: u.url for u in results.includes['media'] if u.type == 'photo'}
    users = {u['id']: u for u in results.includes['users']}

    #iterate for all the tweets in results
    for i,tweet in enumerate(results.data):
        inserted = False
        #set organization variable to none
        org = ""
        #if tweet has media and url is in the set (if is a photo beacause sometimes could be a video, GIF ecc...)
        if(tweet.attachments and tweet.attachments['media_keys'][0] in imgUrls):
            #retrieve media_key
            media_key = tweet.attachments['media_keys']
            #=========retrieve url from imgUrl set with the media_key=====
            url = imgUrls[media_key[0]]
            url_response = urllib.request.urlopen(url)
            img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
            img = cv2.imdecode(img_array, -1)
            text = pytesseract.image_to_string(img)
            """ CHECK IF AN ORGANIZATION IS PRESENT IN THE TWEET """
            for keyword in ORGANIZATIONS:
                if(keyword in text.upper()):
                    org = keyword
                    #print(org)
                    break
            #print(f"####TESTO IMG TWEET {i}####\n{text}\n")
            data.append([tweet.id, tweet['text'], users[tweet.author_id].username , tweet.data['created_at'][:-14], url, text, org])
            #Set inserted as true so the tweet will not be inserted 2 times 
            inserted=True
        #if the tweet was not inserted before 
        if not inserted:
            data.append([tweet.id, tweet['text'], users[tweet.author_id].username ,tweet.data['created_at'][:-14], '', '', org])

    #build the dataframe
    df = pd.DataFrame(data, columns=['ID', 'Comment', 'Nickname' ,'Creation', 'ImageUrl', 'ImageText', 'Organization'])
    return df

if __name__ == '__main__':
    print(extract_data())
