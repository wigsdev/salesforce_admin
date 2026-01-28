#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Iniciando Build Process..."

echo "📦 Instalando dependencias Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🎨 Compilando TailwindCSS..."
npm install
npm run build:css

echo "🗄️ Ejecutando Migraciones (Alembic)..."
alembic upgrade head

echo "🌱 Seed Data (Opcional)..."
# python scripts/seed_data.py  <-- Descomentar si queremos seed automático

echo "✅ Build Completado Exitosamente."
