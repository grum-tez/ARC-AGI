import json

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
        md_file.write(f"{element['input']}\n\n")
        md_file.write("#### Output\n")
        md_file.write(f"{element['output']}\n\n")

# Read and print the contents of the .md file
with open('train_elements.md', 'r') as md_file:
    print(md_file.read())
