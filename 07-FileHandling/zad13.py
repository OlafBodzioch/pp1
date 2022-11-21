with open(".\\07-FileHandling\\plik13.txt","r") as f:
    for line in f:
        print(line, end="")
    f.close()
