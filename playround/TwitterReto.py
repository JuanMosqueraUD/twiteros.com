#Primero instalar Tweepy:
#pip install tweepy

import tweepy
import pandas as pd
from sklearn import tree
import json

from playround.models import Candidato
from .models import Candidato

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

def dataCandidatos():
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
    return candidatos

def mediaColumnas(candidatos):
    mediaSeguidores=round(candidatos["Seguidores"].mean(), 2)
    mediaFavoritos=round(candidatos["Favoritos"].mean(), 2)
    mediaListas=round(candidatos["N°Listas"].mean(), 2)
    return mediaSeguidores, mediaFavoritos, mediaListas

def porcentajes(candidatos):
    candidatos['Porcentaje de seguidores'] = round(candidatos['Seguidores'] / candidatos['Seguidores'].sum() * 100, 2)
    candidatos['Porcentaje de favoritos'] = round(candidatos['Favoritos'] / candidatos['Favoritos'].sum() * 100, 2)
    candidatos['Porcentaje de listas'] = round(candidatos['N°Listas'] / candidatos['N°Listas'].sum() * 100, 2)
    return candidatos

def abrirCandidatos():
    candidatos=pd.read_csv("candidatos2019.csv")
    return candidatos

def arbolDecision(candidatos, candidatos2022):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(candidatos.iloc[:,0:3], candidatos.iloc[:,3:4])

    for nombre, resultado in zip(candidatos2022.index, clf.predict(candidatos2022)):
        print(nombre, ":", resultado)


#print("RESULTADO DE DECISION TREE CLASSIFIER:\n")
#arbolDecision(abrirCandidatos(),dataCandidatos())


"""
#LA SIGUIENTE FUNCIÓN ES TEMPORAL PARA GUARDAR ALGO
api=conexion(*getKeys())
# INFORMACIÓN ALCANDÍAS AÑO 2019

#alcaldía de bogotá

dataBogota=[api.get_user(screen_name="ClaudiaLopez"),api.get_user(screen_name="CarlosFGalan"),api.get_user(screen_name="HOLLMANMORRIS"),api.get_user(screen_name="MiguelUribeT")]

claudiaLopez=[dataBogota[0].followers_count, dataBogota[0].favourites_count, dataBogota[0].listed_count, "GANADOR"]
carlosGalan=[dataBogota[1].followers_count, dataBogota[1].favourites_count, dataBogota[1].listed_count, "NO GANADOR"]
hollmanMorris=[dataBogota[2].followers_count, dataBogota[2].favourites_count, dataBogota[2].listed_count, "NO GANADOR"]
miguelUribe=[dataBogota[3].followers_count, dataBogota[3].favourites_count, dataBogota[3].listed_count, "NO GANADOR"]

#alcaldía de medellín

dataMedallo=[api.get_user(screen_name="QuinteroCalle"),api.get_user(screen_name="AlfredoRamosM"),api.get_user(screen_name="JDValde"),api.get_user(screen_name="BeatrizRave"),api.get_user(screen_name="VictorJCorreaV"),api.get_user(screen_name="jcvelezuribe")]

danielQuintero=[dataMedallo[0].followers_count, dataMedallo[0].favourites_count, dataMedallo[0].listed_count, "GANADOR"]
alfredoRamos=[dataMedallo[1].followers_count, dataMedallo[1].favourites_count, dataMedallo[1].listed_count, "NO GANADOR"]
juanDavidValderrama=[dataMedallo[2].followers_count, dataMedallo[2].favourites_count, dataMedallo[2].listed_count, "NO GANADOR"]
beatrizRave=[dataMedallo[3].followers_count, dataMedallo[3].favourites_count, dataMedallo[3].listed_count, "NO GANADOR"]
victorCorrea=[dataMedallo[4].followers_count, dataMedallo[4].favourites_count, dataMedallo[4].listed_count, "NO GANADOR"]
juanCarlosVelez=[dataMedallo[5].followers_count, dataMedallo[5].favourites_count, dataMedallo[5].listed_count, "NO GANADOR"]

#alcaldía de cali

dataCali=[api.get_user(screen_name="JorgeIvanOspina"),api.get_user(screen_name="robertoortizu"),api.get_user(screen_name="DanisRenteria"), api.get_user(screen_name="alejoeder")]

jorgeOspina=[dataCali[0].followers_count, dataCali[0].favourites_count, dataCali[0].listed_count, "GANADOR"]
robertoOrtiz=[dataCali[1].followers_count, dataCali[1].favourites_count, dataCali[1].listed_count, "NO GANADOR"]
danisRenteria=[dataCali[2].followers_count, dataCali[2].favourites_count, dataCali[2].listed_count, "NO GANADOR"]
alejandroEder=[dataCali[3].followers_count, dataCali[3].favourites_count, dataCali[3].listed_count, "NO GANADOR"]

#alcaldía de barranquilla

dataBarranquilla=[api.get_user(screen_name="jaimepumarejo"),api.get_user(screen_name="AntonioBohrquez"),api.get_user(screen_name="diogenesroserod")]

jaimePumarejo=[dataBarranquilla[0].followers_count, dataBarranquilla[0].favourites_count, dataBarranquilla[0].listed_count, "GANADOR"]
antonioBohorquez=[dataBarranquilla[1].followers_count, dataBarranquilla[1].favourites_count, dataBarranquilla[1].listed_count, "NO GANADOR"]
diogenesRosero=[dataBarranquilla[2].followers_count, dataBarranquilla[2].favourites_count, dataBarranquilla[2].listed_count, "NO GANADOR"]

#alcaldía de cartagena

dataCtg=[api.get_user(screen_name="daulaw"),api.get_user(screen_name="williamgarciatd"),api.get_user(screen_name="yolandawongb"),api.get_user(screen_name="FerAraujoP_")]

williamDau=[dataCtg[0].followers_count, dataCtg[0].favourites_count, dataCtg[0].listed_count, "GANADOR"]
williamGarcia=[dataCtg[1].followers_count, dataCtg[1].favourites_count, dataCtg[1].listed_count, "NO GANADOR"]
yolandaWong=[dataCtg[2].followers_count, dataCtg[2].favourites_count, dataCtg[2].listed_count, "NO GANADOR"]
fernandoAraujo=[dataCtg[3].followers_count, dataCtg[3].favourites_count, dataCtg[3].listed_count, "NO GANADOR"]


candidatos2019=pd.DataFrame([claudiaLopez,carlosGalan,hollmanMorris,miguelUribe,danielQuintero,alfredoRamos,juanDavidValderrama,beatrizRave,juanCarlosVelez,jorgeOspina,robertoOrtiz,danisRenteria,alejandroEder, jaimePumarejo,antonioBohorquez,diogenesRosero, williamDau,williamGarcia, yolandaWong,fernandoAraujo],columns=["Seguidores","Favoritos","N°Listas","Resultado"])
print(candidatos2019)

candidatos2019.to_csv('candidatos2019.csv', index=False)
"""

def crear_candidatos_desde_dataframe():
    df = dataCandidatos()
    for index, row in df.iterrows():
        Candidato.objects.create(
            nombre=index,
            seguidores=row['Seguidores'],
            favoritos=row['Favoritos'],
            numero_listas=row['N°Listas']
        )
