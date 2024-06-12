# Function to convert array to ASCII art with cell borders and row separators
def convert_grid(array):
    ascii_art = ""
    for i, row in enumerate(array):
        ascii_art += "|"
        for num in row:
            ascii_art += mapping.get(num, ' ') + "|"
        if i < len(array) - 1:
            ascii_art += "\n" + "---" * len(row) + "\n"  # Horizontal line to separate rows
    return ascii_art

# Function to convert ASCII art back to array with cell borders and row separators
def convert_back_grid(ascii_art):
    array = []
    rows = ascii_art.split("\n")
    for row in rows:
        if row.startswith("|"):
            row = row[1:]  # Remove leading '|'
        if row.endswith("|"):
            row = row[:-1]  # Remove trailing '|'
        array.append([reverse_mapping.get(char, 0) for char in row.split("|") if char])
    return array
