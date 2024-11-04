from player import Player
from board import Square, Board

# Defining two risk-neutral players
player_1 = Player(1, 0)
player_2 = Player(2, 0)

class Game:
    def __init__(self, player_risks, bidding):
        """
            Risk is array of 1, 0, or -1 for risk-averse, risk-neutral, or risk-loving players
            Biddding is type of auction design, where:
                1: English auctions
                2: Dutch auctions
                3: Blind auctions
                4: Vickery auctions
        """
        self.round = 0          # number of turns
        self.bank = 0           # keep track of how much money is in the economy
        self.board = Board()    # board object
        self.bidding = bidding  # auction design

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

        if current_square.is_buyable():
            print(current_square)
            if self.bidding == "English":
                num_rounds = self.english_auction(current_player, opponent_player, current_square)
                print(f"Total number of rounds is: {num_rounds}")
        return

    def english_auction(self, current_player, opponent_player, property):
        """
            Function to run an English auction where price increases gradually
        """
        auction_rounds = 0
        # Player initial valuation:
        player_valuation = current_player.valutation_function(property)
        print(f"player valuation of {property} is {player_valuation}")
        opponent_valuation = opponent_player.valutation_function(property)
        print(f"opponent valuation of {property} is {opponent_valuation}")

        # Case where both players cannot afford the property
        if (player_valuation == 0) and (opponent_valuation == 0):
            return auction_rounds
        
        # Case where player does not value property at all, so opponent pays their valuation for it
        if (player_valuation == 0 and opponent_valuation != 0):
            opponent_player.add_property(property)
            opponent_player.change_wealth(-opponent_valuation)
            print(f"Player {opponent_player} wins the auction for {property} at ${opponent_valuation}")
            return auction_rounds
        # Vice versa of case above
        elif (opponent_valuation == 0 and player_valuation != 0):
            current_player.add_property(property)
            current_player.change_wealth(-player_valuation)
            print(f"Player {current_player} wins the auction for {property} at ${player_valuation}")
            return auction_rounds

        # BEGIN AUCTION: Starting bid as 80% of min valuation
        price = min(player_valuation, opponent_valuation) * 0.8  

        current_decision, opponent_decision = True, True         # initial decision: both players willing to pay

        # Run auction until someone is no longer willing to pay
        while (current_decision and opponent_decision):
            auction_rounds += 1
            print(f"Auction at price ${price}: Player {current_player} decision = {current_decision}, Player {opponent_player} decision = {opponent_decision}")

            price *= 1.1 # 10% increase price each time

            current_decision = current_player.decide_buy(price)
            opponent_decision = opponent_player.decide_buy(price)

            if not current_decision and opponent_decision:
                # Opponent wins, pays final bid price
                opponent_player.add_property(property)
                opponent_player.change_wealth(-price)
                print(f"Player {opponent_player} wins the auction for {property} at ${price}")
                break
            elif current_decision and not opponent_decision:
                # Current player wins, pays final bid price
                current_player.add_property(property)
                current_player.change_wealth(-price)
                print(f"Player {current_player} wins the auction for {property} at ${price}")
                break
        return auction_rounds
            
    def current_player_wealth(self, i):
        """
            Checking current player wealth of player i
        """
        return self.players[i].wealth