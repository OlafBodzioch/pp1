def f(array2D):
    arr = []
    for i in range (0, len(array2D)):
        for j in range (0, len(array2D[0])):
            arr.append(array2D[i][j])
    return arr          