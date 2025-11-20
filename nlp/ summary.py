from kg.build_kg import KG

def summarize(event_id: str) -> str:
    node = KG.nodes()[event_id]
    t = node.get("type", "event")
    d = node.get("date", "unknown date")
    return f"{event_id} is classified as {t} and occurred on {d}."
