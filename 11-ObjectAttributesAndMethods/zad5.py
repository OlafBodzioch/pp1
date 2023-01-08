class Music():
    
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return(f"ARTIST: \t{self.artist}\n TITLE: \t{self.title}\n ALBUM: \t{self.album}\n YEAR: \t\t{self.year}\n")

file1 = Music("Pendulum", "Slam", "Hold your Color", 2007)
file2 = Music("Meydad Tasa", "Gadol Hashem", "Gadol Hashem", 2011)
file3 = Music("Infected Mushroom", "Becoming Insane", "Vicious Delicious", 2008)

print(file1)
print(file2)
print(file3)