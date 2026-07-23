import os
import psycopg
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():

    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        return "DATABASE_URL Not Found"

    try:
        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:

                cur.execute("SELECT current_database();")
                db_name = cur.fetchone()[0]

                cur.execute("SELECT version();")
                version = cur.fetchone()[0]

        return f"""
        <h2>Render PostgreSQL 測試成功</h2>

        <p><b>Database：</b>{db_name}</p>

        <p><b>Version：</b>{version}</p>
        """

    except Exception as e:
        return f"<pre>{e}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)