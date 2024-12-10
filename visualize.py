import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

def visualize_board(data_file):
    # Load the Monopoly board data
    board_data = pd.read_csv(data_file)

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
    
    
    
def group_winners(data_file):
    """
    Currently Useless
    """
    # Load the Monopoly game data
    game_data = pd.read_csv(data_file)
    
    # Initialize a counter for English winners
    english_winner_count = 0
    vickrey_winner_count = 0
    random_winner_count = 0

    # Increment the counter for each row where 'is_English' is True
    for _, row in game_data.iterrows():
        if row['is_English']:
            english_winner_count += 1
        elif row['is_Vickrey']:
            vickrey_winner_count += 1
        elif row['is_Random']:
            random_winner_count += 1

            # Plot the number of winners
            winner_counts = {
                'English': english_winner_count,
                'Vickrey': vickrey_winner_count,
                'Random': random_winner_count
            }

    plt.figure(figsize=(8, 6))
    plt.bar(winner_counts.keys(), winner_counts.values(), color=['blue', 'green', 'red'])
    plt.xlabel('Winner Type')
    plt.ylabel('Number of Wins')
    plt.title('Number of Wins by Winner Type')
    plt.show()
    
    
    
    
    
def plot_neighborhood_completeness_vs_win(data_file):
    """
    Plots if neighborhood_completeness corresponds to a win.
    """
    # Load the data
    data = pd.read_csv(data_file)
    
    # Filter data by auction type
    english_data = data[data['is_English'] == 1]
    vickrey_data = data[data['is_Vickrey'] == 1]
    random_data = data[data['is_Random'] == 1]
    
    english_completeness_values = []
    vickrey_completeness_values = []
    random_completeness_values = []
    
    for _, row in english_data.iterrows():
        if row['winner'] == 1:
            english_completeness_values.append(row['P1_neighborhood_completeness'])
        elif row['winner'] == 2:
            english_completeness_values.append(row['P2_neighborhood_completeness'])

    # Append risk values of winners for Vickrey auction
    for _, row in vickrey_data.iterrows():
        if row['winner'] == 1:
            vickrey_completeness_values.append(row['P1_neighborhood_completeness'])
        elif row['winner'] == 2:
            vickrey_completeness_values.append(row['P2_neighborhood_completeness'])

    # Append risk values of winners for Random auction
    for _, row in random_data.iterrows():
        if row['winner'] == 1:
            random_completeness_values.append(row['P1_neighborhood_completeness'])
        elif row['winner'] == 2:
            random_completeness_values.append(row['P2_neighborhood_completeness'])
    
    
    
    
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.hist(english_completeness_values, bins=20, color='blue', alpha=0.7)
    plt.title('Neighborhood Completeness of Winners - English Auction')
    plt.xlabel('Neighborhood Completeness')
    plt.ylabel('Frequency')

    plt.subplot(3, 1, 2)
    plt.hist(vickrey_completeness_values, bins=20, color='green', alpha=0.7)
    plt.title('Neighborhood Completeness of Winners - Vickrey Auction')
    plt.xlabel('Neighborhood Completeness')
    plt.ylabel('Frequency')

    plt.subplot(3, 1, 3)
    plt.hist(random_completeness_values, bins=20, color='red', alpha=0.7)
    plt.title('Neighborhood Completeness of Winners - Random Auction')
    plt.xlabel('Neighborhood Completeness')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.savefig("results/neighborhood_completeness_vs_win.png")

    plt.show()
    
    
    
def plot_wins_and_risk(data_file):
    """
    Plots the neighborhood completeness and risk value grouped by winners as a bar graph.
    Creates subplots for English auction, Vickrey auction, and Random auction.
    """
    # Load the data
    data = pd.read_csv(data_file)
    
    # Filter data by auction type
    english_data = data[data['is_English'] == 1]
    vickrey_data = data[data['is_Vickrey'] == 1]
    random_data = data[data['is_Random'] == 1]
    
    # Initialize arrays to store risk values of winners
    english_risk_values = []
    vickrey_risk_values = []
    random_risk_values = []

    # Append risk values of winners for English auction
    for _, row in english_data.iterrows():
        if row['winner'] == 1:
            english_risk_values.append(row['P1_risk'])
        elif row['winner'] == 2:
            english_risk_values.append(row['P2_risk'])

    # Append risk values of winners for Vickrey auction
    for _, row in vickrey_data.iterrows():
        if row['winner'] == 1:
            vickrey_risk_values.append(row['P1_risk'])
        elif row['winner'] == 2:
            vickrey_risk_values.append(row['P2_risk'])

    # Append risk values of winners for Random auction
    for _, row in random_data.iterrows():
        if row['winner'] == 1:
            random_risk_values.append(row['P1_risk'])
        elif row['winner'] == 2:
            random_risk_values.append(row['P2_risk'])

    # Plotting the risk values for each auction type
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.hist(english_risk_values, bins=20, color='blue', alpha=0.7)
    plt.title('Risk Values of Winners - English Auction')
    plt.xlabel('Risk Value')
    plt.ylabel('Frequency')

    plt.subplot(3, 1, 2)
    plt.hist(vickrey_risk_values, bins=20, color='green', alpha=0.7)
    plt.title('Risk Values of Winners - Vickrey Auction')
    plt.xlabel('Risk Value')
    plt.ylabel('Frequency')

    plt.subplot(3, 1, 3)
    plt.hist(random_risk_values, bins=20, color='red', alpha=0.7)
    plt.title('Risk Values of Winners - Random Auction')
    plt.xlabel('Risk Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.savefig("results/neighborhood_completeness_and_risk.png")

    plt.show()


def plot_distributions(data_file):
    # Load the data
    data = pd.read_csv(data_file)
    
    # Define paired features
    paired_features = [
        'neighborhood_completeness',
        'passed_go_count',
        'properties_owned',
        'total_rent_paid',
        'wealth'
    ]
    
    # Define single features
    single_features = [
        'num_rounds',
        'winner',
    ]
    
    # Plot distributions for paired features
    for feature in paired_features:
        plt.figure(figsize=(10, 6))
        plt.hist(data[f'P1_{feature}'], bins=20, color='blue', alpha=0.5, label='P1')
        plt.hist(data[f'P2_{feature}'], bins=20, color='red', alpha=0.5, label='P2')
        plt.title(f'Distribution of {feature} for P1 and P2')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'results/distribution_{feature}_P1_P2.png')
        plt.show()
    
    # Plot distributions for single features
    for feature in single_features:
        plt.figure(figsize=(10, 6))
        plt.hist(data[feature], bins=20, color='blue', alpha=0.7)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.savefig(f'results/distribution_{feature}.png')
        plt.show()
    
    # Plot distribution of overall winners
    plt.figure(figsize=(10, 6))
    plt.hist(data['winner'], bins=3, color='green', alpha=0.7)
    plt.title('Distribution of Overall Winners')
    plt.xlabel('Winner')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('results/distribution_overall_winners.png')
    plt.show()


if __name__ == "__main__":
    # visualize_board()
    # group_winners("results/full_data.csv")
    # plot_neighborhood_completeness_vs_win("results/full_data.csv")
    # plot_wins_and_risk("results/full_data.csv")
    plot_distributions("results/full_data.csv")
    

"""
Stuff I could plot:



grouped by winners, plot the neighborhood_completeness and risk value as a bar graph. create subplots for english auction, vickrey auction, and random auction

find the best strategy for winning the game then pit it against a trained model

"""