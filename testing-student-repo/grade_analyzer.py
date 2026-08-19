# grade_analyzer.py
# A script to load student grades, clean them, and filter passing students.

# ---------------------------------------------------------
# GLOBAL CONFIGURATION
# ---------------------------------------------------------
DATA_PATH = "student_grades.csv"

def load_csv(path):
    """Loads CSV data into a list of lists."""
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    
    data = []
    # Skip the header row
    for line in lines[1:]:
        # Expecting format: Name, ID, Score
            row = [field.strip() for field in line.strip().split(',')] 
        data.append(row)
    
    return data

def clean_records(data_list):
    """Removes records that have an empty score."""
        if row[2] == "":
            continue
        cleaned_data.append(row)
    return data_list

def get_letter_grade(score_str):
    """Converts a numerical score into a letter grade."""
    score = int(score_str)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

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
print("--- Welcome to the Grade Analyzer ---")

raw_data = load_csv(DATA_PATH)
cleaned_data = clean_records(raw_data)

# Get minimum passing score from the user
min_score = int(input("Enter minimum passing score (e.g., 70): "))

passed_students = filter_passing_students(cleaned_data, min_score)

# Extract just the names of the passing students
passed_names = []
for student in passed_students:
    passed_names.append(student[0])

# Ask user if they want to sort the results
    sort_pref = input("Do you want to sort the names alphabetically? (Type 1 for Yes, 2 for No): ")

    if sort_pref == "1":
        passed_names.sort()

print(f"\nThere are {len(passed_names)} passing students:")
print(passed_names)
