"""
LCM of any number.
"""
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
i = max(number_one, number_two)
while True:
    if (i%number_one==0 and i%number_two==0):
        break
    i = i + 1
print(f"The LCM of {number_one} and {number_two} is: {i}\n")
"""
This number is prime or not.
"""
number = int(input("Enter the number: "))
prime = True
for number in range (2,number):
    if number%number == 0:
        prime = False
if prime:
    print("This is prime number.")
else:
    print("This is not a prime number.")