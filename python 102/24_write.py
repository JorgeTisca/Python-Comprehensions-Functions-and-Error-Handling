with open("./text.txt", "r+", encoding="UTF-8") as file:
    print(file.read())  # ----print all file
    file.write("new things in file \n")
    file.write("extra line \n")
