import pandas as pd
import matplotlib.pyplot as plt

def visualize_parking(csv_path, selected_slot):
    data = pd.read_csv(csv_path)

    fig, ax = plt.subplots()
    ax.set_title("Quantum-Based Smart Parking Allocation")

    for i, row in data.iterrows():
        color = "green" if row["availability"] == 1 else "red"

        rect = plt.Rectangle((i, 0), 0.8, 0.8,
                              facecolor=color,
                              edgecolor="black",
                              linewidth=2)
        ax.add_patch(rect)

        ax.text(i + 0.4, 0.4,
                f"{row['slot_id']}\nD={row['distance']}",
                ha="center", va="center",
                color="white", fontsize=9)

        if row["slot_id"] == selected_slot:
            highlight = plt.Rectangle((i - 0.05, -0.05),
                                      0.9, 0.9,
                                      fill=False,
                                      edgecolor="blue",
                                      linewidth=3)
            ax.add_patch(highlight)

    ax.set_xlim(-0.2, len(data))
    ax.set_ylim(-0.2, 1)
    ax.axis("off")
    plt.show()
