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

TODO: wealth over time graph
TODO: rent paid over time graph
TODO: Amount of properties owned over time
TODO: Track what squares are landed on the most -> square object -> self.landed

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

def main(player_1_risk, player_2_risk, auction_type, seed):
    wealth_history = []
    pass_go_counts_p1 = 0
    pass_go_counts_p2 = 0

    rent_history_p1 = []
    rent_history_p2 = []
    
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
        
        # Append player wealth to wealth history
        track_player_wealth(game, wealth_history)
        
        # Append player rent paid to rent history
        track_player_rent_paid(game, rent_history_p1, rent_history_p2)
        
        # Track when players pass Go
        # track_pass_go(game, pass_go_counts_p1, pass_go_counts_p2, game.round)
    
    print('======================')
    print(f"Total rounds: {game.round}")
    print("FINAL WEALTH:")
    game.get_final_stats()
    
    # Plot the wealth history of both players and save it to a file
    plot_wealth_history(wealth_history, 'plots/wealth_history.png')
    
    # Plot the pass Go history of both players and save it to a file
    #plot_pass_go_history(game, 'plots/pass_go_history.png')


main(-1, -1, "English", 420)