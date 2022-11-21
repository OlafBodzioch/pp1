file = open(".\\07-FileHandling\\shopping.txt",'a',encoding='utf-8')

zakup = input("PODAJ: ")
file.write(zakup+"\n")

file.close()
