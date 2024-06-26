import json
import os
import random
import sys
import datetime
from asciiconverter import array_to_ascii_art, build_prompts, convert_grid, add_rank_file
from altfunctions import add_borders

def compare_answers(json_file_path):
    with open('prompts/correct_answer', 'r') as correct_file:
        correct_answer = correct_file.read().strip()
    with open('prompts/your_answer', 'r') as your_answer_file:
        your_answer = your_answer_file.read().strip()
    
    correct = correct_answer == your_answer
    if correct:
        print("Correct!")
    else:
        print("Incorrect")
    
    # Update the run log with the result
    save_last_run(json_file_path, correct)
    return correct

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

grid = True
borders = True
json_file_path = None

import argparse

# Argument parsing
parser = argparse.ArgumentParser(description="Run the dry run task on a specified JSON file.")
parser.add_argument("-j", "--json", help="Specify the JSON file name without extension.")
parser.add_argument("-r", "--random", action="store_true", help="Select a random JSON file.")
parser.add_argument("--nogrid", action="store_true", help="Disable grid conversion.")
parser.add_argument("--borders", action="store_true", help="Enable borders.")
args = parser.parse_args()

if args.json:
    json_file_path = os.path.join(training_folder, f"{args.json}.json")
elif args.random:
    random_json_file = random.choice(json_files)
    json_file_path = os.path.join(training_folder, random_json_file)
elif args.nogrid:
    grid = False
    json_file_path = sys.argv[2] if len(sys.argv) > 2 else None
elif args.borders:
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
    correct_output_ascii = add_rank_file(correct_output_ascii)
    correct_output_ascii = add_borders(correct_output_ascii)
with open('prompts/correct_answer', 'w') as correct_file:
    correct_file.write(correct_output_ascii)

# Create an empty "prompts/your_answer" file
with open('prompts/your_answer', 'w') as your_answer_file:
    pass
print(f"Saving last run to {RUN_LOGS_FILE}")

build_prompts(json_file_path, grid=grid, border=borders)

# Prompt the user to press enter when they are ready to check their answer
input("Press enter when you are ready to check your answer: ")

# Check if the "your_answer" file is empty
your_answer_path = 'prompts/your_answer'
if os.path.getsize(your_answer_path) == 0:
    print("your_answer file is empty")
else:
    correct = compare_answers(json_file_path)
    if correct:
        print("correct")
    else:
        print("incorrect")
