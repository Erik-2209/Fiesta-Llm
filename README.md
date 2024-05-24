# Fiesta-Llm
## 1. Instalacion de ollama
`shell
curl -fsSL https://ollama.com/install.sh | sh`

## 2. Arrancar el servidor
`shell
ollama serve`

## 3. Descargar un modelo
`shell
ollama pull tinyllama`

## 4. Correr el modelo tinyllama
`shell
ollama run tinyllama` y escribir lo que queremos saber.
 
## 5. entrar en modo chat
`shell
ollama run tinyllama` y enter.

## 6. detener el modelo
`shell
ctrl+D`

## 7. consumir una API de IA generativa
`curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": Porque el cielo es azul?",
  "stream": false
}'`