from random import randint, random


class Arrays():

    import random

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    def create(amount, value):
        arr=[]
        for i in range(0, amount):
            list.append(arr, value)
        return arr

    def generate(amount, min, max):
        arr=[]
        for i in range(0, amount):
            list.append(arr, randint(min,max))
        return arr
        
    def check(array, min, max):
        count = 0
        for i in range(0, len(array)):
            if array[i]>=min and array[i]<=max:
                count +=1
        return count
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)

print(Arrays.create(7,11))

print(Arrays.generate(5,9,33))

print(Arrays.check(my_array,1,7))
