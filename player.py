# MONOPOLY PLAYER OBJECT

# functions needed:
#   init with wealth (int), owned_properties (array), position on board (index), bankruptcy (boolean)
#   move() that randomly rolls dice (selects 1-12) and increases position on board
#   pay_rent() that decreases rent from wealth
#   buy_property() that adds property information to owned_properties array

import random
import math

random.seed(100)

class Player:
    def __init__(self, i, risk):
        # Player number as 1 or 2 (string)
        self.i = i 

        # Define risk-aversion: (1 = Risk-averse, 0 = Risk-neutral, -1 = Risk-loving)
        self.risk = risk

        # Array of bought properties as Square object
        self.owned_property = []

        # Keep track of current location on Board:
        self.position = 0

        # Keep track of wealth (initial wealth is $1,500)
        self.wealth = 1_500

        # Other metrics to keep track of:
        self.rent_paid = 0                      # total rent paid
        self.neighborhood_completeness = 0.0    # number of completed neighborhood (1=complete, .x=percent completed)
        self.pass_go = 0                        # how many laps around the board
    
    def passed_go(self):
        """
            Players get +$200 each time they pass Go
            Updates the "pass_go" counter metric
        """
        print(f"Player {self.i} Passed Go!!")
        self.wealth += 200
        self.pass_go += 1

    def roll_dice(self):
        """"
            "Make move" function where player rolls dice and
            moves position index
            Returns new position (?)
        """
        dice_outcome = random.randint(1, 6) + random.randint(1, 6)
        
        print(f'player {self.i} is at {self.position} and rolled {dice_outcome}')

        self.position += dice_outcome
        if (self.position > 40):
            self.passed_go()
        
        self.position = self.position % 40 # wrap position around the board

        return self.position
    
    def valutation_function(self, property):
        """ 
            Input: property (Square object)
                [position, name, cost, rent, neighborhood]
                    ex. [1, "Mediterranean Avenue", 60, 2, "Brown"]
        """

        ## m = NUMBER OF OTHER PROPERTY IN NEIGHBORHOOD OWNED
        ## r = PROPERTY RENT
        ## w_new = WEALTH AFTER BUYING PROPERTY --> if < 0, return 0
        ## v_other = OPPONENT'S VALUATION...?

        # Risk-aversion only affects how I bid 
        # common value as price not the market value
        # need probability of people landing on the board
        # halves the number of times people go around the board.... double valuation once you own two properties
        # p winning is p my valuation is higher than yours 

        # Start really straight-forward: here's the valuation... (first time second time)...
        ### What is a squares worth based on what they own?
        ### Ammending pre-existing code

        pass
    
    ## max_(b_i) = probability of winning auction * (f(n, m, rent, …) - b_i)
    
    def utility_function(self, x):
        """
            Utility function is how much "happiness" someone gets from having x amount of money
                Risk-averse: concave utility function, second derivative is positive
                Risk-neutral: linear utility function
                Risk-loving: convex utility function, second derivative is negative

            Using most common utility function for each preference?

            Player i's VALUATION of the property
        """
        # RISK-AVERSE PLAYER
        if (self.risk == 1):
            # Default to U=sqrt(x)
            return math.sqrt(x)
        
        # RISK-NEUTRAL PLAYER
        if (self.risk == 0):
            # Default to U=x
            return x
        
        # RISK-LOVING PLAYER
        if (self.risk == -1):
            # Default to U=x^2
            return x**2
        
    def change_wealth(self, x):
        self.wealth += x
        return self.wealth

player_1 = Player(1, 0)
player_2 = Player(2, 0)

for i in range(20):
    # testing 10 rolls
    player_1.roll_dice()
    player_2.roll_dice()