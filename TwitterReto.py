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

data=[api.get_user(screen_name="GustavoBolivar"),api.get_user(screen_name="CarlosFGalan"),api.get_user(screen_name="Diego_Molano"),api.get_user(screen_name="JERobledo"),api.get_user(screen_name="ElGeneralVargas"),api.get_user(screen_name="JDOviedoA"),api.get_user(screen_name="Rodrigo_Lara_")]

gustavoBolivar=[data[0].followers_count, data[0].favourites_count, data[0].listed_count]
carlosGalan=[data[1].followers_count, data[1].favourites_count, data[1].listed_count]
diegoMolano=[data[2].followers_count, data[2].favourites_count, data[2].listed_count]
jorgeRobledo=[data[3].followers_count, data[3].favourites_count, data[3].listed_count]
generalVargas=[data[4].followers_count, data[4].favourites_count, data[4].listed_count]
juanOviedo=[data[5].followers_count, data[5].favourites_count, data[5].listed_count]
rodrigoLara=[data[6].followers_count, data[6].favourites_count, data[6].listed_count]

candidatos=pd.DataFrame([gustavoBolivar,carlosGalan,diegoMolano,jorgeRobledo,generalVargas,juanOviedo,rodrigoLara],columns=["Seguidores","Favoritos","N°Listas"],index=["Gustavo Bolivar","Carlos Galan","Diego Molano","Jorge Robledo","Jorge Luis Vargas","Juan Oviedo","Rodrigo Lara"])
print(candidatos)
