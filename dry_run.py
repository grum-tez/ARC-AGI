import json
import os
import random
import sys
from asciiconverter import array_to_ascii_art, build_prompts, convert_grid

RUN_LOGS_FILE = 'run_logs.json'

def save_last_run(json_file_path):
    with open(RUN_LOGS_FILE, 'w') as log_file:
        json.dump({"last_run": json_file_path}, log_file)

def get_last_run():
    if os.path.exists(RUN_LOGS_FILE):
        with open(RUN_LOGS_FILE, 'r') as log_file:
            data = json.load(log_file)
            return data.get("last_run")
    return None

training_folder = 'data/training'
json_files = [f for f in os.listdir(training_folder) if f.endswith('.json')]

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == "r":
        random_json_file = random.choice(json_files)
        json_file_path = os.path.join(training_folder, random_json_file)
    else:
        json_file_path = arg
else:
    last_run = get_last_run()
    if last_run and os.path.exists(last_run):
        json_file_path = last_run
    else:
        random_json_file = random.choice(json_files)
        json_file_path = os.path.join(training_folder, random_json_file)

save_last_run(json_file_path)

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
input_ascii = convert_grid(first_element['input'])
print("Input matrix in ASCII:")
print(input_ascii)

# Convert the output matrix to ASCII and print it
output_ascii = convert_grid(first_element['output'])
print("Output matrix in ASCII:")
print(output_ascii)

# Run build_prompts on the chosen JSON file
print(f"Saving last run to {RUN_LOGS_FILE}")
build_prompts(json_file_path)
