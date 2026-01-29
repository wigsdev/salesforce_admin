#!/usr/bin/env bash
set -o errexit

echo "🗄️ Ejecutando Migraciones de Base de Datos..."
alembic upgrade head

echo "🌱 Seed Data (Opcional)..."
python scripts/seed_data.py

echo "🚀 Iniciando Servidor Web..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT
