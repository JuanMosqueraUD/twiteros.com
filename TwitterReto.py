#Primero instalar Tweepy:
#pip install tweepy

import tweepy
import pandas as pd
import json

def getKeys():
    APIKey="K1KFRre4gcNHbSDuzjyjbYpkn"
    APISecret="a3WIfFaKKT6KutRyGNAKOmWPCKfhkCjlbAfeaY2H4znC2oLHn0"
    accessToken="1075143372455727104-mpC9UBQ6C3rYvCiqKgzlkJJmGY0KQd"
    accessTokenSecret="JGksz8hPWyq7X7MRYzz4bVjY3Ggx0k8mq85JVLAY6ezRo"
    #bearerToken="AAAAAAAAAAAAAAAAAAAAAEneqgEAAAAAh1fYx4U38oXmstXpvWVNX9Ov4iY%3DEXix8mmOriaXshZsApRMRZk34QL9eeagpzJesOzeL0RXolBmmR"

    return APIKey,APISecret,accessToken,accessTokenSecret

def conexion(APIKey,APISecret,accessToken,accessTokenSecret):

    auth = tweepy.OAuthHandler(APIKey, APISecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api= tweepy.API(auth, wait_on_rate_limit=True) #pa k no se nos piffee el programa cuando ya no tengamos para obtener más data
    return api


api=conexion(*getKeys())

#client = tweepy.Client('AAAAAAAAAAAAAAAAAAAAAEneqgEAAAAAh1fYx4U38oXmstXpvWVNX9Ov4iY%3DEXix8mmOriaXshZsApRMRZk34QL9eeagpzJesOzeL0RXolBmmR')
data=api.get_user(screen_name="GustavoBolivar")
#data=api.get_user(screen_name="Daniel29468195")
print (json.dumps(data._json,indent=2))

