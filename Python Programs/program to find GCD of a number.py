#program to find GCD of a number
n1=int(input("enter the number n1:"))
n2=int(input("enter the number n2:"))
rem=n1%n2
while rem!=0:
  n1=n2
  n2=rem
  rem=n1%n2
print ("gcd of given numbers is:",n2)