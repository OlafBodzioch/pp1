def f(arr):
    x = len(arr)
    y = len(arr[0])
    count = 0

    arr2 = [[] for i in range(x*y)]

    #arr2 = 0-5
    #x 0-1
    #y 0-2

    count = 0

    while count<x*y:
        for i in range(x):
            for j in range(y):
                arr2[count]=arr[i][j]
                count = count + 1
                
    return arr2
    
arr = [[1,2],[3,4],[5,6],[5,11],[33,7]]
print(f(arr))