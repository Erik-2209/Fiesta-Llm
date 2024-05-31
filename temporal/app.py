import requests
import json
import base64

# Ruta de la imagen
ruta_imagen = 'ruta/a/tu/imagen.jpg'

# Leer la imagen en modo binario
with open(ruta_imagen, 'rb') as imagen_file:
    # Convertir la imagen a base64
    imagen_base64 = base64.b64encode(imagen_file.read()).decode('utf-8')

# Imprimir el resultado en base64
print(imagen_base64)

url = 'http://localhost:11434/api/generate'
data = {
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": False
  }

response = requests.post(uri, json = data)

response = json.loads(response.text)

print(response['response'])