#program to print sum of odd numbers

num=int(input("Enter any number:"))
total=0
for value in range(1, num+1):
    if (value %2!=0):
        total=total+value

print("The sum of odd number is: {1} ".format(num, total))     
    
