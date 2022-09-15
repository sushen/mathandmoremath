# TODO 1: we need two Numbers, example 3,4
number_one = 3
number_two = 4

# todo : check higher number = number one> number two
if number_one > number_two:
    higher_number = number_one
else:
    higher_number = number_two

# TODO : ? বড় সংখ্যাটিকে ছোটটি দিয়ে ভাগ করলে যদি ভাগশেষ 0 হয় তাহলে বড় সংখাটি ল সা গু..
# todo: তাই বড় সংখাটিকে প্রথম এবং দ্বিতিয় নাম্বারটি দিয়ে ভাগ করি যদি ভাগশেষ 0 না হয় তবে দুটি সংখাকে গুন করে দেই।
while True:
    print("looping")
    if (higher_number % number_one == 0) and (higher_number % number_two == 0):
        lcm = higher_number
    # TODO : When we multiply tow number we got the LCM
    higher_number = number_one * number_two
    print(higher_number)
    break

