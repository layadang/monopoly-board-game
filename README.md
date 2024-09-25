# CS 506 Final Project: Predicting Monopoly Board Game Outcomes

## Collaborators 
* Laya Dang (pd03@bu.edu)
* Gabi Guillermo (gabe441@bu.edu)

## Project Description 
This project aims to model *n* number of two-player auction-based monopoly board games to find the best strategy of accumulating the most wealth by the end of the game. In this game scenario, unlike traditional monopoly, every unbought property immediately goes to auction. The strategy would be how much each player bids on the property. We hope to find a consistent winning strategy that takes into consideration: player's current wealth, opponent's current wealth, price, rent, and number of properties in the same neighborhood already owned.

For the sake of simplicity, we will NOT implement ability to:
- Upgrades on properties (i.e. build houses and hotels)
- Chance/community chest cards
- Going to jail.

## Methodology
### Game Logic Implementation
We will begin by building the logic for the Monopoly board game and players as Python objects. The board class will follow available data on the classic Board and actions for each squares. The player class has the ability to row the dice, keep track of owned property and wealth, and specify a player's auction strategy.

### Data Collection
These objects will track the players' actions and game state throughout each game. The inputs will include player decisions, the outcomes of dice rolls, and auction strategies.

### Feature Extraction
The key features to track for each turn of the game include:
- Dice roll (out of 12)
- Player's wealth
- Number of properties owned
- Rent paid
- Auction results (winning bids and price)
- Final results of who won each game
- Other relevant data points, such as neighborhood ownership and frequency of landing on properties

We will run these simulations *n* times until we have sufficient data for analysis.

## Modeling and Visualizations
After collecting the data, we will apply machine learning models to identify patterns and predict optimal strategies. Visualizations will include wealth over time, auction outcomes, and the effect of different bidding strategies on game results. We could also visualzie where on the board players are landing on the most to determine which neighborhoods are best to buy. We will explore various algorithms, such as decision trees or reinforcement learning, to predict the best moves based on game states.


## Testing
We will validate the effectiveness of our model by testing it on unseen Monopoly runs. Metrics for success will include winning percentage, average wealth by the end of the game, and the impact of each factor (e.g., property ownership, rent payments, and auction bids) on the game outcome.
