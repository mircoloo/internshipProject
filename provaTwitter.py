import tweepy
import pyScripts.ApiKeys.apiKey as k

client = tweepy.Client(bearer_token=k.BEARER_TOKEN)

query = "SMS truffa"

response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang', 'context_annotations', 'entities', 'public_metrics'])


for t in response.data:
    print(t.created_at)
    """ 
    print(t.public_metrics)
    print(t.entities, '\n') """
    try:
        print(t.entites['urls']['images'])
    except:
        print('not present')
        print(t.entities.keys())
    print(t.text,'\n')

