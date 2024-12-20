# MONOPOLY BOARD OBJECT

# functions needed:
#   init with all squares (array of Property object) and index (array), and bidding strategy
#   get_property_at() that returns the rent price of certain index
#   auction() that simulations an auction, takes in property,  player object, and bidding strategy

import pandas as pd

# LOADING IN DATA...

# squares data from: https://github.com/jm-contreras-zz/monopoly/blob/master/board.csv
board_squares = pd.read_csv("data/board.csv")

# drop irrelevant columns
board_squares = board_squares.drop(['rent_house_1', 
                                    'rent_house_2', 
                                    'rent_house_3', 
                                    'rent_house_4', 
                                    'build_cost', 
                                    'rent_hotel'], 
                                    axis=1)

# neighborhood sizes
neighborhood_size_info = pd.read_csv("data/neighborhood_info.csv")
neighborhood_dict = dict(zip(neighborhood_size_info.iloc[:, 0], neighborhood_size_info.iloc[:, 1]))

class Square():
    """
        Square information
        Example:
        (1, "Mediterranean Avenue", 60, 2, "Brown", None)
        (5, "Income Tax", None, None, None, -200)
    """
    def __init__(self, position, name, cost, rent, neighborhood, action):
        # should we implement mortgage?

        # Position on board (0-39)
        self.position = position

        # Name of square (string)
        self.name = name

        # Cost to buy (int)
        self.cost = cost

        # Standard rent (no houses!) (int)
        self.rent = rent

        # Neighborhood (string)
        self.neighborhood = neighborhood

        # Effect on wealth (if square is Go or Tax) (int)
        self.action = action

        # Define who owns property (string)
        self.ownedBy = None

        # Keep track of how many times the 
        self.landed = 0

    def __str__(self):
        return f'{self.position} {self.name}'
    
    def buy_property(self, player):
        """
            Assign property to Player object
        """
        self.ownedBy = player
    
    def is_owned(self):
        return (self.ownedBy is not None)
    
    def is_buyable(self):
        if self.is_owned():
            return False
        else:
            return (self.rent != 0)

    def is_landed(self):
        """
            Keep track of how often square was landed on
        """
        self.landed += 1

    def get_neighborhood_size(self):
        """ 
            return size of neighborhood for this square
            (empty string if look-up failed)
        """
        return neighborhood_dict.get(self.neighborhood, "")

    
class Board:
    """
        Main game board with information of squares
    """
    def __init__(self):
        """
            Set up board squares (an array of Square objects)
        """
        self.squares = []
        for i, row in board_squares.iterrows():
            # for income and luxury tax squares:
            action = -row['tax']
            
            # Wealth logic moved to player.py
            # if (i==0):
            #      # manual adjustmet for +200 when passing Go
            #     action = 200
                
            to_add = Square(i, 
                            row['name'], 
                            row['price'], 
                            row['rent'],
                            row['monopoly'],
                            action)
            
            self.squares.append(to_add)

    def get_property_at(self, i):
        return self.squares[i]
    
    def get_neighborhood_size(self, neighborhood):
        """ 
            input is name of neighborhood (str) 
                ex. Brown, Railroad, Light Blue
        """
        for _, row in neighborhood_size_info.iterrows():
            if row['name'] == neighborhood:
                return row['monopoly_size']
            
        # else it is not a neighborhood
        return 0

board = Board()
# chance_square = board.get_property_at(36)
# print(chance_square.is_buyable())
