
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Player': ['Rohit Sharma', 'Virat Kohli', 'KL Rahul', 'Suryakumar Yadav', 'Hardik Pandya',
               'Ravindra Jadeja', 'MS Dhoni', 'Jasprit Bumrah', 'Mohammad Shami', 'Kuldeep Yadav'],
    'Team': ['India'] * 10,
    'Runs_Scored': [120, 85, 45, 60, 30, 15, 5, 2, 0, 0],
    'Balls_Faced': [80, 70, 30, 40, 25, 12, 3, 4, 1, 1],
    'Fours': [10, 8, 5, 7, 3, 1, 0, 0, 0, 0],
    'Sixes': [5, 1, 2, 3, 1, 1, 0, 0, 0, 0],
}
df = pd.DataFrame(data)

print("## Imported Dataset (First 5 Rows):")
print(df.head())
print("-" * 50)

df['Strike_Rate'] = (df['Runs_Scored'] / df['Balls_Faced']) * 100

top_scorers = df.sort_values(by='Runs_Scored', ascending=False).head(5)

print("\n## Top 5 Batting Performance (Runs Scored):")
print(top_scorers[['Player', 'Runs_Scored', 'Balls_Faced', 'Strike_Rate']])
print("-" * 50)

plt.figure(figsize=(10, 6))

plt.bar(df['Player'], df['Runs_Scored'], color='skyblue')


plt.xlabel("Player", fontsize=12)
plt.ylabel("Runs Scored", fontsize=12)
plt.title("Player Runs Scored in the Match 🏏", fontsize=16, weight='bold')

plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

top_players_runs = top_scorers['Runs_Scored'].sum()
other_runs = df['Runs_Scored'].sum() - top_players_runs

pie_data = top_scorers['Runs_Scored'].tolist()
pie_labels = top_scorers['Player'].tolist()

pie_data.append(other_runs)
pie_labels.append('Others')

plt.figure(figsize=(8, 8))

plt.pie(
    pie_data,
    labels=pie_labels,
    autopct='%1.1f%%',       
    startangle=90,           
    shadow=True,
    explode=[0.1] + [0] * (len(pie_labels) - 1)  
)


plt.title("Percentage Run Contribution (Top 5 vs Others)", fontsize=14, weight='bold')
plt.axis('equal') 
plt.tight_layout()
plt.show()
