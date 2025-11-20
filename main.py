from fastapi import FastAPI
import networkx as nx

# ----- Build Knowledge Graph -----
G = nx.DiGraph()

# Nodes
G.add_node("Event1", type="HeavyRain", date="2021-09-10")
G.add_node("Event2", type="Flood", date="2021-09-12")
G.add_node("SensorA", type="RainGauge")
G.add_node("SensorB", type="RiverGauge")

# Edges
G.add_edge("SensorA", "Event1", relation="measured")
G.add_edge("SensorB", "Event2", relation="triggered")
G.add_edge("Event1", "Event2", relation="cause_of")

# ----- Reasoning -----
def explain_event(event_id: str):
    results = []
    for node in G.nodes():
        if nx.has_path(G, node, event_id):
            results.append(nx.shortest_path(G, node, event_id))
    return results

# ----- NLP summary -----
def summarize(event_id: str) -> str:
    node = G.nodes()[event_id]
    t = node.get("type", "event")
    d = node.get("date", "unknown date")
    return f"{event_id} is classified as {t} and occurred on {d}."

# ----- FastAPI app -----
app = FastAPI()

@app.get("/neighbors/{node_id}")
def neighbors(node_id: str):
    return list(G.neighbors(node_id))

@app.get("/explain/{event_id}")
def explain(event_id: str):
    return explain_event(event_id)

@app.get("/summary/{event_id}")
def summary(event_id: str):
    return {"summary": summarize(event_id)}
