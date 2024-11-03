from player import Player
from board import Square, Board

# Defining two risk-neutral players
player_1 = Player(1, 0)
player_2 = Player(2, 0)

class Game:
    def __init__(self, player_risks):
        """
            Risk is array of 1, 0, or -1 for risk-averse, risk-neutral, or risk-loving players
        """
        self.round = 0          # number of turns
        self.bank = 0           # keep track of how much money is in the economy
        self.board = Board()    # board object

        player_1 = Player(1, player_risks[0])
        player_2 = Player(2, player_risks[1])
        self.players = [player_1, player_2]      # array of Player objects (len=2)

    def increase_round(self):
        self.round += 1

    def next_turn(self, player):
        current_player = self.players[player]
        opponent_player = self.players[abs(player-1)]

        new_position = current_player.roll_dice()
        current_square = self.board.get_property_at(new_position)

        player_valuation = current_player.valutation_function(current_square)
        print(f"player valuation of {current_square} is {player_valuation}")

        opponent_valuation = opponent_player.valutation_function(current_square)
        print(f"opponent valuation of {current_square} is {opponent_valuation}")


game = Game([0, 1])
game.next_turn(1)
print('========')
game.next_turn(0)
print('========')
game.next_turn(1)
print('========')
game.next_turn(0)
print('========')