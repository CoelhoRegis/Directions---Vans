import googlemaps
from datetime import datetime

#Chave API

gmaps = googlemaps.Client(key='AIzaSyDEa44LAccTgGkomlcn7E8fXlqY4byBKBc')

#Requisicao de rota a partir de dois pontos, levando em conta o transito

now = datetime.now() #Data e Hora local, parametro da requisicao

directions_result = gmaps.directions("PUC Minas Coracao Eucaristico", "Estacao Gameleira",
mode = "transit",
departure_time = now
) #Retona uma lista com os paramentros gerados pela API

with open("Results.txt","w") as f: #Escrita em arquivo para tratamento
  for item in directions_result:
    f.write("%s\n" % item)

#Print para debug, afim de determinar se as informacoes foram obtidas

print (directions_result)