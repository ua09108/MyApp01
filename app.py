from flask import Flask, render_template

from database.db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    """
    首頁：
    測試 Render PostgreSQL 連線，
    並將資料庫狀態傳給 index.html。
    """
    print("======= NEW VERSION =======")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT current_database();")
                db_name = cur.fetchone()[0]

                cur.execute("SELECT version();")
                db_version = cur.fetchone()[0]

                # 只保留前兩個字
                db_version = " ".join(db_version.split()[:2])

        return render_template(
            "index.html",
            db_status="Connected",
            db_name=db_name,
            db_version=db_version,
        )

    except Exception as error:
        app.logger.exception("PostgreSQL connection failed")

        return render_template(
            "index.html",
            db_status=f"Connection failed: {error}",
            db_name="-",
            db_version="-",
        ), 500


@app.route("/health")
def health():
    """
    提供 Render 或監控工具檢查 Web Service 是否正常。
    """
    return {
        "status": "ok",
        "service": "MyApp01",
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )