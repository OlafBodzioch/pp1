def f(dictionary,x,y):
    sum = 0
    for i in dictionary:
        for key in dictionary[i]:
            if key>=x and key<=y:
                sum+=key            
    return sum