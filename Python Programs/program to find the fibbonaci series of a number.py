#program to find the fibbonaci series of a number
fib=0
a=1
b=1
num=(int(input("enter the upper limit")))
print("fibbonacci series")
if(num==0):
 print("0")
else:
   for i in range(1,num+1):
    fib=fib+a
    a=b
    b=fib
    print(fib)