import json
import os
import random
from asciiconverter import array_to_ascii_art, build_prompts

# Get a random JSON file from the training folder
training_folder = 'data/training'
json_files = [f for f in os.listdir(training_folder) if f.endswith('.json')]
random_json_file = random.choice(json_files)
json_file_path = os.path.join(training_folder, random_json_file)

# Print the name of the chosen JSON file
print(f"Chosen JSON file: {random_json_file}")

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
input_ascii = array_to_ascii_art(first_element['input'])
print("Input matrix in ASCII:")
print(input_ascii)

# Convert the output matrix to ASCII and print it
output_ascii = array_to_ascii_art(first_element['output'])
print("Output matrix in ASCII:")
print(output_ascii)
