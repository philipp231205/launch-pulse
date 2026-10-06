from fastapi import FastAPI
import os
from dotenv import load_dotenv

import psycopg
from psycopg.rows import dict_row

app = FastAPI()

load_dotenv()

DB_CONNECTION = os.getenv("DATABASE_URL")

@app.get("/health")
def get_health() -> dict[str, str]:
	return {"status": "UP"}

@app.get("/launches")
def get_launches() -> dict:

	with psycopg.connect(DB_CONNECTION, row_factory = dict_row) as conn:
		rows = conn.execute(
			"SELECT * FROM launches ORDER BY launch_time"
		).fetchall()

	result = {row["id"]: row for row in rows}

	return result
