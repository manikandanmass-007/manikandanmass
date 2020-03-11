#program to find a num is prime number or not
i=2
num=(int(input("enter the number...")))
while (i<=num-1):
    if(num%i==0):
         print("the given number is not a prime number")
         break
    i=i+1
if(i==num):
    print("the given number is a prime number")