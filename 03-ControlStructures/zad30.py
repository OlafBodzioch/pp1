x = int(input("Proszę wprowadzić ilość. "))
i = 0
num = 2
flag = 0

while i<x:

    if num==2:
        print(num)
        i=i+1
        num=num+1
    else:
        flag = 0
        for z in range(2, num-1):
            if num%z==0:
                num = num +1
                flag = 1
        if flag != 1: 
            print(num)
            num=num+1
            i=i+1