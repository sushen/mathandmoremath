add_number = 0, 2, 4, 6, 8

numbers_power = 5**5, 8**2, 9**3, 7**5

square_number = 5**2, 8**2, 10**2

qube_number = 2**3, 8**3, 5**3, 29**3, 78**3
print(qube_number)

number_square_root = 4**0.5, 16**0.5

sum_square_rout= (8*2)**0.5, (9*2)**0.5, (5**2)**0.5

#number_quabe_root
number = int(input("enter your number:"))
for i in range (0,number):
    if i**3 == number:
        print(i)
        break
    elif i == number-1 and i**3 != number:
        print("not root")


factor_number =10
    print("factor of",factor_number,"is:")
for i in range (1,factor_number+1):
    if factor_number%i == 0:
        print(i)