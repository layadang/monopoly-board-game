import pandas as pd
files_to_clean =["./results/game_stats_english.csv", "./results/game_stats_random.csv", "./results/game_stats_vickrey.csv"]
new_directory = "clean_results/"


def remove_seed_column(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if 'seed' column exists and remove it
    if 'seed' in df.columns:
        df = df.drop(columns=['seed'])
    
    # New file path to save the cleaned data
    # Renaming the file to mark as cleaned and moving to a new directory
    new_file_path = file_path.replace('.csv', '_cleaned.csv')
    new_file_path = file_path.replace('results/',new_directory)
        
    # Save the modified DataFrame back to the CSV file
    df.to_csv(new_file_path, index=False)
    
    print(f"Seed column removed from {file_path}")

def remove_player_column(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if 'player' column exists and remove it
    if 'player' in df.columns:
        df = df.drop(columns=['player'])
    
    # New file path to save the cleaned data
    # Renaming the file to mark as cleaned and moving to a new directory

    new_file_path = file_path.replace('.csv', '_cleaned.csv')
    new_file_path = file_path.replace('results/', new_directory)
        
    # Save the modified DataFrame back to the CSV file
    df.to_csv(new_file_path, index=False)
    
    print(f"Player column removed from {file_path}, saved to {new_file_path}")
    
def remove_duplicates(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # New file path to save the cleaned data
    # Renaming the file to mark as cleaned and moving to a new directory
    new_file_path = file_path.replace('.csv', '_cleaned.csv')
    new_file_path = file_path.replace('results/', new_directory)
        
    # Save the modified DataFrame back to the CSV file
    df.to_csv(new_file_path, index=False)
    
    print(f"Duplicates removed from {file_path}, saved to {new_file_path}")

def remove_loser_column(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if 'loser' column exists and remove it
    if 'loser' in df.columns:
        df = df.drop(columns=['loser'])
    
    # New file path to save the cleaned data
    # Renaming the file to mark as cleaned and moving to a new directory
    new_file_path = file_path.replace('.csv', '_cleaned.csv')
    new_file_path = file_path.replace('results/', new_directory)
        
    # Save the modified DataFrame back to the CSV file
    df.to_csv(new_file_path, index=False)
    
    print(f"Loser column removed from {file_path}, saved to {new_file_path}")


def remove_num_rounds_column(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if 'num_rounds' column exists and remove it
    if 'num_rounds' in df.columns:
        df = df.drop(columns=['num_rounds'])
    
    # New file path to save the cleaned data
    # Renaming the file to mark as cleaned and moving to a new directory
    new_file_path = file_path.replace('.csv', '_cleaned.csv')
    new_file_path = file_path.replace('results/', new_directory)
        
    # Save the modified DataFrame back to the CSV file
    df.to_csv(new_file_path, index=False)
    
    print(f"num_rounds column removed from {file_path}, saved to {new_file_path}")


def one_hot_encode(file_path, column_name_1, column_name_2):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # One-hot encode the column
    df = pd.get_dummies(df, columns=[column_name_1, column_name_2])
    
    # New file path to save the cleaned data
    # Renaming the file to mark as cleaned and moving to a new directory
    new_file_path = file_path.replace('.csv', '_encoded.csv')
    new_file_path = file_path.replace('results/', new_directory)
        
    # Save the modified DataFrame back to the CSV file
    df.to_csv(new_file_path, index=False)
    
    print(f"One-hot encoded {column_name_1} and {column_name_2} columns in {file_path}, saved to {new_file_path}")



"""
Options:
1. Remove seed column
2. Remove player column
3. Remove duplicates
4. Remove loser column
5. Remove num_rounds column
6. One-hot encode columns

"""

if __name__ == '__main__':
    # Mark which cleaning options to use
    seed = True
    player = True
    duplicates = True
    loser = True
    num_rounds = True
    
    remove_duplicates(files_to_clean[0])
    
    for file in files_to_clean:
        if seed:
            remove_seed_column(file)
        if player:
            remove_player_column(file)
        if duplicates:
            remove_duplicates(file)
        if loser:
            remove_loser_column(file)
        if num_rounds:
            remove_num_rounds_column