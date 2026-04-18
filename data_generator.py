import pandas as pd
import random
from datetime import datetime, timedelta

# Synthetic Poll Data generate karne ke liye script
languages = ['Python', 'Java', 'JavaScript', 'C++', 'R', 'Go']
user_types = ['Student', 'Professional', 'Researcher']
regions = ['North', 'South', 'East', 'West']

data_list = []

for i in range(1, 101):  # 100 responses generate karenge
    data_list.append({
        'Respondent_ID': i,
        'Timestamp': datetime.now() - timedelta(days=random.randint(0, 30)),
        'Language': random.choice(languages),
        'User_Type': random.choice(user_types),
        'Region': random.choice(regions),
        'Satisfaction': random.randint(1, 5)
    })

df = pd.DataFrame(data_list)
df.to_csv('data/poll_data.csv', index=False)
print("✅ 100 entries wala data/poll_data.csv file ban gaya hai!")