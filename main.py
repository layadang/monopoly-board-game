from game import Game
import random
import matplotlib.pyplot as plt

# for i in range(30):
#     game.next_turn(1)
#     print('========')
#     game.next_turn(0)
#     print('========')
#     game.get_player_wealth()
#     print('========')
#     game.increase_round()
#     print()

"""
TODO: Add graphs for: english and random auction types to ppt
"""

"""
TRACKING FUNCTIONS
"""

def track_player_wealth(game, wealth_history):
    """
    Appends the current wealth of both players to the wealth_history array.
    TODO: This function is kind of useless, change it so it tracks WHEN the player passes go
    """
    player_1_wealth = game.players[0].wealth
    player_2_wealth = game.players[1].wealth
    wealth_history.append((player_1_wealth, player_2_wealth))
    
def track_player_rent_paid(game, rent_history_p1, rent_history_p2):
    """
    Appends the current rent paid by both players to the rent_history array.
    """
    
    rent_history_p1.append(game.players[0].rent_paid)
    rent_history_p2.append(game.players[1].rent_paid)
    
def track_properties_owned(game, properties_owned_p1, properties_owned_p2):
    """
    Appends the number of current properties owned by both players to the properties_owned array.
    """
    player_1_properties = len(game.players[0].owned_property)
    player_2_properties = len(game.players[1].owned_property)
    
    properties_owned_p1.append(player_1_properties)
    properties_owned_p2.append(player_2_properties)
    
def track_squares_landed(board):
    """
    Iterates through all squares on the board and stores the number of times a player has landed on each square in an array.
    """
    squares_landed = []
    for square in board.squares:
        squares_landed.append(square.landed)
    return squares_landed

    
"""
    PLOTTING FUNCTIONS
"""
    
def plot_rent_history(rent_history_p1, rent_history_p2, filename):
    """
    Plots the rent history of both players and saves it to a file.
    """
    rounds = list(range(len(rent_history_p1)))
    
    plt.figure()
    plt.plot(rounds, rent_history_p1, label='Player 1 Rent Paid')
    plt.plot(rounds, rent_history_p2, label='Player 2 Rent Paid')
    plt.xlabel('Round')
    plt.ylabel('Rent Paid')
    plt.title('Rent History')
    plt.legend()
    plt.savefig(filename)
    plt.close()

def plot_wealth_history(wealth_history, filename):
    """
    Plots the wealth history of both players and saves it to a file.
    """
    rounds = list(range(len(wealth_history)))
    player_1_wealth = [wealth[0] for wealth in wealth_history]
    player_2_wealth = [wealth[1] for wealth in wealth_history]

    plt.figure()
    plt.plot(rounds, player_1_wealth, label='Player 1 Wealth')
    plt.plot(rounds, player_2_wealth, label='Player 2 Wealth')
    plt.xlabel('Round')
    plt.ylabel('Wealth')
    plt.title('Wealth History')
    plt.legend()
    plt.savefig(filename)
    plt.close()

def plot_properties_owned(properties_owned_p1, properties_owned_p2, filename):
    """
    Plots the number of properties owned by both players and saves it to a file.
    """
    rounds = list(range(len(properties_owned_p1)))
    
    plt.figure()
    plt.plot(rounds, properties_owned_p1, label='Player 1 Properties Owned')
    plt.plot(rounds, properties_owned_p2, label='Player 2 Properties Owned')
    plt.xlabel('Round')
    plt.ylabel('Properties Owned')
    plt.title('Properties Owned History')
    plt.legend()
    plt.savefig(filename)
    plt.close()
    
def plot_squares_landed(squares_landed, filename):
    """
    Plots the number of times a player landed on each square as a bar graph and saves it to a file.
    """
    squares = list(range(len(squares_landed)))
    
    plt.figure()
    plt.bar(squares, squares_landed, color='blue')
    plt.xlabel('Square')
    plt.ylabel('Number of Times Landed')
    plt.title('Number of Times Each Square Was Landed On')
    plt.savefig(filename)
    plt.close()

def main(player_1_risk, player_2_risk, auction_type, seed):
    wealth_history = []
    pass_go_counts_p1 = 0
    pass_go_counts_p2 = 0

    rent_history_p1 = []
    rent_history_p2 = []
    
    properties_owned_p1 = []
    properties_owned_p2 = []
    
    
    random.seed(seed)

    game = Game([player_1_risk, player_2_risk], auction_type)

    while (game.end_game() is None):
        print('======================')
        if (not game.next_turn(1)):
            break
        print('======================')
        if (not game.next_turn(0)):
            break
        print('======================')
        game.get_player_wealth()
        print('======================')
        game.increase_round()
        print()
        
        
        """
        Calling Tracking Functions
        """
        # Append player wealth to wealth history
        track_player_wealth(game, wealth_history)
        
        # Append player rent paid to rent history
        track_player_rent_paid(game, rent_history_p1, rent_history_p2)
        
        # Append player properties owned to properties owned history
        track_properties_owned(game, properties_owned_p1, properties_owned_p2)
        
    
    print('======================')
    print(f"Total rounds: {game.round}")
    print("FINAL WEALTH:")
    game.get_final_stats()
    
    """
    Calling plotting functions
    """
    rent_history_output = ''
    wealth_history_output = ''
    properties_owned_output = ''
    squares_landed_output = ''
    
    if(auction_type == "English"):
        rent_history_output = 'plots/rent_history_english.png'
        wealth_history_output = 'plots/wealth_history_english.png'
        properties_owned_output = 'plots/properties_owned_english.png'
        squares_landed_output = 'plots/squares_landed_english.png'
    else:
        rent_history_output = 'plots/rent_history_random.png'
        wealth_history_output = 'plots/wealth_history_random.png'
        properties_owned_output = 'plots/properties_owned_random.png'
        squares_landed_output = 'plots/squares_landed_random.png'
        
    # Plot rent paid history
    plot_rent_history(rent_history_p1, rent_history_p2, rent_history_output)
    
    # Plot the wealth history of both players and save it to a file
    plot_wealth_history(wealth_history, wealth_history_output)
    
    # Plot the properties owned history of both players and save it to a file
    plot_properties_owned(properties_owned_p1, properties_owned_p2, properties_owned_output)
    
    squares_landed = track_squares_landed(game.board)
    plot_squares_landed(squares_landed, squares_landed_output)

    
    
    # Plot the pass Go history of both players and save it to a file
    #plot_pass_go_history(game, 'plots/pass_go_history.png')


main(-1, -1, "Random", 420)