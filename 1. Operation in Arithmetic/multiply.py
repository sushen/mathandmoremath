"""
I make a simple calculator for multiply any number.
"""
num = int(input("Enter the number: 1\n"))
for i in range(1, 11):
    print(str(num) + "x" + str(i) + "= " + str(num*i))

"""
again it is a multiply calculator but this time using while loop
"""
i = 1
num1 = int(input("Enter the number: 2\n"))
while i<=10:
    print(f'{num1} x {i} = {num1*i}')
    i = i+1