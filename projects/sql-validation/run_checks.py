"""Run the SQLite data-validation example without external dependencies."""
from pathlib import Path
import sqlite3

HERE = Path(__file__).parent


def main():
    connection = sqlite3.connect(":memory:")
    connection.executescript((HERE / "schema_and_seed.sql").read_text())
    sql = (HERE / "checks.sql").read_text()
    for i, statement in enumerate(sql.split(";"), start=1):
        if not statement.strip() or not any(line.strip() and not line.strip().startswith("--") for line in statement.splitlines()):
            continue
        cursor = connection.execute(statement)
        print(f"CHECK {i}: {', '.join(column[0] for column in cursor.description)}")
        for row in cursor.fetchall():
            print("  " + " | ".join(map(str, row)))
    connection.close()


if __name__ == "__main__":
    main()
