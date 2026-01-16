#!/bin/bash

# Activar entorno virtual
ENV_DIR="$HOME/marea_stem/venv_stem311"
echo "🔹 Activando entorno virtual en $ENV_DIR ..."

source "$ENV_DIR/bin/activate"

echo " Arrancando Marea STEM ..."

python3 $HOME/marea_stem/chatbot.py

