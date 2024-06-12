import json

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

# Function to convert array to ASCII art
def array_to_ascii_art(array):
    ascii_art = ""
    for row in array:
        for num in row:
            ascii_art += mapping.get(num, ' ')  # Use ' ' (space) for any unmapped numbers
        ascii_art += '\n'  # Newline at the end of each row
    return ascii_art

# Function to convert ASCII art back to array
def convert_back(ascii_art):
    array = []
    for line in ascii_art.strip().split('\n'):
        row = []
        for char in line:
            row.append(reverse_mapping.get(char, 0))  # Use 0 for any unmapped characters
        array.append(row)
    return array

# Read the JSON file
with open('data/training/0a938d79.json', 'r') as file:
    data = json.load(file)

# Extract the "train" array
train_array = data['train']

# Create and write to a .md file
with open('train_elements.md', 'w') as md_file:
    md_file.write("# Pattern recreation challenge\n\n")
    md_file.write("## Pattern examples\n\n")
    for index, element in enumerate(train_array):
        md_file.write(f"### Pattern example {index + 1}\n")
        md_file.write("#### Input\n")
        md_file.write("```ascii\n")
        md_file.write(array_to_ascii_art(element['input']))
        md_file.write("```\n\n")
        md_file.write("#### Output\n")
        md_file.write("```ascii\n")
        md_file.write(array_to_ascii_art(element['output']))
        md_file.write("```\n\n")

# Read and print the contents of the .md file
with open('train_elements.md', 'r') as md_file:
    print(md_file.read())

# Extract the "test" array
test_array = data['test']

# Create and write to a .md file
with open('recreate_this.md', 'w') as md_file:
    md_file.write("# Recreate this Pattern\n\n")
    for index, element in enumerate(test_array):
        md_file.write(f"## Challenge {index + 1}\n")
        md_file.write("### Input\n")
        md_file.write("```ascii\n")
        md_file.write(array_to_ascii_art(element['input']))
        md_file.write("```\n\n")

# Read and print the contents of the .md file
with open('recreate_this.md', 'r') as md_file:
    print(md_file.read())
