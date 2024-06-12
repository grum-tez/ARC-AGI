import json

# Read the JSON file
with open('data/training/0a938d79.json', 'r') as file:
    data = json.load(file)

# Extract the "train" array
train_array = data['train']

# Iterate through each element of the "train" array and print it
for element in train_array:
    print(element)
