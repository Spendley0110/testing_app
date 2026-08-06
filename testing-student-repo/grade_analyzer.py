# grade_analyzer.py
# A script to load student grades, clean them, and filter passing students.

# ---------------------------------------------------------
# GLOBAL CONFIGURATION
DATA_PATH = "student_grades.csv"

def load_csv(path):
import csv

def load_csv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        data = [row for row in reader]
    return data
    return data

def clean_records(data_list):
    return [row for row in data_list if row[2] != '']

def get_letter_grade(score_str):
    """Converts a numerical score into a letter grade."""
    score = int(score_str)
    if score >= 80:
        return "B"
    elif score >= 90:
        return "A"
    elif score >= 70:
        return "C"
    else:
        return "F"
def get_letter_grade(score_str):
    score = int(score_str)
    grades = {90: 'A', 80: 'B', 70: 'C'}
    for boundary, grade in grades.items():
        if score >= boundary:
            return grade
    return 'F'
# SCRIPT EXECUTION
# ---------------------------------------------------------
print("--- Welcome to the Grade Analyzer ---")

raw_data = load_csv(DATA_PATH)
cleaned_data = clean_records(raw_data)

# Get minimum passing score from the user
min_score = int(input("Enter minimum passing score (e.g., 70): "))
try:
    min_score = int(input("Enter minimum passing score (e.g., 70): "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()
passed_names = []
for student in passed_students:
    passed_names.append(student[0])

# Ask user if they want to sort the results
if sort_pref == '1':
    passed_names.sort()

print(f"\nThere are {len(passed_names)} passing students:")
print(passed_names)
