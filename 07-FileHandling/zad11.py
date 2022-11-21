film_titles = ["Scoby-doo", 'Scobby-doo 2', 'Scobbby-doo 3', 'Scobbby-doo IV', 'ScobbyDooV']

file = open(".\\07-FileHandling\\movie.txt",'w')

for i in range(len(film_titles)):
    file.write(film_titles[i]+"\n")

file.close()
