import json
from asciiconverter import array_to_ascii_art

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
