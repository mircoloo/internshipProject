#!python3
import pandas as pd
import Prove.pyScripts.ApiKeys.apiKey as k
import pandas as pd
import tweepy




"""    ######PROVE RETREIVING IMMAGINI######

#id -> tweet.data['id']
#created at -> tweet.data['created']

client = tweepy.Client(bearer_token=k.BEARER_TOKEN)

#tweet = client.get_tweet(id='1503723497356509188',tweet_fields=['context_annotations', 'created_at', 'attachments', 'id'], 
                            # media_fields=['preview_image_url'],expansions=['attachments.media_keys'])


tweet = client.get_tweet(id='1505547745578336261',tweet_fields=['context_annotations', 'created_at', 'attachments', 'id'],  media_fields=['preview_image_url'],expansions=['attachments.media_keys'])

# attachments = tweet.data['attachments']
# media_keys = attachments['media_keys']
# print(media.text)
# if media[media_keys[0]].preview_image_url:
#     print(media[media_keys[0]].preview_image_url)

query = 'sms truffa -is:retweet has:media'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],  media_fields=['preview_image_url'], expansions='attachments.media_keys',max_results=100)

# Get list of media from the includes object
media = {m["media_key"]: m for m in tweets.includes['media']}


#print(media)

for tweet in tweets.data:
    attachments = tweet.data['attachments']
    media_keys = attachments['media_keys']
    #if media[media_keys[0]].preview_image_url:
    print(tweet.data['id'], media_keys ,media[media_keys[0]].preview_image_url)


"""

ids = []
comments = []
creationTimes = []

client = tweepy.Client(bearer_token=k.BEARER_TOKEN)
#query = 'sms truffa -is:retweet has:media'
query = 'SMS truffa '

#results of the query
results = client.search_recent_tweets(query=query,  tweet_fields=['geo', 'created_at', 'attachments', 'id'], 
                            media_fields=['preview_image_url'],expansions=['attachments.media_keys'])

#iterate from all the tweet and retrieve information | twitter comment | tweet id | tweet image text | ... | time | image url 
data = []
for tweet in results.data:
    print(tweet.text, '\n')
    #print(tweet['geo'])
    #print(tweet.data['context_annotations'])
    #data.append([tweet.id, tweet['text'], tweet.data['created_at'][:-14]])


#df = pd.DataFrame(data, columns=['ID', 'Comment', 'Creation'])

#print(df)

