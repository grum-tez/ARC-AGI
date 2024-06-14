import json
import os
import random
from altfunctions import convert_grid, convert_back_grid, add_borders


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

def build_prompts(json_file_path, grid=True, border=False):
    import shutil

    # Delete the prompts folder if it exists
    if os.path.exists('prompts'):
        shutil.rmtree('prompts')
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    train_array = data['train']
    test_array = data['test']

    json_file_name = os.path.basename(json_file_path).replace('.json', '')

    # Recreate the prompts folder
    os.makedirs('prompts', exist_ok=True)

    train_md_path = f'prompts/train_prompt_{json_file_name}.md'
    test_md_path = f'prompts/test_prompt_{json_file_name}.md'

    combined_md_path = f'prompts/combined_prompts_{json_file_name}.md'

    with open(train_md_path, 'w') as train_md_file, \
         open(test_md_path, 'w') as test_md_file, \
         open(combined_md_path, 'w') as combined_md_file:

        train_md_file.write("# ascii pattern recreation challenge\n\n")
        train_md_file.write("all the following ascii grid patterns are visual artworks within rectangular grid canvases, and therefore  MUST BE viewed with a monospaced font. This allows for the patterns, and the transformations from inputs to outputs, to be understood\n\n")
        train_md_file.write("## Pattern examples\n\n")
        combined_md_file.write("# ascii pattern recreation challenge\n\n")
        combined_md_file.write("all the following ascii grid patterns are visual artworks within rectangular grid canvases, and therefore  MUST BE viewed with a monospaced font. This allows for the patterns, and the transformations from inputs to outputs, to be understood\n\n")
        combined_md_file.write("Rules govern the transformation of the input patterns into the output patterns. Your task is to understand these rules so that you can create a new output from a given challenge input.\n\n")
        combined_md_file.write("## Pattern examples\n\n")

        for index, element in enumerate(train_array):
            train_md_file.write(f"### Pattern example {index + 1}\n")
            input_art = convert_grid(element['input']) if grid else array_to_ascii_art(element['input'])
            input_dimensions = f"{len(element['input'])}x{len(element['input'][0])}"
            output_art = convert_grid(element['output']) if grid else array_to_ascii_art(element['output'])
            output_dimensions = f"{len(element['output'])}x{len(element['output'][0])}"
            
            train_md_file.write("#### Input\n")
            train_md_file.write(f"input canvas size: {input_dimensions}\n")
            train_md_file.write("```ascii\n")
            input_art = convert_grid(element['input']) if grid else array_to_ascii_art(element['input'])
            output_art = convert_grid(element['output']) if grid else array_to_ascii_art(element['output'])
            if border:
                input_art = add_borders(input_art)
                output_art = add_borders(output_art)
            train_md_file.write(input_art)
            train_md_file.write("```\n\n")

                
            train_md_file.write("#### Output\n")
            train_md_file.write(f"output canvas size: {output_dimensions}\n")
            train_md_file.write("```ascii\n")
            train_md_file.write(output_art)
            train_md_file.write("```\n\n")

            combined_md_file.write(f"### Pattern example {index + 1}\n")
            combined_md_file.write("#### Input\n")
            combined_md_file.write(f"input canvas size: {input_dimensions}\n")
            combined_md_file.write("```ascii\n")
            combined_md_file.write(input_art)
            combined_md_file.write("```\n\n")
            combined_md_file.write("#### Output\n")
            combined_md_file.write(f"output canvas size: {output_dimensions}\n")
            combined_md_file.write("```ascii\n")
            combined_md_file.write(output_art)
            combined_md_file.write("```\n\n")

        train_md_file.write("### Output\n")
        train_md_file.write("\nYour response must be strictly within this canvas.\n\n")

        combined_md_file.write("### Output\n")
        combined_md_file.write("\nYour response must be strictly within this canvas.\n\n")

        output_dimensions = None
        for index, element in enumerate(test_array):
            output_art = convert_grid(element['output']) if grid else array_to_ascii_art(element['output'])
            output_dimensions = f"{len(element['output'])}x{len(element['output'][0])}"
            test_md_file.write(f"## Challenge {index + 1}\n")
            input_art = convert_grid(element['input']) if grid else array_to_ascii_art(element['input'])
            input_dimensions = f"{len(element['input'])}x{len(element['input'][0])}"
            
            test_md_file.write("### Input\n")
            test_md_file.write(f"input canvas size: {input_dimensions}\n")
            test_md_file.write("```ascii\n")
            input_art = convert_grid(element['input']) if grid else array_to_ascii_art(element['input'])
            if border:
                input_art = add_borders(input_art)
            test_md_file.write(input_art)
            test_md_file.write("```\n\n")

            combined_md_file.write(f"## Challenge {index + 1}\n")
            combined_md_file.write("### Input\n")
            combined_md_file.write(f"input canvas size: {input_dimensions}\n")
            combined_md_file.write("```ascii\n")
            combined_md_file.write(input_art)
            combined_md_file.write("```\n\n")

        # Add example "output canvas" with an empty bordered canvas
        empty_canvas = [[" " for _ in range(len(test_array[0]['output'][0]))] for _ in range(len(test_array[0]['output']))]
        empty_canvas_art = array_to_ascii_art(empty_canvas)
        if border:
            empty_canvas_art = add_borders(empty_canvas_art)
        empty_canvas_dimensions = f"{len(empty_canvas)}x{len(empty_canvas[0])}"

        test_md_file.write("### Output Canvas\n")
        test_md_file.write("\nYour response must be strictly within this canvas.\n")
        test_md_file.write(empty_canvas_art)
        test_md_file.write("\n\n")

        combined_md_file.write("### Output Canvas\n")
        combined_md_file.write("\nYour response must be strictly within this canvas.\n")
        combined_md_file.write(empty_canvas_art)
        combined_md_file.write("\n\n")

        combined_md_file.write("\nProduce a single code block with the language indicated as ascii as your response. Then reflect on that code block. Reason aloud. Consider how both how it does, and does not reflect the examples you were given. Then make a final attempt, again produce a single code block with the language indicated as ascii as your response.\n")

    # Write the correct test output to "prompts/correct_answer" file
    correct_output_ascii = convert_grid(test_array[0]['output']) if grid else array_to_ascii_art(test_array[0]['output'])
    if border:
        correct_output_ascii = add_borders(correct_output_ascii)
    correct_answer_path = 'prompts/correct_answer'
    with open(correct_answer_path, 'w') as correct_file:
        correct_file.write(correct_output_ascii)

    # Create an empty "prompts/your_answer" file
    your_answer_path = 'prompts/your_answer'
    with open(your_answer_path, 'w') as your_answer_file:
        pass
