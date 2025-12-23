#!/bin/bash
set -e

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

# Crear el directorio que Vercel espera SIEMPRE
rm -rf public
mkdir -p public

# NO hagas reflex init en CI (puede modificar cosas y fallar)
# reflex init

# Export estático
reflex export --frontend-only

# Caso 1: Reflex genera frontend.zip (tu caso anterior)
if [ -f "frontend.zip" ]; then
  unzip -o frontend.zip -d public
  rm -f frontend.zip
  echo "Export OK: frontend.zip -> public/"
  deactivate
  exit 0
fi

# Caso 2: Reflex genera una carpeta estática en vez de zip (según versión)
# Intentamos detectar salidas comunes
if [ -d ".web/_static" ]; then
  cp -r .web/_static/* public/
  echo "Export OK: .web/_static -> public/"
elif [ -d "web/_static" ]; then
  cp -r web/_static/* public/
  echo "Export OK: web/_static -> public/"
elif [ -d "out" ]; then
  cp -r out/* public/
  echo "Export OK: out -> public/"
elif [ -d "frontend/out" ]; then
  cp -r frontend/out/* public/
  echo "Export OK: frontend/out -> public/"
else
  echo "ERROR: Reflex export no generó frontend.zip ni una carpeta de salida conocida."
  echo "Lista de archivos actuales:"
  ls -la
  echo "Lista de carpetas:"
  find . -maxdepth 2 -type d
  exit 1
fi

deactivate
