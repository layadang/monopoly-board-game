from game import Game

# for i in range(30):
#     game.next_turn(1)
#     print('========')
#     game.next_turn(0)
#     print('========')
#     game.get_player_wealth()
#     print('========')
#     game.increase_round()
#     print()

def main(player_1_risk, player_2_risk, auction_type):
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
    
    print('======================')
    print(f"Total rounds: {game.round}")
    print("FINAL WEALTH:")
    game.get_player_wealth()

main(1, 1, "Random")