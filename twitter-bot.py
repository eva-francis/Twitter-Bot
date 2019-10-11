import tweepy as tp
import time
import os

# Credenciales para acceder a la API de Twitter
consumer_key = 'LLAVE DEL CONSUMIDOR'
consumer_secret = 'SECRETO DEL CONSUMIDOR'
access_token = 'ACCESO SIMBÓLICO'
access_secret = 'ACCESO SECRETO'

# Acceder a la cuenta de desarrollador
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# Iteración sobre las fotos en el directorio
os.chdir('modelos')
for img_modelo in os.listdir('.'):
	api.update_with_media(img_modelo)
	time.sleep(3)