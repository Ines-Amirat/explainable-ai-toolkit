import os
import sys

# Ajoute le dossier parent (explainable-ai-toolkit) au PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)



from fastapi import FastAPI
from reasoning.explain import explain_event
from nlp.summary import summarize
from kg.build_kg import KG

app = FastAPI()

@app.get("/neighbors/{node_id}")
def neighbors(node_id: str):
    return list(KG.neighbors(node_id))

@app.get("/explain/{event_id}")
def explain(event_id: str):
    return explain_event(event_id)

@app.get("/summary/{event_id}")
def summary(event_id: str):
    return {"summary": summarize(event_id)}
