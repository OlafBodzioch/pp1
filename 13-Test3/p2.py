def f(arr):
    x = True
    for j in range(1, len(arr[0])):
        for i in range(1, len(arr)):
            if (arr[i][j]) != (arr[0][j]*(i+1)):
                x = False
                break
    return x


print(f([[1,2,3],[2,4,6],[3,6,9]]))
print(f([[1,2],[2,4]])) 
print(f([[1,2],[3,6]]))
print(f([[1,2,3],[2,4,6]]))