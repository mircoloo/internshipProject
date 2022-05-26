#!python3
from time import sleep
import pandas as pd
import tweepy
import pytesseract
import cv2
import urllib.request
import numpy as np
import requests
import re
import spacy
import os
from dotenv import load_dotenv
load_dotenv()

nlp = spacy.load('it_core_news_lg')

#number of maxResults from the query (min:10 - max:100)
MAX_RESULTS = 15
ORGANIZATIONS = ['UNICREDIT', 'POSTEID','POSTEINFO', 'AMAZON']
#DATAFRAME PRINTING OPTION 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def extract_data(maxResults: int=10) -> pd.DataFrame: 
    client = tweepy.Client(bearer_token=os.environ["BEARER_TOKEN"])
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
        #set link to none
        link = "" 

        text = tweet.text
        doc = nlp(text)
        # Find entities
        for entity in doc.ents:
            if(entity.label_ == 'ORG'):
                org += f" {entity}"






        #if tweet has media and url is in the set (if is a photo beacause sometimes could be a video, GIF ecc...)
        if(tweet.attachments and tweet.attachments['media_keys'][0] in imgUrls):
            #retrieve media_key
            media_key = tweet.attachments['media_keys']
            #=========retrieve url from imgUrl set with the media_key=====
            url = imgUrls[media_key[0]]
            url_response = urllib.request.urlopen(url)
            img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
            img = cv2.imdecode(img_array, -1)
            img = cv2.resize(img, (0, 0), fx=2, fy=2)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))
            text = pytesseract.image_to_string(msk)
            domain_re = r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))'
            domain_match = re.search(domain_re, text.replace('\n', ''))
            if(domain_match):
                #print(tweet.id, domain_match.group(1))
                link = domain_match.group(1)
            """ CHECK IF AN ORGANIZATION IS PRESENT IN THE TWEET """
            for keyword in ORGANIZATIONS:
                if(keyword in text.upper()):
                    org = keyword
                    #print(org)
                    break
            doc = nlp(text)
            for entity in doc.ents:
                if(entity.label_ == 'ORG'):
                    #print(entity)
                    org += f" {entity}"




            #print(f"####TESTO IMG TWEET {i}####\n{text}\n")
            data.append([tweet.id, tweet['text'], users[tweet.author_id].username , tweet.data['created_at'][:-14], url, text, org, link])
            #Set inserted as true so the tweet will not be inserted 2 times 
            inserted=True
        #if the tweet was not inserted before 
        if not inserted:
            data.append([tweet.id, tweet['text'], users[tweet.author_id].username ,tweet.data['created_at'][:-14], '', '', org, link])

    #build the dataframe
    df = pd.DataFrame(data, columns=['ID', 'Comment', 'Nickname' ,'Creation', 'ImageUrl', 'ImageText', 'Organization', 'Link'])
    return df

if __name__ == '__main__':
    print(extract_data(100))
