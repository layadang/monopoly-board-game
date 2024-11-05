from player import Player
from board import Square, Board
import random
import csv

# # Defining two risk-neutral players
# player_1 = Player(1, 0)
# player_2 = Player(2, 0)

# random.seed(101)

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

        self.players = [Player(1, player_risks[0]), Player(2, player_risks[1])]  # array of Player objects (len=2)
      # array of Player objects (len=2)

    def increase_round(self):
        self.round += 1

    def get_player_wealth(self):
        print(f"Player 1 has ${self.players[0].wealth}")
        print(f"Player 2 has ${self.players[1].wealth}")

    def end_game(self):
        """ 
        Determines if the game has ended.
        Returns:
            - None if the game has not ended.
            - Player who lost (bankrupt or with less wealth).
            - "TIE" if all properties are bought and both players have equal wealth.
        """
        # Check for bankruptcy
        if self.players[0].wealth < 0:
            print(f"Player 1 is bankrupt!")
            return self.players[0]
        elif self.players[1].wealth < 0:
            print(f"Player 2 is bankrupt!")
            return self.players[1]

        """
        TODO: Winning strategy could be based on per-round wealth trend
        """

        # Check if all properties are bought
        total_properties_owned = len(self.players[0].owned_property) + len(self.players[1].owned_property)
        if total_properties_owned == 28:
            if self.players[0].wealth > self.players[1].wealth:
                print("All properties bought. Player 2 loses with less wealth.")
                return self.players[1]
            elif self.players[1].wealth > self.players[0].wealth:
                print("All properties bought. Player 1 loses with less wealth.")
                return self.players[0]
            else:
                print("All properties bought and players are tied.")
                # TODO: Implement tie-breaker as random number between 1 and 2
                return "TIE"

        # Game continues
        return None


    def next_turn(self, player):
        current_player = self.players[player]
        opponent_player = self.players[abs(player-1)]

        new_position = current_player.roll_dice()
        current_square = self.board.get_property_at(new_position)
        current_square.is_landed()

        # POTENTIAL BUY
        if current_square.is_buyable():
            if self.bidding == "English":
                num_rounds = self.english_auction(current_player, opponent_player, current_square)
                print(f"Total auction rounds: {num_rounds}")
                # print(f"Square is now owned: {current_square.is_owned()}")
            if self.bidding == "Random":
                self.random_auction(current_player, opponent_player, current_square)

        # PAY RENT?
        elif (current_square.is_owned()):
            print(f"Player {current_player} landed on {current_square}, owned by Player {current_square.ownedBy}")
            owner = current_square.ownedBy
            if owner == current_player:
                return True
            else:
                # Current player pays the opponent player
                owner.change_wealth(current_square.rent)
                current_player.change_wealth(-current_square.rent)
                current_player.rent_paid += current_square.rent

                if current_player.wealth < 0:
                # END GAME HERE
                    self.end_game()
                    return False
                
        # TAX SQUARES
        elif (current_square.action  != 0):
            current_player.change_wealth(current_square.action)
            print(f"Player {current_player} got taxed ${current_square.action}")
            
        return True

    def english_auction(self, current_player, opponent_player, property):
        """
            Function to run an English auction where price increases gradually
        """
        auction_rounds = 0
        # Player initial valuation:
        player_valuation = current_player.valutation_function(property)
        opponent_valuation = opponent_player.valutation_function(property)
        print(f"Player {current_player} valuation of {property} is {player_valuation}")
        print(f"Player {opponent_player} valuation of {property} is {opponent_valuation}")

        # Case where both players cannot afford the property
        if (player_valuation == 0) and (opponent_valuation == 0):
            return auction_rounds

        # Case where player does not value property at all, so opponent pays their valuation for it
        if (player_valuation == 0 and opponent_valuation != 0):
            opponent_player.add_property(property)
            opponent_player.change_wealth(-opponent_valuation)
            property.buy_property(opponent_player)
            print(f"Player {opponent_player} wins the auction for {property} at ${opponent_valuation}")
            return auction_rounds
        
        # Vice versa of case above
        elif (opponent_valuation == 0 and player_valuation != 0):
            current_player.add_property(property)
            current_player.change_wealth(-player_valuation)
            property.buy_property(current_player)
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
                property.buy_property(opponent_player)
                print(f"Player {opponent_player} wins the auction for {property} at ${price}")
                return auction_rounds

            elif current_decision and not opponent_decision:
                # Current player wins, pays final bid price
                current_player.add_property(property)
                current_player.change_wealth(-price)
                property.buy_property(current_player)
                print(f"Player {current_player} wins the auction for {property} at ${price}")
                return auction_rounds

        print("Neither players bought the property.")

        return auction_rounds
            
    def random_auction(self, current_player, opponent_player, property):
        """
            Function to randomly select a player to buy the property at the property's set cost.
            If the selected player cannot afford it, the property is offered to the other player.
        """
        price = property.cost

        if current_player.wealth < price and opponent_player.wealth < price:
            print("Neither player can afford the property.")
            return 

        selected_player = random.choice([current_player, opponent_player])
        other_player = opponent_player if selected_player == current_player else current_player

        # Check if the selected player can afford the property
        if selected_player.wealth >= price:
            selected_player.add_property(property)
            selected_player.change_wealth(-price)
            property.buy_property(selected_player)
            print(f"Player {selected_player} wins the random auction and buys {property} for ${price}")
        elif other_player.wealth >= price:
            # If the selected player can't afford it, give it to the other player
            other_player.add_property(property)
            other_player.change_wealth(-price)
            property.buy_property(other_player)
            print(f"Player {selected_player} couldn't afford it. Player {other_player} buys {property} for ${price}")

    def current_player_wealth(self, i):
        """
            Checking current player wealth of player i
        """
        return self.players[i].wealth
    
    def get_final_stats(self, file_note, seed, loser):
        self.players[0].update_neighborhood_completeness()
        self.players[1].update_neighborhood_completeness()

        print(f"Player 1 ended with ${self.players[0].wealth}")
        print(f"Player 1 paid a total rent of ${self.players[0].rent_paid}")
        print(f"Player 1 had {len(self.players[0].owned_property)} properties")
        print(f"Player 1 passed Go {self.players[0].pass_go} times")
        print(f"Player 1 has {self.players[0].neighborhood_completeness} completed neighborhoods")

        print()

        print(f"Player 2 ended with ${self.players[1].wealth}")
        print(f"Player 2 paid a total rent of ${self.players[1].rent_paid}")
        print(f"Player 2 had {len(self.players[1].owned_property)} properties")
        print(f"Player 2 passed Go {self.players[1].pass_go} times")
        print(f"Player 2 has {self.players[1].neighborhood_completeness} completed neighborhoods")

        player_stats = [
        {
            "seed": seed, 
            "player": "Player 1",
            "num_rounds": self.round,
            "risk": self.players[0].risk,
            "wealth": self.players[0].wealth,
            "total_rent_paid": self.players[0].rent_paid,
            "properties_owned": len(self.players[0].owned_property),
            "passed_go_count": self.players[0].pass_go,
            "neighborhood_completeness": self.players[0].neighborhood_completeness,
            "loser":loser
        },
        {
            "seed": seed,
            "player": "Player 2",
            "num_rounds": self.round,
            "risk": self.players[1].risk,
            "wealth": self.players[1].wealth,
            "total_rent_paid": self.players[1].rent_paid,
            "properties_owned": len(self.players[1].owned_property),
            "passed_go_count": self.players[1].pass_go,
            "neighborhood_completeness": self.players[1].neighborhood_completeness,
            "loser":loser
        }
    ]
    
        # Append stats to CSV file
        filename = f"results/game_stats_{file_note.lower()}.csv"
        with open(filename, mode="a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=player_stats[0].keys())
            if csvfile.tell() == 0:
                writer.writeheader()
            
            for stats in player_stats:
                writer.writerow(stats)
