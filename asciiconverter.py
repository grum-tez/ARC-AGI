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

# Function to convert array to ASCII art
def array_to_ascii_art(array):
    ascii_art = ""
    for row in array:
        for num in row:
            ascii_art += mapping.get(num, ' ')  # Use ' ' (space) for any unmapped numbers
        ascii_art += '\n'  # Newline at the end of each row
    return ascii_art

# The given array
array = [
    [2, 2, 2],
    [2, 1, 8],
    [2, 8, 8]
]

# Convert to ASCII art
ascii_art = array_to_ascii_art(array)
print(ascii_art)
