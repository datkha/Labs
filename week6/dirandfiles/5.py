path = (
    "/Users/datkha/Desktop"
)


lst = [1, 2, 3, 4, 5]

with open(path, "w") as my_file:
    for item in lst:
        my_file.write(str(item) + "\n")