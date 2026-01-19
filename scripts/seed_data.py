"""
Seed data script to populate database with initial sprints and tasks.
"""

import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.sprint import Sprint
from app.models.task import Task
from app.models.base import Base

def seed_data():
    db = SessionLocal()
    try:
        print("Creating seed data...")
        
        # Check if data already exists
        if db.query(Sprint).count() > 0:
            print("Data already exists. Skipping seed.")
            return

        # Create Sprints
        sprint1 = Sprint(
            number=1,
            name="Fundamentos y Modelado de Datos",
            description="Introducción a Salesforce, configuración de org, y creación de objetos y campos.",
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=7),
            is_active=True
        )
        
        sprint2 = Sprint(
            number=2,
            name="Seguridad y Automatización Básica",
            description="Modelos de seguridad, sharing rules, y automatización con flujos.",
            start_date=datetime.now() + timedelta(days=8),
            end_date=datetime.now() + timedelta(days=14),
            is_active=False
        )
        
        db.add(sprint1)
        db.add(sprint2)
        db.commit()
        
        print("Sprints created.")
        
        # Create Tasks for Sprint 1
        tasks_sprint1 = [
            Task(
                sprint_id=sprint1.id,
                category="Clase",
                title="Clase 1: Introducción al Ecosistema Salesforce",
                description="Visión general de la plataforma, ediciones, y navegación.",
                markdown_path="curriculum/sprint1/clase1.md",
                order_index=1
            ),
            Task(
                sprint_id=sprint1.id,
                category="Practica",
                title="Práctica 1: Configuración de tu Org",
                description="Pasos para configurar tu Developer Edition.",
                markdown_path="curriculum/sprint1/practica1.md",
                order_index=2
            ),
            Task(
                sprint_id=sprint1.id,
                category="Superbadge",
                title="Superbadge: Security Specialist",
                description="Desafío práctico de seguridad.",
                markdown_path="curriculum/sprint1/superbadge_security.md",
                order_index=3
            )
        ]
        
        for task in tasks_sprint1:
            db.add(task)
            
        db.commit()
        print(f"Created {len(tasks_sprint1)} tasks for Sprint 1.")
        
        print("✅ Database seeded successfully!")
        
    except Exception as e:
        print(f"❌ Error creating seed data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
