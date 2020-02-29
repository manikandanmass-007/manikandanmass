#program to swap first and last digit in a list

lis=[]
n= int(input("Enter the number of elements in list:"))

for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    lis.append(element)

temp=lis[0]
lis[0]=lis[n-1]
lis[n-1]=temp
print("New list is:")
print(lis)
