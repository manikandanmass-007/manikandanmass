print("--MENU--");
print("1 ADDITION");
print("2 SUBTRACTION");
print("3 MULTIPLICATOIN");
print("4 DIVISION");
print("0 EXIT");
n=int(input("enter your choice:"))
if (n<=9 and n>0):
 a=int(input("enter the first number:"))
 b=int(input("enter the second number:"))
 c=int(input("enter the third number:"))
if n==1:
  d=a+b+c
  print("ADDITION:",d)
elif n==2:
    d=a-b-c
    print("SUBTRACTION:",d)
elif n==3:
       c=a*b
       print("MULTIPLICATION:",c)
elif n==4:
           c=a/b
           print("DIVISION",c)
           print("invalid option")