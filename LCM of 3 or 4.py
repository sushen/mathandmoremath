# TODO 1: we need two Numbers, example 8,9
# todo : cake higher number = number one> number two
# todo: the higher number is one
# todo : or higher number is two
# todo : higher number reminds number one result = 0
# todo : higher number reminds number two result = 0
# todo lcm = higher number
# todo : higher number = number one * number two


number_one = int(input("Enter any number:"))
number_two = int(input("Enter any number:"))
if number_one >number_two:
    higher_number = number_one
else:
    higher_number = number_two
while True:
    if ((higher_number % number_one == 0) and (higher_number % number_two == 0)):
        lcm = higher_number
        break
    higher_number = number_one*number_two
print(lcm)

