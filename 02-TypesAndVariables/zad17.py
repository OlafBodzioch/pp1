from math import floor

x = input("State height in cm. ")
x = int(x)
feet = floor(x*0.0328)
xx = x-(feet/0.0328)
inch = round(xx*0.3937,2)

print(f"I am {x}cm tall, i.e. {feet} feet and about {inch} inches")