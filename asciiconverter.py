import json

# Read the JSON file
with open('data/training/0a938d79.json', 'r') as file:
    data = json.load(file)

# Extract the "train" array
train_array = data['train']

# Create and write to a .txt file
with open('train_elements.txt', 'w') as txt_file:
    for index, element in enumerate(train_array):
        txt_file.write(f"Element {index}: {element}\n")

# Read and print the contents of the .txt file
with open('train_elements.txt', 'r') as txt_file:
    print(txt_file.read())
