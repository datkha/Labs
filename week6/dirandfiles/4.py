path = "/Users/datkha/Desktop/text.txt"

try:
    with open(path) as my_file:
        line_count = sum(1 for line in my_file)
    print(line_count)
except FileNotFoundError:
    print("File not found")