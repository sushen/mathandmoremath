"""
I make a simple calculator for multiply any number.
"""
num = int(input("Enter the number\n"))
for i in range(1, 11):
    print(str(num) + "x" + str(i) + "= " + str(num*i))