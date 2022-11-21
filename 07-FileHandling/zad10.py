file = open(".\\07-FileHandling\\writ.txt",'w')

name = input("WPROWADZ IMIE:")
surname = input("WPROWADZ NAZWISKO:")
uni_name = "UEK"
field = "Applied Informatics"

file.write(name+"\n"+surname+"\n"+uni_name+"\n"+field)

file.close()
