#program to print even numbers from 1 to 100

start=int(input("enter the starting value:"))
end=int(input("enter the ending value:"))
for i in range(start, end+1):

    if i%2==0:
        print(i, end = " ")
