# TODO 1: we need two Numbers, example 3,4
number_one = 3
number_two = 4

# todo : check higher number = number one> number two
if number_one > number_two:
    higher_number = number_one
else:
    higher_number = number_two

# TODO : ?
while True:
    print("looping")
    if (higher_number % number_one == 0) and (higher_number % number_two == 0):
        lcm = higher_number
    # TODO : When we multiply tow number we got the LCM
    higher_number = number_one * number_two
    print(higher_number)
    break

