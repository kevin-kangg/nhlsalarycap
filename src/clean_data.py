"""
Clean the data, making sure all the names and columns are uniform

Author: Kevin Kang
"""

import pandas as pd

# --- Player Stats with Plus/Minus ---
# Load the player stats CSV file
player_stats_file_path = '../data/raw/player_stats_23_24.csv'  
df_player_stats = pd.read_csv(player_stats_file_path)

# Load the plus/minus values from the second CSV file
plus_minus_file_path = '../data/raw/players_plus_minus.csv'  
df_plus_minus = pd.read_csv(plus_minus_file_path)

# Rename specific player names in the plus-minus file
rename_dict = {
    'Mitch Marner': 'Mitchell Marner',
    'John (Jack) Roslovic': 'Jack Roslovic',
    'Alexander Wennberg': 'Alex Wennberg',
    'Cameron Atkinson': 'Cam Atkinson',
    'Janis Moser': 'J.J. Moser',
    'Patrick Maroon': 'Pat Maroon',
    'Jani Hakanp§§': 'Jani Hakanpää',
    'Mathew Dumba': 'Matt Dumba',
    'Matthew Grzelcyk': 'Matt Grzelcyk',
    'Joshua Brown': 'Josh Brown',
    'Gustav Lindstrom': 'Gustav Lindström',
    'Joshua Mahura': 'Josh Mahura',
    'Jesse Ylonen': 'Jesse Ylönen',
    'Zachary Sanford': 'Zach Sanford',
    'Jake Lucchini': 'Jacob Lucchini',
    'Matt Benning': 'Matthew Benning',
    'Maxime Lajoie': 'Max Lajoie',
    'Maxime Comtois': 'Max Comtois',
    'Alexander Petrovic': 'Alex Petrovic',
    'Matthew Savoie': 'Matt Savoie',
}

# Apply the renaming
df_plus_minus['Player'] = df_plus_minus['Player'].replace(rename_dict)

# Ensure the column names are consistent. Rename the +/- column to 'plus_minus' to avoid issues with special characters.
df_plus_minus = df_plus_minus.rename(columns={'+/-': 'plus_minus'})

# Merge the two datasets based on the 'Player' column to include the plus-minus values
merged_player_df = pd.merge(df_player_stats, df_plus_minus[['Player', 'plus_minus']], on='Player', how='left')

# Display the first few rows of the merged dataframe to verify
print("Player Stats with Plus/Minus:")
print(merged_player_df.head())

merged_player_file_path = '../data/cleaned/merged_player_stats_with_plus_minus.csv'
merged_player_df.to_csv(merged_player_file_path, index=False)

# --- Goalie Stats with Wins ---
# Load the goalie stats CSV file
goalie_stats_file_path = '../data/raw/goalie_stats_23_24.csv'  
df_goalie_stats = pd.read_csv(goalie_stats_file_path)

# Load the wins data from a separate CSV file (assuming it contains player names and wins)
wins_file_path = '../data/raw/goalie_wins_losses.csv'  
df_wins = pd.read_csv(wins_file_path)

# Ensure the column names are consistent. Rename the 'Wins' column to 'wins'
df_wins = df_wins.rename(columns={'W': 'wins'})

# Merge the two datasets based on the 'Player' column to include the wins values
merged_goalie_df = pd.merge(df_goalie_stats, df_wins[['Player', 'wins']], on='Player', how='left')

# Calculate win percentage and handle division by zero if a goalie has no games played
merged_goalie_df['win_percentage'] = (merged_goalie_df['wins'] / merged_goalie_df['GP'].replace(0, pd.NA)) * 100

# Display the first few rows of the merged dataframe to verify
print("\nGoalie Stats with Wins:")
print(merged_goalie_df.head())

merged_goalie_file_path = '../data/cleaned/merged_goalie_stats_with_wins.csv'
merged_goalie_df.to_csv(merged_goalie_file_path, index=False)

