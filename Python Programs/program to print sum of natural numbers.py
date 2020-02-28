#program to print dsum of natural numbers

num=int(input("Enter any number:"))
total=0
for value in range(1, num+1):
    total=total+value

print("The sum of natural number is: {1} ".format(num, total))     
    
