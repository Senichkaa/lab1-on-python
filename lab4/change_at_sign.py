with open("art_symbol_at_sign.txt", 'r') as input_file, open("art_symbol_hash", 'w') as output_file:
    modified_lines = [line.replace('@', '#') for line in input_file]
    output_file.writelines(modified_lines)
