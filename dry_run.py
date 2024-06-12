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

# Run build_prompts on the chosen JSON file
build_prompts(json_file_path)
