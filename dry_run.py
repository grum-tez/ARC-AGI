import json
import os
import random
import sys
import datetime
from asciiconverter import array_to_ascii_art, build_prompts, convert_grid
from altfunctions import add_borders

def compare_answers(json_file_path):
    with open('prompts/correct_answer', 'r') as correct_file:
        correct_answer = correct_file.read().strip()
    with open('prompts/your_answer', 'r') as your_answer_file:
        your_answer = your_answer_file.read().strip()
    
    if correct_answer == your_answer:
        print("Correct!")
    else:
        print("Incorrect")

RUN_LOGS_FILE = 'run_logs.json'

def save_last_run(json_file_path, correct=None):
    history = []
    if os.path.exists(RUN_LOGS_FILE):
        try:
            with open(RUN_LOGS_FILE, 'r') as log_file:
                data = json.load(log_file)
                history = data.get("history", [])
        except (json.JSONDecodeError, IOError):
            history = []

    run_object = {
        "timestamp": datetime.datetime.now().isoformat(),
        "json_file": json_file_path,
        "correct": correct
    }
    history.insert(0, run_object)
    with open(RUN_LOGS_FILE, 'w') as log_file:
        json.dump({"last_run": json_file_path, "history": history}, log_file)

def get_last_run():
    if os.path.exists(RUN_LOGS_FILE):
        with open(RUN_LOGS_FILE, 'r') as log_file:
            try:
                data = json.load(log_file)
                return data.get("last_run"), data.get("history", [])
            except (json.JSONDecodeError, IOError):
                return None, []
    return None

training_folder = 'data/training'
json_files = [f for f in os.listdir(training_folder) if f.endswith('.json')]

grid = False
borders = True
json_file_path = None

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == "r":
        random_json_file = random.choice(json_files)
        json_file_path = os.path.join(training_folder, random_json_file)
    elif arg == "nogrid":
        grid = False
        json_file_path = sys.argv[2] if len(sys.argv) > 2 else None
    elif arg == "borders":
        borders = True
        json_file_path = sys.argv[2] if len(sys.argv) > 2 else None

if not json_file_path:
    last_run, history = get_last_run()
    if last_run and os.path.exists(last_run):
        json_file_path = last_run
    else:
        random_json_file = random.choice(json_files)
        json_file_path = os.path.join(training_folder, random_json_file)

# Save the last run without the "correct" field initially
save_last_run(json_file_path, correct=None)

# Print the name of the chosen JSON file
print(f"Chosen JSON file: {os.path.basename(json_file_path)}")

# Load the JSON data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Locate the test array and count the number of elements
test_array = data['test']
num_elements = len(test_array)
print(f"Number of elements in the test array: {num_elements}")

# Take the first element in the test array
first_element = test_array[0]

# Convert the input matrix to ASCII and print it
input_ascii = convert_grid(first_element['input']) if grid else array_to_ascii_art(first_element['input'])
input_dimensions = f"{len(first_element['input'])}x{len(first_element['input'][0])}"
if borders:
    input_ascii = add_borders(input_ascii)
print("Input matrix in ASCII:")
print(input_ascii)
print(f"Input dimensions: {input_dimensions}")

# Convert the output matrix to ASCII and print it
output_ascii = convert_grid(first_element['output']) if grid else array_to_ascii_art(first_element['output'])
output_dimensions = f"{len(first_element['output'])}x{len(first_element['output'][0])}"
if borders:
    output_ascii = add_borders(output_ascii)
print("Output matrix in ASCII:")
print(output_ascii)
print(f"Output dimensions: {output_dimensions}")


# Ensure the prompts directory exists
os.makedirs('prompts', exist_ok=True)

# Write the correct test output to "prompts/correct_answer" file
correct_output_ascii = convert_grid(first_element['output']) if grid else array_to_ascii_art(first_element['output'])
if borders:
    correct_output_ascii = add_borders(correct_output_ascii)
with open('prompts/correct_answer', 'w') as correct_file:
    correct_file.write(correct_output_ascii)

# Create an empty "prompts/your_answer" file
with open('prompts/your_answer', 'w') as your_answer_file:
    pass
print(f"Saving last run to {RUN_LOGS_FILE}")

build_prompts(json_file_path, grid=grid, border=borders)

# Ask the user if they would like to check their answer
check_answer = input("Would you like to check your answer? (yes/no): ").strip().lower()
if check_answer == 'yes':
    correct = compare_answers(json_file_path)
    # Update the last run with the correct field
    save_last_run(json_file_path, correct)

# Ask the user if they would like to check their answer
check_answer = input("Would you like to check your answer? (yes/no): ").strip().lower()
if check_answer == 'yes':
    compare_answers()
