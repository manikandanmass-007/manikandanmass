#program to find biggest of 3 numbers

x=(int(input("enter the first number:")))
y=(int(input("enter the second number:")))
z=(int(input("enter the third number:")))
if x<y and x>z:
    print(x)
elif y>z and y>x:
    print(y)
else:  
    print(z)