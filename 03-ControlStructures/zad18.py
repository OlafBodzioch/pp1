x = 33
piec = 0
dwa = 0
jeden = 0

while x is not 0:
    if x>=5:
        piec=x//5
        x=x%5
    elif x>=2:
        dwa=x//2
        x=x%2
    elif x>=1:
        jeden=x
    
print(x)
print(f"Piec: {piec}, Dwa: {dwa}, Jeden: {jeden}")
        

        ##dokonczyc!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!