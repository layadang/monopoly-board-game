# MONOPOLY PLAYER OBJECT

# functions needed:
#   init with wealth (int), owned_properties (array), position on board (index), bankruptcy (boolean)
#   move() that randomly rolls dice (selects 1-12) and increases position on board
#   pay_rent() that decreases rent from wealth
#   add_property() that adds property information to owned_properties array

class Player:
    def __init__(self, i):
        # Player number as 1 or 2
        self.i = i 