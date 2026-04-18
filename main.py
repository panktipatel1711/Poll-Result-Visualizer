import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Synthetic Data (Banavati Data) Generate Karna
# Sochiye ki humne ek poll kiya: "Aapki favourite Programming Language konsi hai?"
data = {
    'Language': ['Python', 'Java', 'JavaScript', 'Python', 'C++', 'Python', 'Java', 
                 'JavaScript', 'Python', 'JavaScript', 'C++', 'Python', 'Java'],
    'User_Type': ['Student', 'Student', 'Professional', 'Professional', 'Student', 
                  'Professional', 'Student', 'Professional', 'Student', 'Student', 
                  'Professional', 'Professional', 'Professional']
}

# Data ko Table (DataFrame) mein badalna
df = pd.DataFrame(data)

# 2. Data Analysis (Counting votes)
vote_counts = df['Language'].value_counts()
print("--- Poll Results Summary ---")
print(vote_counts)

# 3. Visualization (Graph Banana)
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Bar Chart banana
sns.barplot(x=vote_counts.index, y=vote_counts.values, palette="viridis")

plt.title('Poll Results: Favourite Programming Language', fontsize=15)
plt.xlabel('Programming Language', fontsize=12)
plt.ylabel('Number of Votes', fontsize=12)

# Graph ko save karna
plt.savefig('poll_results.png')
print("\nSuccess! Aapka graph 'poll_results.png' ke naam se save ho gaya hai.")

# Graph ko screen par dikhana
plt.show()