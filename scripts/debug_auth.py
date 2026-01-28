import sys
import os
from dotenv import load_dotenv

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

url = os.getenv("DATABASE_URL")
print(f"DEBUG: DATABASE_URL is set: {bool(url)}")
if url:
    # Print protocol and host, mask password
    try:
        from sqlalchemy.engine.url import make_url

        u = make_url(url)
        print(f"DEBUG: Drivername: {u.drivername}")
        print(f"DEBUG: Host: {u.host}")
        print(f"DEBUG: Port: {u.port}")
        print(f"DEBUG: Database: {u.database}")
    except Exception as e:
        print(f"DEBUG: Could not parse URL: {e}")


print("Testing DB connection with timeout...")
try:
    # Try a quick engine directly
    from sqlalchemy import create_engine

    # Use valid replacement logic from app/database.py
    if url and url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)

    eng = create_engine(url, connect_args={"connect_timeout": 5})
    with eng.connect() as conn:
        print("✅ DB Connection successful")
except Exception as e:
    print(f"❌ DB Connection failed: {e}")
