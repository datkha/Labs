import string


for letter in string.ascii_uppercase:
    path = (
        "/Users/datkha/Desktop/text"
        + letter
        + ".txt"
    )
    with open(path, "w") as my_file:
        my_file.write("Hello".format(path))