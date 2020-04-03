word_count = 0

file_name = "china1.txt"

with open(file_name, 'r') as file:
    for line in file:
        word_count += len(line.split())



