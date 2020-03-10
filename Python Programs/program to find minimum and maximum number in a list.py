#program to find minimum and maximum number in a list

list1=[]
print("enter the upper limit....")
n=int(input())
print("enter the number")
for i in range (0,n):
   a=int(input())
   list1.append(a)
maxno=list1[0]
minno=list1[0]
for i in range (len(list1)):
       if list1[i]>maxno:
           maxno=list1[i]
       if list1[i]<minno:
           minno=list1[i]
print("maximum number of the list1:",maxno)
print("minimum number of the list1:",minno)