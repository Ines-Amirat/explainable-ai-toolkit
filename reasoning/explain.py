
import networkx as nx
from kg.build_kg import KG

def explain_event(event_id: str):
    results = []
    for node in KG.nodes():
        if nx.has_path(KG, node, event_id):
            results.append(nx.shortest_path(KG, node, event_id))
    return results
