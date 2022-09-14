number_one = 3
number_two = 6

print(f"LTC : {number_one * number_two}")

number_one_multiplication_list = []
number_two_multiplication_list = []


for i in range(10):
    # print(f" i :{i + 1}")
    number_one_multiplication = i * number_one
    # print(f"one multiplication :{number_one_multiplication}")
    number_one_multiplication_list.append(number_one_multiplication)
    print(number_one_multiplication_list)

    number_two_multiplication = i * number_two
    # print(f"two multiplication :{number_two_multiplication}")
    number_two_multiplication_list.append(number_two_multiplication)
    print(number_two_multiplication_list)
    print(".................................")






