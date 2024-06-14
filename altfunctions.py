
def add_top_border(ascii_art):
    rows = ascii_art.split("\n")
    width = len(rows[0])
    top_border = "_" * (width - 2)
    return f"{top_border}\n{ascii_art}"

def add_bottom_border(ascii_art):
    rows = ascii_art.split("\n")
    width = len(rows[0])
    bottom_border = "‾" * (width)
    return f"{ascii_art}\n{bottom_border}"

def remove_top_border(ascii_art):
    rows = ascii_art.split("\n")
    return "\n".join(rows[1:])

def remove_bottom_border(ascii_art):
    rows = ascii_art.split("\n")
    return "\n".join(rows[:-1])

def add_left_border(ascii_art):
    rows = ascii_art.split("\n")
    bordered_rows = [f"_{rows[0]}_"] + [f"|{row}" for row in rows[1:-1]] + [f"‾{rows[-1]}‾"]
    return "\n".join(bordered_rows)

def add_right_border(ascii_art):
    rows = ascii_art.split("\n")
    bordered_rows = [f"_{rows[0]}_"] + [f"{row}|" for row in rows[1:-1]] + [f"‾{rows[-1]}‾"]
    return "\n".join(bordered_rows)

def remove_left_border(ascii_art):
    rows = ascii_art.split("\n")
    bordered_rows = [row[1:] if row.startswith("|") else row for row in rows]
    return "\n".join(bordered_rows)

def remove_right_border(ascii_art):
    rows = ascii_art.split("\n")
    bordered_rows = [row[:-1] if row.endswith("|") else row for row in rows]
    return "\n".join(bordered_rows)

def add_borders(ascii_art):
    ascii_art = add_top_border(ascii_art)
    ascii_art = add_bottom_border(ascii_art)
    ascii_art = add_left_border(ascii_art)
    ascii_art = add_right_border(ascii_art)
    return ascii_art

def remove_borders(ascii_art):
    ascii_art = remove_right_border(ascii_art)
    ascii_art = remove_left_border(ascii_art)
    ascii_art = remove_bottom_border(ascii_art)
    ascii_art = remove_top_border(ascii_art)
    return ascii_art

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
        for j, num in enumerate(row):
            ascii_art += mapping.get(num, ' ')
            if j < len(row) - 1:
                ascii_art += "|"
        if i < len(array) - 1:
            if len(row) > 1:
                ascii_art += "\n" + "-" + "-".join(["+"] * (len(row) - 1)) + "-" + "\n"  # Horizontal line to separate rows
            else:
                ascii_art += "\n" + "-" + "\n"  # Horizontal line for single column
    return ascii_art

def convert_back_grid(ascii_art):
    array = []
    rows = ascii_art.split("\n")
    for row in rows:
        # if row.startswith("|"):
        #     row = row[1:]  # Remove leading '|'
        # if row.endswith("|"):
        #     row = row[:-1]  # Remove trailing '|'
        if "+" not in row:  # Ignore rows that are just horizontal lines
            array.append([reverse_mapping.get(char, 0) for char in row.split("|") if char])
    return array
