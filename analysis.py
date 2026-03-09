import numpy as np
import pandas as pd

# Load the dataset from the text file
data = pd.read_csv('dataset.txt', sep='\t', skipinitialspace=True)

# Clean column names (remove extra whitespace)
data.columns = data.columns.str.strip()

# Use the Math and Turkish columns from the dataset
math_scores = data['MATEMATIK']
turkish_scores = data['TURKCE']

# Create a DataFrame with the two subjects
scores = pd.DataFrame({
    'Math': math_scores,
    'Turkish': turkish_scores
})

# Calculate the correlation between Math and Turkish scores
correlation_value = scores['Math'].corr(scores['Turkish'])

# Calculate the difference between Math and Turkish for each student
differences = scores['Math'] - scores['Turkish']
average_difference = differences.mean()

# Print the results
print("Correlation between Math and Turkish scores:", correlation_value)
print("Average difference between Math and Turkish:", average_difference)
