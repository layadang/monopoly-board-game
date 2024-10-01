# CS 506 Final Project: Predicting Monopoly Board Game Outcomes

## Collaborators 
* Laya Dang (pd03@bu.edu)
* Gabi Guillermo (gabe441@bu.edu)

## Project Description 
This project aims to model a two-player auction-based monopoly board game to find the best strategy of accumulating the most wealth by the end of the game. In this game scenario, every unbought property immediately goes to auction when a player lands on it. The strategy would be how much a player chooses to bid on the property. We hope to find a consistent winning strategy that takes into consideration player's current wealth, opponent's current wealth, price, rent, number of properties in the same neighborhood already owned, and so on.

For the sake of simplicity, we will NOT implement ability to:
- Upgrade properties (i.e. build houses and hotels),
- Chance/community chest cards,
- Going to jail, and
- Auction off owned property when rent cannot be paid (so player automatically loses if they cannot pay rent).

## Methodology
### Game Logic Implementation
We will begin by building the logic for the Monopoly board game and players as Python objects. The `Board` class will follow available data on the classic Board and keep track of property information (price, tax, neighborhood). The `Player` class has the ability to roll the dice(s), keep track of owned property and wealth, and specify a player's auction strategy.

As a recap the rules of Monopoly and key game elements:
1. **Board Layout**: 
   - The board consists of 40 squares, including properties, utilities, railroads, and special spaces (like "Go," "Free Parking," and "Income Tax").
   - Properties are divided into neighborhoods or color groups.

2. **Properties**: 
   - When a player lands on an unowned property, it immeddiate goes to auction. 
   - If a property is owned by another player, rent must be paid based on the property's value.
   
3. **Wealth**: 
   - Each player starts with $1,500. Players can accumulate wealth through rent collection and passing Go (get $200).
   - Going bankrupt (i.e. cannot pay rent) eliminates a player from the game.

4. **Rolling the Dice**:
   - Players take turns rolling two dice to move around the board.
   - The outcome of dice rolls determines movement and whether the player lands on an unowned property, owned property, or other squares.

Other game rules can be found at [Hasbro's official rule book](https://www.hasbro.com/common/instruct/00009.pdf).

### Auction Theory
A player's auction strategy will depend on:
- Expected value from the property (rent, how frequently that square gets landed on, what in the neighborhood is already owned)
- Price of property in relation to current wealth 

We will find the best strategy for the four most common auction designs, described as:
- **English auctions**: players continue to make higher bids until they are no longer willing to to pay higher than the last price
- **Dutch auctions**: a high price is initially set and decreases until a player is willing to to pay the current price
- **Blind auctions**: players simultaneously bid a price without knowing the opponent's price, and the higher bid wins
- **Vickery auctions**: the highest price bidder wins, but only has to pay the second-highest price

### Data Collection
The Python objects created above will, by design, track the players' actions and game state throughout each game. The inputs will include player decisions, the outcomes of dice rolls, and auction strategies.

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

## Visualizations and Modeling

 We will first visualize where on the board players are landing on the most to determine which neighborhoods are best to buy and incorporate that into the Player's strategy. 

After collecting the data, we will apply machine learning models to identify patterns and predict optimal strategies. Visualizations can include:
 - wealth over time
 - auction outcomes
 - the effect of different bidding strategies on game results
 
 We will explore various algorithms, such as decision trees or reinforcement learning, to predict the best moves based on game states. According to similar previous studies, 


## Testing
We will validate the effectiveness of our model by testing it on unseen Monopoly runs. Metrics for success will include winning percentage, average wealth by the end of the game, and the impact of each factor (e.g., property ownership, rent payments, and auction bids) on the game outcome.
