'''
how many prim number are insite 1 to 1000
'''

prime_number = []


for num in range (1, 1000):
    if num>1:
        for i in range (2, num):
            if (num % i) ==0:
                break
        else:
            print(num)
            prime_number.append(num)

print(prime_number)
print(len(prime_number))
