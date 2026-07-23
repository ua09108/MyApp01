"""
Database Connection Module
Author : Ray
Project : MyApp01
"""

import os
import psycopg


def get_connection():
    """
    建立 PostgreSQL Connection
    """

    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL not found.")

    return psycopg.connect(database_url)