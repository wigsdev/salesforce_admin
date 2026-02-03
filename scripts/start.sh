#!/usr/bin/env bash
set -o errexit

echo "🗄️ Ejecutando Migraciones de Base de Datos..."
alembic upgrade head

echo "🧹 Limpiando Datos Basura (Legacy)..."
python scripts/cleanup_lumina.py

echo "🌱 Seed Data Lumina..."
python scripts/seed_data.py

echo "📚 Seed Curriculum (Sprints & Tasks)..."
python scripts/seed_curriculum.py

echo "🚀 Iniciando Servidor Web..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT
