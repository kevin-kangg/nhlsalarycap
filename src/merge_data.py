"""
Merge cps data with salary data

Author: Kevin Kang
"""

import pandas as pd
import datetime

# Get today's date in the desired format (YYYY-MM-DD)
today = datetime.datetime.today().strftime('%Y-%m-%d')

# Load salary data using today's date in the file path
salary_file_path = f'../data/raw/all_player_contract_data_{today}.csv'
salary_df = pd.read_csv(salary_file_path)

# Load combined CPS data for both skaters and goalies
combined_cps_df = pd.read_csv('../data/processed/cps/combined_player_goalie_cps.csv')

# Rename the columns to match (standardize to 'player' for both)
combined_cps_df.rename(columns={'Player': 'player'}, inplace=True)
salary_df.rename(columns={'name': 'player'}, inplace=True)

# Create a dictionary of name mappings (e.g., nicknames or slight variations)
name_corrections = {
    'Mitch Marner': 'Mitchell Marner',
    'John (Jack) Roslovic': 'Jack Roslovic',
    'Alexander Wennberg': 'Alex Wennberg',
    'Cameron Atkinson': 'Cam Atkinson',
    'Janis Moser': 'J.J. Moser',
    'Patrick Maroon': 'Pat Maroon',
    'Jani Hakanpää': 'Jani Hakanpää',
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
    'Matthew Savoie': 'Matt Savoie'
}

# Replace names in the 'player' column of both DataFrames
combined_cps_df['player'] = combined_cps_df['player'].replace(name_corrections)
salary_df['player'] = salary_df['player'].replace(name_corrections)

# Remove duplicate rows from each DataFrame before merging
combined_cps_df = combined_cps_df.drop_duplicates(subset='player')  # Remove duplicates based on 'player'
salary_df = salary_df.drop_duplicates(subset='player')  # Remove duplicates based on 'player'

# Merge the two DataFrames on the 'player' column
merged_df = pd.merge(combined_cps_df, salary_df, on='player')

# Remove duplicates from the merged DataFrame if any exist
merged_df = merged_df.drop_duplicates()

# Display the first few rows of the merged dataset
print(merged_df.head())

# Save the merged DataFrame to a CSV file
output_file_path = '../data/processed/merged_player_goalie_cps_and_salaries.csv'
merged_df.to_csv(output_file_path, index=False)


