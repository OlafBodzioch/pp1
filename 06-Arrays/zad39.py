def f(arr):
    
    for i in range(1, len(arr[0])+1):
        arr[0][i-1]=i
    
    for i in range(1, len(arr[0])):
        for j in range(0, len(arr)):
            arr[i][j]=arr[0][j]*(i+1)
    
    return arr


arr = [[0 for i in range(5)] for j in range(5)]

for i in range(len(arr)):
    print(f(arr)[i])