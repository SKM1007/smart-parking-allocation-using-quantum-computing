import pandas as pd

def classical_allocate(csv_path):
    data = pd.read_csv(csv_path)
    free_slots = data[data["availability"] == 1]
    best = free_slots.loc[free_slots["distance"].idxmin()]
    return best["slot_id"], best["distance"]
