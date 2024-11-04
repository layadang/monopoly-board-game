import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load the Monopoly board data
board_data_path = "data/board.csv"
board_data = pd.read_csv(board_data_path)

# Map neighborhoods to colors for visualization
neighborhood_colors = {
    "Brown": "saddlebrown",
    "Light Blue": "skyblue",
    "Pink": "pink",
    "Orange": "orange",
    "Red": "red",
    "Yellow": "yellow",
    "Green": "green",
    "Dark Blue": "blue",
    "Railroad": "black",
    None: "grey"  # For non-property squares (e.g., Go, Taxes, Community Chest)
}

# Assign colors based on the 'monopoly' (neighborhood) column
board_data['color'] = board_data['monopoly'].map(neighborhood_colors)

# Initialize the Monopoly board graph (circular layout of 40 squares)
G = nx.circular_ladder_graph(20)  # Simplified circular representation of 40 squares (0 to 39)

# Layout positions around a circle
pos = nx.circular_layout(G)

# Plotting the Monopoly board with colored neighborhoods
plt.figure(figsize=(12, 12))

# Plot each square as a node in a circular layout
for _, row in board_data.iterrows():
    square_position = row['position'] - 1  # Adjust to zero-index for plot
    color = row['color']
    label = row['name']

    # Place nodes in circular positions, like a Monopoly board
    nx.draw_networkx_nodes(G, pos, nodelist=[square_position], node_color=color, node_size=500)
    nx.draw_networkx_labels(G, pos, labels={square_position: label}, font_size=6)

# Draw edges to complete the circular board layout
nx.draw_networkx_edges(G, pos, alpha=0.5)

plt.title("Monopoly Board with Neighborhood Colors")
plt.show()
