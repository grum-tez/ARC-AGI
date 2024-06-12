# Recreate this Pattern

## Challenge 1
### Input
```ascii
# Read the JSON file
with open('data/training/0a938d79.json', 'r') as file:
    data = json.load(file)

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
