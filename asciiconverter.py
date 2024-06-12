import json
import os
import random
from altfunctions import convert_grid, convert_back_grid


# Define the mapping for numbers 1 to 9 with the specified swaps
mapping = {
    1: '*',
    2: '#',
    3: '@',
    4: '%',
    5: '&',
    6: 'O',
    7: '$',
    8: 'X',
    9: '~'
}

# Reverse mapping for converting ASCII art back to array
reverse_mapping = {v: k for k, v in mapping.items()}
reverse_mapping[' '] = 0  # Add this line to map spaces back to zeroes

# Function to convert array to ASCII art
def array_to_ascii_art(array):
    ascii_art = ""
    for i, row in enumerate(array):
        for num in row:
            ascii_art += mapping.get(num, ' ')  # Use ' ' (space) for any unmapped numbers
        if i < len(array) - 1:
            ascii_art += '\n'  # Newline at the end of each row except the last one
    return ascii_art

# Function to convert ASCII art back to array
def convert_back(ascii_art):
    array = []
    for line in ascii_art.split('\n'):
        row = []
        for char in line:
            row.append(reverse_mapping.get(char, 0))  # Use 0 for any unmapped characters
        array.append(row)
    
    # Ensure we correctly handle cases where lines are empty (completely zero rows)
    max_length = max(len(row) for row in array)
    for row in array:
        while len(row) < max_length:
            row.append(0)
    return array

def build_prompts(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    train_array = data['train']
    test_array = data['test']

    json_file_name = os.path.basename(json_file_path).replace('.json', '')

    os.makedirs('prompts', exist_ok=True)

    train_md_path = f'prompts/train_prompt_{json_file_name}.md'
    test_md_path = f'prompts/test_prompt_{json_file_name}.md'

    combined_md_path = f'prompts/combined_prompts_{json_file_name}.md'

    with open(train_md_path, 'w') as train_md_file, \
         open(test_md_path, 'w') as test_md_file, \
         open(combined_md_path, 'w') as combined_md_file:

        train_md_file.write("# Pattern recreation challenge\n\n")
        train_md_file.write("## Pattern examples\n\n")
        combined_md_file.write("# Pattern recreation challenge\n\n")
        combined_md_file.write("## Pattern examples\n\n")

        for index, element in enumerate(train_array):
            train_md_file.write(f"### Pattern example {index + 1}\n")
            train_md_file.write("#### Input\n")
            train_md_file.write("```ascii\n")
            train_md_file.write(convert_grid(element['input']))
            train_md_file.write("```\n\n")
            train_md_file.write("#### Output\n")
            train_md_file.write("```ascii\n")
            train_md_file.write(convert_grid(element['output']))
            train_md_file.write("```\n\n")

            combined_md_file.write(f"### Pattern example {index + 1}\n")
            combined_md_file.write("#### Input\n")
            combined_md_file.write("```ascii\n")
            combined_md_file.write(convert_grid(element['input']))
            combined_md_file.write("```\n\n")
            combined_md_file.write("#### Output\n")
            combined_md_file.write("```ascii\n")
            combined_md_file.write(convert_grid(element['output']))
            combined_md_file.write("```\n\n")

        for index, element in enumerate(test_array):
            test_md_file.write(f"## Challenge {index + 1}\n")
            test_md_file.write("### Input\n")
            test_md_file.write("```ascii\n")
            test_md_file.write(convert_grid(element['input']))
            test_md_file.write("```\n\n")

            combined_md_file.write(f"## Challenge {index + 1}\n")
            combined_md_file.write("### Input\n")
            combined_md_file.write("```ascii\n")
            combined_md_file.write(convert_grid(element['input']))
            combined_md_file.write("```\n\n")

        combined_md_file.write("\nReturn a single code block with the language indicated as ascii as your response\n")
