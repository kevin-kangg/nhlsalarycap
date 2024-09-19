"""
Output of optimized team by salary and performance

Author: Kevin Kang
"""

import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Load the combined data
merged_df = pd.read_csv('../data/processed/merged_player_goalie_cps_and_salaries.csv')

# Clean the 'cap_hit' column: remove non-numeric characters and convert to float
merged_df['cap_hit'] = merged_df['cap_hit'].replace({'\$': '', ',': ''}, regex=True)
merged_df['cap_hit'] = pd.to_numeric(merged_df['cap_hit'], errors='coerce')

# Ensure no NaN values in 'cap_hit' and 'cps'
merged_df['cap_hit'].fillna(0, inplace=True)
merged_df['cps'].fillna(0, inplace=True)

# Define constants
salary_cap = 83.5e6  # Salary cap in dollars
forwards_needed = 12
defensemen_needed = 6
goalies_needed = 2

# Create a maximization problem
problem = LpProblem("NHL_Salary_Cap_Optimization", LpMaximize)

# Create binary decision variables for each player
player_vars = LpVariable.dicts("Player", merged_df.index, cat="Binary")

# Objective: Maximize total CPS
problem += lpSum(player_vars[i] * merged_df.loc[i, 'cps'] for i in merged_df.index), "Maximize_CPS"

# Salary cap constraint
problem += lpSum(player_vars[i] * merged_df.loc[i, 'cap_hit'] for i in merged_df.index) <= salary_cap, "Salary_Cap"

# Positional constraints
problem += lpSum(player_vars[i] for i in merged_df.index if merged_df.loc[i, 'Position'] in ['C', 'L', 'R']) == forwards_needed, "Forwards_Limit"
problem += lpSum(player_vars[i] for i in merged_df.index if merged_df.loc[i, 'Position'] == 'D') == defensemen_needed, "Defensemen_Limit"
problem += lpSum(player_vars[i] for i in merged_df.index if merged_df.loc[i, 'Position'] == 'G') == goalies_needed, "Goalies_Limit"

# Solve the problem
problem.solve()

# Extract selected players
selected_players = []
for i in merged_df.index:
    if player_vars[i].varValue == 1:
        selected_players.append({
            'Player': merged_df.loc[i, 'player'],
            'Position': merged_df.loc[i, 'Position'],
            'CPS': merged_df.loc[i, 'cps'],
            'Cap Hit': merged_df.loc[i, 'cap_hit']
        })

# Convert selected players to a DataFrame
selected_df = pd.DataFrame(selected_players)

# Debug: check total cap hit of selected players
total_cap_hit = selected_df['Cap Hit'].sum()
print(f"Total Cap Hit of Selected Players: {total_cap_hit}")

# Display the selected players
print(selected_df)

# Save the selected team to a CSV file
selected_df.to_csv('../result/optimized_team.csv', index=False)