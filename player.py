# MONOPOLY PLAYER OBJECT

# functions needed:
#   init with wealth (int), owned_properties (array), position on board (index), bankruptcy (boolean)
#   move() that randomly rolls dice (selects 1-12) and increases position on board
#   pay_rent() that decreases rent from wealth
#   add_property() that adds property information to owned_properties array

import numpy as np

class Player:
    def __init__(self, i):
        # Player number as 1 or 2
        self.i = i
        
        # Wealth
        self.wealth = 1500
        
        # Owned properties
        self.owned_properties = []
        
        # Position on board
        self.position = 0
        
        # Bankruptcy status
        self.bankruptcy = False
        
        # Auction strategy
        self.auction_strategy = None
        
    def move(self):
        """
            Randomly rolls dice (1-12) and moves player position
            
            TODO: Add wealth effect of passing Go?
        """
        roll = np.random.randint(1, 13)
        self.position += roll
        if(self.position >= 40):
            self.position -= 40
            
            # Add wealth effect of passing Go
            self.wealth += 200
            
                        
    def pay_rent(self, rent):
        """
            Decrease rent from wealth
        """
        self.wealth -= rent
        
        # Check if the player is bankrupt
        self.bankrupt_check()
        
    def add_property(self, property):
        """
            Add property to owned_properties
        """
        self.owned_properties.append(property)
    
    def bankrupt_check(self):
        """
            Check if player is bankrupt
        """
        if(self.wealth < 0):
            self.bankruptcy = True
        return self.bankruptcy