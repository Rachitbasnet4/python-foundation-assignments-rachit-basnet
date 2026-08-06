'''
Exercise 2: Data Quality Checker
Student: Rachit Basnet
Day: 1
'''

# Input Values
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# Calculate total problematic rows
problematic_rows = missing_rows + duplicate_rows

# Calculate the percentage of problematic rows
problem_percentage = (problematic_rows / total_rows) * 100

# Classify data quality based on the problem percentage
# 0% - 2%   : Excellent
# Above 2% - 5% : Acceptable
# Above 5%  : Needs Cleaning
if problem_percentage <= 2:
    classification = 'Excellent'
elif problem_percentage <= 5:
    classification = "Acceptable"
else:
    classification = "Needs Cleaning"

# Display the results
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problem percentage: {problem_percentage}%")
print(f"Final classification: {classification}")
