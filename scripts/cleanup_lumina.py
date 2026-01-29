import sys
import os

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.lumina import LuminaDeliverable


def clean_garbage_data():
    db = SessionLocal()
    try:
        print("🧹 Iniciando limpieza profunda de datos basura en Lumina...")

        # 1. Identificar registros basura (los que empiezan con digitos como '00-', '01-', etc, o contienen '.md')
        # Nuestros registros validos empiezan con emojis o "DÍA"

        garbage_query = db.query(LuminaDeliverable).filter(
            (LuminaDeliverable.title.op("~")("^[0-9]+-"))
            | (  # Empieza con numeros y guion
                LuminaDeliverable.reference.like("%/Gestor_de_Versiones/%")
            )
            | (  # Contiene rutas de archivo antiguas
                LuminaDeliverable.reference.like("%.md")
            )  # Es un archivo markdown literal
        )

        count = garbage_query.count()

        if count > 0:
            print(f"⚠️ Se encontraron {count} registros basura. Eliminando...")
            for item in garbage_query.all():
                print(f"   ❌ Eliminando: {item.title} ({item.reference})")
                db.delete(item)

            db.commit()
            print("✨ Limpieza completada. La basura ha sido sacada.")
        else:
            print("✅ No se encontró basura. La base de datos está limpia.")

    except Exception as e:
        print(f"❌ Error durante la limpieza: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    clean_garbage_data()
