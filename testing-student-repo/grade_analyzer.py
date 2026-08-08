# grade_analyzer.py
# A script to load student grades, clean them, and filter passing students.

# ---------------------------------------------------------
# GLOBAL CONFIGURATION
# ---------------------------------------------------------
DATA_PATH = "C:/Users/StudentName/Desktop/FinalProject/student_grades.csv"

import csv

def load_csv(path):
    """Loads CSV data into a list of lists."""
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        return [row for row in reader]
    return data

def clean_records(data_list):
    """Removes records that have an empty score."""
    return [row for row in data_list if row[2].strip() != '']

def get_letter_grade(score_str):
    """Converts a numerical score into a letter grade."""
    score = int(score_str)
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

def filter_passing_students(data_list, threshold):
    """Returns a list of students who met the minimum threshold."""
    passing = []
    for row in data_list:
        if int(row[2]) >= threshold:
            passing.append(row)
    return passing

# ---------------------------------------------------------
# SCRIPT EXECUTION
# ---------------------------------------------------------
# ---------------------------------------------------------
# SCRIPT EXECUTION
# ---------------------------------------------------------
print("--- Welcome to the Grade Analyzer ---")

try:
    raw_data = load_csv(DATA_PATH)
    cleaned_data = clean_records(raw_data)
except FileNotFoundError:
    print(f"Error: The file at {DATA_PATH} was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Get minimum passing score from the user
try:
    min_score = int(input("Enter minimum passing score (e.g., 70): "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

passed_students = filter_passing_students(cleaned_data, min_score)

# Extract just the names of the passing students
passed_names = [student[0] for student in passed_students]

# Ask user if they want to sort the results
sort_pref = input("Do you want to sort the names alphabetically? (Type 1 for Yes, 2 for No): ")

if sort_pref == '1':
    passed_names.sort()

print(f"\nThere are {len(passed_names)} passing students:")
print(passed_names)
print(passed_names)
