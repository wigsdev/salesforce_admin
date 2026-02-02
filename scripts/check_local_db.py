"""
Check local database connection and data
"""
from app.database import SessionLocal
from app.models.lumina import LuminaDeliverable, LuminaTask

def main():
    print("\n" + "="*80)
    print("🔍 VERIFICANDO BASE DE DATOS LOCAL")
    print("="*80 + "\n")
    
    try:
        db = SessionLocal()
        
        # Check days
        days = db.query(LuminaDeliverable).all()
        print(f"📅 {len(days)} días encontrados\n")
        
        total_tasks = 0
        tasks_with_path = 0
        
        for day in days:
            day_tasks_with_path = sum(1 for t in day.tasks if t.doc_path)
            total_tasks += len(day.tasks)
            tasks_with_path += day_tasks_with_path
            
            print(f"  {day.title}")
            print(f"    Tasks: {len(day.tasks)} ({day_tasks_with_path} con doc_path)")
        
        print(f"\n{'='*80}")
        print(f"RESUMEN: {tasks_with_path}/{total_tasks} tasks tienen doc_path")
        print(f"{'='*80}\n")
        
        if tasks_with_path == total_tasks:
            print("✅ PERFECTO: Todos los tasks tienen doc_path")
        elif tasks_with_path > 0:
            print(f"⚠️  PARCIAL: {total_tasks - tasks_with_path} tasks sin doc_path")
        else:
            print("❌ ERROR: Ningún task tiene doc_path")
        
        db.close()
        
    except Exception as e:
        print(f"❌ Error conectando a la base de datos:")
        print(f"   {e}\n")
        print("💡 Asegúrate de que:")
        print("   1. PostgreSQL está corriendo")
        print("   2. La base de datos existe")
        print("   3. Las migraciones están ejecutadas")
        print("   4. El archivo .env tiene DATABASE_URL correcto\n")

if __name__ == "__main__":
    main()
