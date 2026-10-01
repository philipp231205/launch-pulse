from fastapi import FastAPI
import json

app = FastAPI()

launches = {
	1: {"name": "Starship Flight 15"},
	2: {"name": "Spectrum Block 3"},
	3: {"name": "Artemis III"}
}

@app.get("/health")
def get_health():
	return {"status": "UP"}

@app.get("/launches")
def get_launches():
	return launches