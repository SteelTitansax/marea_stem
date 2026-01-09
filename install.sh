#!/bin/bash

# ===============================================
# Script para crear entorno STEM Python 3.11
# ===============================================

# 1️⃣ Comprobar Python 3.11
echo "🔹 Verificando si Python 3.11 está instalado..."
if ! python3.11 --version &>/dev/null; then
    echo "❌ Python 3.11 no encontrado. Instala Python 3.11 primero."
    exit 1
else
    echo "✅ Python 3.11 encontrado: $(python3.11 --version)"
fi

# 2️⃣ Crear entorno virtual
ENV_DIR="$HOME/venv_stem311"
echo "🔹 Creando entorno virtual en $ENV_DIR..."
python3.11 -m venv "$ENV_DIR"

# 3️⃣ Activar entorno
echo "🔹 Activando entorno virtual..."
source "$ENV_DIR/bin/activate"

# 4️⃣ Actualizar pip
echo "🔹 Actualizando pip..."
pip install --upgrade pip

# 5️⃣ Instalar paquetes compatibles
echo "🔹 Instalando paquetes STEM..."
pip install -r requirements.txt

echo "🎉 Entorno STEM listo en $ENV_DIR"
echo "Para activarlo: source $ENV_DIR/bin/activate"
