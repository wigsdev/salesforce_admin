"""
Create a test user in local database
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password


def create_test_user():
    print("\n" + "=" * 80)
    print("👤 CREANDO USUARIO DE PRUEBA LOCAL")
    print("=" * 80 + "\n")

    db = SessionLocal()

    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == "admin@local.com").first()

        if existing_user:
            print("⚠️  Usuario ya existe:")
            print(f"   Email: {existing_user.email}")
            print(f"   Nombre: {existing_user.name}\n")
            print("💡 Puedes usar este usuario para login.")
        else:
            # Create new user
            user = User(
                name="Admin Local",
                email="admin@local.com",
                hashed_password=hash_password("admin123"),
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            print("✅ Usuario creado exitosamente!\n")
            print("📝 Credenciales:")
            print("   Email:    admin@local.com")
            print("   Password: admin123")
            print(f"   Nombre:   {user.name}")
            print(f"   ID:       {user.id}\n")

        print("=" * 80)
        print("🎯 Ahora puedes hacer login en: http://localhost:8000/login")
        print("=" * 80 + "\n")

    except Exception as e:
        print(f"❌ Error creando usuario: {e}\n")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    create_test_user()
