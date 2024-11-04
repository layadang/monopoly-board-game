from game import Game

game = Game([0, 1], "English")

for i in range(10): 
    game.next_turn(1)
    print('========')
    game.next_turn(0)
    print('========')
    game.increase_round()

print(f"Total rounds: {game.round}")
print(f"Player 1 final wealth: {game.current_player_wealth(0)}")
print(f"Player 2 final wealth: {game.current_player_wealth(1)}")