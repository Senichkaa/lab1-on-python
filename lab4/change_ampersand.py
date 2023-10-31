with open("art_symbol_percent.txt", 'r') as input_file, open("art_symbol_ampersand", 'w') as output_file:
    modified_lines = [line.replace('%', '&') for line in input_file]
    output_file.writelines(modified_lines)