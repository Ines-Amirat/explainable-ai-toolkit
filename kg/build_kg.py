import csv
import networkx as nx

def build_graph(path="data/events.csv"):
    G = nx.DiGraph()

    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            G.add_node(row["id"], type=row["type"], date=row["date"])
            if row["sensor"]:
                G.add_edge(row["sensor"], row["id"], relation="measured")

    # extra rule: HeavyRain → Flood
    if "Event1" in G.nodes() and "Event2" in G.nodes():
        G.add_edge("Event1", "Event2", relation="cause_of")

    return G

KG = build_graph()
