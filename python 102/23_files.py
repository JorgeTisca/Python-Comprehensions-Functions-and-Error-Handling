# file = open("./text.txt", encoding="UTF-8")
# print(file.read())
# file.close()


# Best practice
with open("./text.txt", "r", encoding="UTF-8") as file:
    # print(file.readline())        #----print line for line
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.read())            #----print all file
    for line in file:
        print(line)
