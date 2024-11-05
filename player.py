# MONOPOLY PLAYER OBJECT

import random
import math
import numpy as np

# random.seed(101)

import numpy as np

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
        self.neighborhood_completeness = 0.0    # number of completed neighborhood
        self.pass_go = 0                        # how many laps around the board

    def __str__(self):
        return str(self.i)
    
    def passed_go(self):
        """
            Players get +$200 each time they pass Go
            Updates the "pass_go" counter metric
        """
        print(f"Player {self.i} Passed Go!")
        self.wealth += 200
        self.pass_go += 1

    def roll_dice(self):
        """"
            "Make move" function where player rolls dice and
            moves position index
            Returns new position (?)
        """
        dice_outcome = random.randint(1, 6) + random.randint(1, 6)
        
        print(f'Player {self.i} is at {self.position} and rolled {dice_outcome}')

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
        # position, name, cost, rent, neighborhood = property

        # position = property.position
        # name = property.name
        cost = property.cost
        rent = property.rent
        neighborhood = property.neighborhood

        ## m = NUMBER OF OTHER PROPERTY IN NEIGHBORHOOD OWNED
        ## r = PROPERTY RENT
        ## w_new = WEALTH AFTER BUYING PROPERTY --> if < 0, return 0
        ## v_other = OPPONENT'S VALUATION...?

        # IF PLAYER CANNOT AFFORD PROPERTY
        if cost > self.wealth:
            return 0
        
        base_valuation = cost + rent                        # multiply with square landing frequency factor when we find it
        wealth_factor = 1 + np.log(self.wealth / 1_500+1)           # factor in current wealth

        same_neighborhood_properties = [p for p in self.owned_property if p.neighborhood == neighborhood]
        neighborhood_completion_factor = (1 + len(same_neighborhood_properties) / property.get_neighborhood_size())
        valuation = base_valuation * neighborhood_completion_factor * wealth_factor

        # Apply risk adjustment
        if self.risk == 1:  # Risk-averse: reduce valuation
            valuation *= 0.81
        elif self.risk == -1:  # Risk-loving: increase valuation
            valuation *= 1.2
        
        if valuation >= self.wealth: # property worth entire wealth
            return self.wealth

        # Risk-neutral: use base valuation (do nothing)

        return valuation
    
    def decide_buy(self, valuation):
        """ 
            Player will decide to buy if buying property makes player 50% more happy
        """
        return self.utility_function(self.wealth) < 1.5 * self.utility_function(self.wealth - valuation)
    
    ## max_(b_i) = probability of winning auction * (f(n, m, rent, …) - b_i)

    def add_property(self, property):
        """
        **Only adds property, does not change wealth**
            Input: property (Square object)
                [position, name, cost, rent, neighborhood]
                    ex. [1, "Mediterranean Avenue", 60, 2, "Brown"]
        """
        if property not in self.owned_property:
            self.owned_property.append(property)
        else:
            print(f"Player {self.i} already owns {property}. Skipping addition.")

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
        # self.wealth = self.wealth.round(2)
        return self.wealth
    
    def update_neighborhood_completeness(self):
        """
            Calculate number of completed neighborhoods
        """
        # dictionary to store count of properties owned per neighborhood
        neighborhood_counts = {}
        
        for property in self.owned_property:
            neighborhood = property.neighborhood

            if neighborhood not in neighborhood_counts:
                neighborhood_counts[neighborhood] = 0

            neighborhood_counts[neighborhood] += 1

            if (neighborhood_counts[neighborhood] == property.get_neighborhood_size()):
                self.neighborhood_completeness += 1

        return self.neighborhood_completeness


# player_1 = Player(1, 0)
# player_2 = Player(2, 0)

# for i in range(20):
#     player_1.roll_dice()
#     player_2.roll_dice()