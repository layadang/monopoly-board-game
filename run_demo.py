from main import main
import pickle
import pandas as pd

# Run a demo of a andom auction
# Between a risk-neutral player (Player 1) and risk-averse player (Player 2)
main(player_1_risk=0, player_2_risk=1, auction_type="Random", seed=4020, visualization=True)
# note this will append two rows:
    # seed,player,num_rounds,risk,wealth,total_rent_paid,properties_owned,passed_go_count,neighborhood_completeness,loser
    # 4020,Player 1,11,0,210.7,31,4,1,0.0,2
    # 4020,Player 2,11,1,-50.0,50,5,1,0.0,2
# to "results/game_stats_random.csv" file
# and print out final game stats

# Load the decision tree model
with open('results/decision_tree_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Reminder what the features are
features = ['P1_neighborhood_completeness', 'P2_neighborhood_completeness',
       'P1_passed_go_count', 'P2_passed_go_count', 'P1_properties_owned',
       'P2_properties_owned', 'P1_risk', 'P2_risk', 'P1_total_rent_paid',
       'P2_total_rent_paid', 'num_rounds', 'is_English', 'is_Random', 'is_Vickrey']

# Demo of a decision with first line of data (from above):
dummy_data = pd.DataFrame([{
    'P1_neighborhood_completeness': 0,
    'P2_neighborhood_completeness': 0,
    'P1_passed_go_count': 1,
    'P2_passed_go_count': 1,
    'P1_properties_owned': 4,
    'P2_properties_owned': 5,
    'P1_risk': 0,
    'P2_risk': 1,
    'P1_total_rent_paid': 31,
    'P2_total_rent_paid': 51,
    'num_rounds': 11,
    'is_English': 0,
    'is_Random': 1,
    'is_Vickrey': 0
}])

# Make prediction
predicted_winner = loaded_model.predict(dummy_data)
predicted_probabilities = loaded_model.predict_proba(dummy_data)

# Print results
print(f"Predicted winner: Player {predicted_winner[0]}")
print(f"Prediction probabilities: {predicted_probabilities}")
print("Actual winner: Player 1")