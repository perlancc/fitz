# main.py
import os
import sys
import subprocess
from pathlib import Path


def run_psql_file(psql_path: str, db_url: str, sql_file: Path) -> None:
    if not sql_file.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_file}")

    # ON_ERROR_STOP=1 makes psql stop on the first error (critical for migrations)
    cmd = [
        psql_path,
        db_url,
        "-v", "ON_ERROR_STOP=1",
        "-f", str(sql_file),
    ]

    print(f"\n==> Running: {sql_file}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("\n❌ ERROR while running:", sql_file)
        if result.stdout.strip():
            print("\n--- STDOUT ---\n", result.stdout)
        if result.stderr.strip():
            print("\n--- STDERR ---\n", result.stderr)
        sys.exit(result.returncode)

    # psql writes a lot of useful info to stdout
    if result.stdout.strip():
        print(result.stdout)

    print(f"✅ Done: {sql_file}")


def main() -> None:
    # Repo root assumed to be where main.py is located
    repo_root = Path(__file__).resolve().parent

    schema_file = repo_root / "db" / "01_schema.sql"
    seed_file = repo_root / "db" / "02_seed.sql"

    # Use a single DATABASE_URL env var (recommended)
    # Example (local): postgresql://postgres:postgres@localhost:5432/fitz_local
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        print(
            "DATABASE_URL is not set.\n"
            "Set it like this (PowerShell):\n"
            '  $env:DATABASE_URL="postgresql://postgres:postgres@localhost:5432/fitz_local"\n'
            "Then run:\n"
            "  python main.py\n"
        )
        sys.exit(1)

    # If psql isn't in PATH, set this env var to the full path.
    # Example: C:\\Program Files\\PostgreSQL\\18\\bin\\psql.exe
    psql_path = os.environ.get("PSQL_PATH", "psql")

    # Run files in order
    run_psql_file(psql_path, db_url, schema_file)
    run_psql_file(psql_path, db_url, seed_file)

    print("\n🎉 All migrations applied successfully.")


if __name__ == "__main__":
    main()
