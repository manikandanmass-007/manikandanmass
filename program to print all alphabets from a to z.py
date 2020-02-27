# program to print all alphabets from a to z

print("Alphabets from a to z are : ")

# ascii values for a= 97 and z = 123
for alphabets_up in range(97, 123):
    print(chr(alphabets_up), end=" ")
print ("\nAlphabets from A to Z are :")    
for alphabets_low in range(65, 90):
    print (chr(alphabets_low), end=" ")
