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

## 7. Consumir una API de IA generativa
`curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": Porque el cielo es azul?",
  "stream": false
}'`

## Respaldar el README
- ` git add .` cualquier archivo lo guarda
- `git commit -m "UPDATE README` actualiza los cambios que hagamos hecho 
- ` git push -u origin main` sube el codigo de nuestra maquina a github