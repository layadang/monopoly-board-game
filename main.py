import matplotlib.pyplot as plt
import random
from game import Game

def track_player_wealth(game, wealth_history):
    """
        Appends the current wealth of both players to the wealth_history array.
    """
    player_1_wealth = game.players[0].wealth
    player_2_wealth = game.players[1].wealth
    wealth_history.append((player_1_wealth, player_2_wealth))

def plot_live_wealth(wealth_history, player_1_risk, player_2_risk, auction_type, seed):
    """
    Plots the live wealth history of both players.
    """
    rounds = list(range(len(wealth_history)))
    player_1_wealth = [wealth[0] for wealth in wealth_history]
    player_2_wealth = [wealth[1] for wealth in wealth_history]

    plt.clf()  # clear the previous plot
    plt.plot(rounds, player_1_wealth, label='Player 1 Wealth')
    plt.plot(rounds, player_2_wealth, label='Player 2 Wealth')
    plt.xlabel('Round')
    plt.ylabel('Wealth')
    plt.title(f'Player Wealth for {auction_type} Auction \nRisks={[player_1_risk, player_2_risk]} Seed={seed}')
    plt.legend()
    plt.pause(0.05)

def main(player_1_risk, player_2_risk, auction_type, seed):
    wealth_history = []

    random.seed(seed)
    game = Game([player_1_risk, player_2_risk], auction_type)
    
    plt.ion()  
    fig = plt.figure()  

    while (game.end_game() is None):
        if not game.next_turn(1):
            break
        if not game.next_turn(0):
            break
        game.increase_round()
        
        track_player_wealth(game, wealth_history)
        
        plot_live_wealth(wealth_history, player_1_risk, player_2_risk, auction_type, seed)

    loser=game.end_game()
    print('======================')
    print(f"Total rounds: {game.round}")
    print("FINAL STATS:")
    game.get_final_stats(auction_type, seed, loser)

    plt.ioff()  
    plt.pause(2)  
    plt.close(fig)

## CHANGE THIS FOR DATA COLLECTION!!
for i in range(20):
    seed = 100 + i
    main(0, 1, "English", seed)
