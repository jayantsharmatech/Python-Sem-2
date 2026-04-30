import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setting seed for reproducibility
np.random.seed(42)

# Generate Synthetic Data
n_students = 50
subjects = ['Math', 'Science', 'English', 'History']

data = {
    'StudentID': range(101, 101 + n_students),
    'Math': np.random.randint(40, 100, n_students),
    'Science': np.random.randint(35, 100, n_students),
    'English': np.random.randint(50, 100, n_students),
    'History': np.random.randint(45, 100, n_students)
}

df = pd.DataFrame(data)

# Calculate Total Score and Average
df['Total Score'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1)
