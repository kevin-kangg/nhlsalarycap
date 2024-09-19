# NHL Salary Cap Optimization Project

## Project Overview

The **NHL Salary Cap Optimization** project aims to construct an optimal NHL roster under the league's salary cap limit. The goal is to maximize team performance by selecting players based on key performance metrics such as goals, assists, points, and more, while adhering to salary cap constraints.

### Project Goal:
To build an optimal roster under the NHL salary cap limit by maximizing player performance, balancing salary, and player roles (forwards, defensemen, goalies).

### Key Objectives:
- Gather player salary and performance data.
- Optimize player selection using performance metrics and salary constraints.
- Build an optimal roster using linear programming techniques.

---

## Steps and Process

### 1. Data Collection
We collected player salary and performance data from the following sources:
- **Spotrac**: Player salary data including cap hit and contract information.
- **Natural Stat Trick & nhl.com/stats**: Player performance metrics such as goals, assists, points, and other advanced stats.

#### Data Points Collected:
- **Player Name**
- **Team**
- **Position** (Forward, Defenseman, Goalie)
- **Age**
- **Salary (Cap Hit)**
- **Contract Duration**
- **Performance Metrics** (Goals, Assists, Points, etc.)

### 2. Performance Metric Selection
We selected key performance metrics for player evaluation, including:
- **Goals (G)**
- **Assists (A)**
- **Points (P)**
- **Expected Goals (xG)**
- **Corsi (CF)**

Additionally, we developed a **Custom Performance Score (CPS)**, which combines several metrics to assess player performance across different positions. For goalies, the CPS incorporates metrics such as save percentage (SV%), goals against average (GAA), and more.

### 3. Optimization Setup
We implemented the optimization using Python's linear programming tools such as **PuLP** or **SciPy**.

#### Steps:
1. **Define the Objective**: Maximize the selected performance metric (e.g., CPS or total points).
2. **Set Constraints**:
   - Salary cap limit: The total salary of selected players must not exceed the NHL salary cap.
   - Roster structure: Ensure a balanced roster with the required number of forwards, defensemen, and goalies.
3. **Optimization**:
   - Build and solve a linear programming model that maximizes the performance metric while respecting the constraints.

### 4. Output
The output of the optimization model is an **optimized NHL roster**, which includes the best possible combination of players while staying within the salary cap. The selected roster maximizes performance metrics based on the provided data.

---

## Files and Resources

- **`all_player_contract_data.csv`**: Contains player salary and contract data.
- **`player_cps.csv`**: Custom Performance Score (CPS) data for skaters.
- **`goalie_cps.csv`**: CPS data for goalies.
- **`combined_player_goalie_cps.csv`**: Combined CPS data for skaters and goalies.
- **`merged_player_goalie_cps_and_salaries.csv`**: Final merged dataset with CPS and salary data.
- **Optimization Code**: Python scripts for data collection, processing, and optimization using linear programming.

---

## Tools and Libraries

- **Python**: Programming language used for data processing, analysis, and optimization.
- **Pandas**: Library for handling data manipulation and analysis.
- **SciPy / PuLP**: Libraries used for linear programming and optimization.
- **BeautifulSoup/Requests**: For web scraping player salary and performance data.
- **MinMaxScaler (Sklearn)**: For normalizing performance metrics in CPS calculation.

---

## How to Run the Project

1. **get_data**: Gather all the necessary player salary and performance data by scraping Spotrac for salary information and NHL's stats section for player performance metrics.
2. **clean_data**: Standardize and clean the dataset, ensuring player names and column formats are consistent across all sources.
3. **integrate_data**: Calculate the Custom Performance Score (CPS) for both skaters and goalies using the cleaned performance data.
4. **merge_data**: Combine the CPS data with the salary data to create a comprehensive dataset for analysis.
5. **analyze_data**: Apply the linear programming model to generate an optimized NHL roster, maximizing performance while adhering to salary cap constraints.

---

## Future Improvements

- **Advanced Metrics**: Incorporate more advanced stats like zone entries, puck possession, and defensive metrics.
- **Dynamic Cap Changes**: Allow for flexibility in salary cap changes based on upcoming seasons or trade scenarios.
- **User Interaction**: Develop a user interface where users can input different roster constraints and see real-time optimization results.

---

This project allows for efficient roster management and provides insights into how player performance and salary constraints impact the overall effectiveness of an NHL team.

