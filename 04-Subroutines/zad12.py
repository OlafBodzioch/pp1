def sum(n):
    if n>=1:
        return n+sum(n-1)
    else:
        return 0

x = 10
print(sum(x))