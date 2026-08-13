# grade_analyzer.py
# A script to load student grades, clean them, and filter passing students.

# ---------------------------------------------------------
# GLOBAL CONFIGURATION
# ---------------------------------------------------------
DATA_PATH = "student_grades.csv"

import pandas as pd
def load_csv(path):
    \"\"\"Loads CSV data into a DataFrame.\"\"\"
    return pd.read_csv(path)

def clean_records(data_df):
    \"\"\"Removes records that have an empty score.\"\"\"
    return data_df.dropna(subset=['Score'])

def get_letter_grade(score_str):
    \"\"\"Converts a numerical score into a letter grade.\"\"\"
    try:
        score = int(score_str)
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'F'
    except ValueError:
        return 'Invalid Score'

def filter_passing_students(data_df, threshold):
    \"\"\"Returns a list of students who met the minimum threshold.\"\"\"
    return data_df[data_df['Score'] >= threshold]

# ---------------------------------------------------------
# SCRIPT EXECUTION
# ---------------------------------------------------------
print("--- Welcome to the Grade Analyzer ---")

raw_data = load_csv(DATA_PATH)
cleaned_data = clean_records(raw_data)

# Get minimum passing score from the user
min_score = int(input("Enter minimum passing score (e.g., 70): ")) if input("Enter minimum passing score (e.g., 70): ").isdigit() else 70

passed_students = filter_passing_students(cleaned_data, min_score)

# Extract just the names of the passing students
passed_names = []
for student in passed_students:
    passed_names.append(student[0])

# Ask user if they want to sort the results
sort_pref = input("Do you want to sort the names alphabetically? (Type y for Yes, n for No): ")
if sort_pref.lower() == 'y':
    passed_names.sort()
    passed_names.sort()

print(f"\nThere are {len(passed_names)} passing students:")
print(passed_names)
