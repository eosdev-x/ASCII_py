# Define table headers
headers = ["Decimal", "Hexadecimal", "Binary", "Octal", "Char"]
divider = "+---------+-------------+---------+-------+---------------+"

# Function to generate ASCII data
def generate_ascii_data(start, end):
    ascii_data = []
    for i in range(start, end + 1):
        decimal = i
        hexadecimal = hex(i)[2:].upper()  # Remove '0x' and convert to uppercase
        binary = bin(i)[2:]  # Remove '0b'
        octal = oct(i)[2:]  # Remove '0o'
        char = chr(i) if 32 <= i <= 126 else "Non-printable" if i < 32 or i > 126 else chr(i)
        ascii_data.append([decimal, hexadecimal, binary, octal, char])
    return ascii_data

# Generate ASCII data for the characters
ascii_data = generate_ascii_data(0, 127)

# Calculate maximum width for each column
max_widths = [max(len(header), max(len(str(cell)) for cell in column)) for header, column in zip(headers, zip(*ascii_data))]
for row in ascii_data:
    for i, cell in enumerate(row):
        max_widths[i] = max(max_widths[i], len(str(cell)))

# Print the table headers
print(divider)
header_row = "| " + " | ".join(header.ljust(max_widths[i]) for i, header in enumerate(headers)) + " |"
print(header_row)
print(divider)

# Print the ASCII data with proper formatting
for row in ascii_data:
    formatted_row = "| " + " | ".join(str(cell).ljust(max_widths[i]) for i, cell in enumerate(row)) + " |"
    print(formatted_row)
print(divider)