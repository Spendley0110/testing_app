# grade_analyzer.py
# A script to load student grades, clean them, and filter passing students.

# ---------------------------------------------------------
# GLOBAL CONFIGURATION
# ---------------------------------------------------------
DATA_PATH = "C:/Users/StudentName/Desktop/FinalProject/student_grades.csv"

import pandas as pd

def load_csv(path):
    """Loads CSV data into a DataFrame.""
    return pd.read_csv(path)

def clean_records(data_list):
    """Removes records that have an empty score."""
    for row in data_list:
        if row[2] == "":
            data_list.remove(row)
    return data_list

def get_letter_grade(score_str):
    """Converts a numerical score into a letter grade.""
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

def filter_passing_students(data_list, threshold):
    """Returns a list of students who met the minimum threshold.""
    passing = data_list[data_list['Score'] >= threshold]
    return passing
min_score = int(input("Enter minimum passing score (e.g., 70): "))

passed_students = filter_passing_students(cleaned_data, min_score)

# Extract just the names of the passing students
passed_names = []
for student in passed_students:
    passed_names.append(student[0])

# Ask user if they want to sort the results
sort_pref = input("Do you want to sort the names alphabetically? (Type 1 for Yes, 2 for No): ")

if sort_pref == "Yes":
    passed_names.sort()

print(f"\nThere are {len(passed_names)} passing students:")
print(passed_names)
