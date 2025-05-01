with open("file1.txt", 'r') as file:
    count = sum(1 for line in file) # or len(file.readlines())
    print("{}{}".format("Total number of lines: ", count))