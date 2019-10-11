import requests
from bs4 import BeautifulSoup as bs
import os

# Recurso de imágenes de modelos
url = 'URL TARGET PARA RECOLECTAR IMÁGENES'

# Descargar URL para el análisis
pagina = requests.get(url)
soup = bs(pagina.text, 'html.parser')

# Localizar los elementos con las etiquetas de las imágenes
image_tags = soup.findAll('img')

# Crear un directorio para las imágenes
if not os.path.exists('modelos'):
	os.makedirs('modelos')

# Moverlas al directorio nuevo
os.chdir('modelos')

# Variable contador para escribir enumeración de imágenes
num_img = 0

# Escribir las imágenes
for src in image_tags:
	try:
		url = src['data-large-src']
		fuente = requests.get(url)
		if fuente.status_code == 200:
			with open('model-' + str(num_img) + '.jpg', 'wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x += 1
	except:
		pass