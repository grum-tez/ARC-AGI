

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

def convert_grid(array):
    ascii_art = ""
    for i, row in enumerate(array):
        ascii_art += "|"
        for num in row:
            ascii_art += mapping.get(num, ' ') + "|"
        if i < len(array) - 1:
            ascii_art += "\n" + "-" * (len(row) * 2 + 1) + "\n"  # Horizontal line to separate rows
    return ascii_art

def convert_back_grid(ascii_art):
    array = []
    rows = ascii_art.split("\n")
    for row in rows:
        if row.startswith("|"):
            row = row[1:]  # Remove leading '|'
        if row.endswith("|"):
            row = row[:-1]  # Remove trailing '|'
        if row.strip("-"):  # Ignore rows that are just horizontal lines
            array.append([reverse_mapping.get(char, 0) for char in row.split("|") if char])
    return array
