from sqlite3 import Cursor

import ApiKeys.apiKey as k
import tweepy

auth = tweepy.OAuthHandler(
    k.api_key, k.api_secret_key,   
)
auth.set_access_token(k.access_token,k.access_secret_token)
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("ok")
except:
    print("something wrong")
