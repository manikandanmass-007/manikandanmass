#program for product of a given number

num = int(input("Enter any number : "))

temp = num
product = 1;

while(temp != 0):
    product = product * (temp % 10);
    temp = int(temp / 10)

print("\nProduct of all digits in", num, ":", product)
