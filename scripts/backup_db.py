import os
import subprocess
import sys
from datetime import datetime
from urllib.parse import urlparse

# Add parent directory to path to import app config if needed,
# but here we prefer standalone execution relying on env vars.
# We will use python-dotenv to load .env if available.

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not installed. Relying on system env vars.")


def backup_database():
    """
    Creates a backup of the PostgreSQL database defined in DATABASE_URL.
    Uses pg_dump.
    """
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        print("Error: DATABASE_URL environment variable not set.")
        sys.exit(1)

    # Parse connection details
    try:
        url = urlparse(database_url)
        username = url.username
        password = url.password
        hostname = url.hostname
        port = url.port or 5432
        database = url.path[1:]  # Remove leading /
    except Exception as e:
        print(f"Error parsing DATABASE_URL: {e}")
        sys.exit(1)

    # Create backups directory if not exists
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"backup_salesforce_admin_{timestamp}.sql"
    filepath = os.path.join(backup_dir, filename)

    print(f"Starting backup for database: {database} at {hostname}...")

    # Prepare environment for pg_dump (pass password safely)
    env = os.environ.copy()
    if password:
        env["PGPASSWORD"] = password

    # Construct command
    # pg_dump -h {host} -p {port} -U {user} -F p -f {file} {dbname}
    # -F p : Plain text SQL script (easier to read/debug/restore manually if needed)
    # -v : Verbose

    command = [
        "pg_dump",
        "-h",
        str(hostname),
        "-p",
        str(port),
        "-U",
        str(username),
        "-F",
        "p",
        "-v",
        "-f",
        filepath,
        database,
    ]

    try:
        # Run pg_dump
        subprocess.run(command, env=env, check=True)
        print(f"✅ Backup successful! Saved to: {filepath}")

        # Verify file creation and size
        if os.path.exists(filepath):
            size_bytes = os.path.getsize(filepath)
            size_mb = size_bytes / (1024 * 1024)
            print(f"   Size: {size_mb:.2f} MB")
        else:
            print("⚠️ Warning: Backup file not found after command execution.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Backup failed with exit code: {e.returncode}")
        print("Ensure 'pg_dump' is installed and valid credentials are provided.")
    except FileNotFoundError:
        print("❌ Error: 'pg_dump' command not found.")
        print("Please install PostgreSQL tools and ensure 'pg_dump' is in your PATH.")


if __name__ == "__main__":
    backup_database()
