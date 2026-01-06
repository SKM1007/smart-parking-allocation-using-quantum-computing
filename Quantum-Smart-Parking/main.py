from classical.classical_allocator import classical_allocate
from quantum.quantum_allocator import quantum_allocate
from visualization.parking_visualizer import visualize_parking

CSV_PATH = "data/parking_data.csv"

c_slot, c_dist = classical_allocate(CSV_PATH)
q_slot = quantum_allocate(CSV_PATH)

print("\nSMART CITY PARKING ALLOCATION\n")
print("Classical Allocation:")
print("Slot:", c_slot, "| Distance:", c_dist)

print("\nQuantum Allocation:")
print("Slot:", q_slot)

visualize_parking(CSV_PATH, q_slot)
