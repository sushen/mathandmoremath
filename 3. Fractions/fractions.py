"""
proper fraction
"""
fraction = (100/1000)
print(fraction)

"""
improper fraction
"""
im_fraction = (1000/100)
print(im_fraction)

"""
Rasel picked (X) mangoes from their trees.
Total (Y) members are there in his family.
Now he will divide these mangoes among all his family members.
"""
X = int(input("How many members are there in his family: : "))
Y = int(input("How many mangoes he picked: "))
print(f'Form {Y} part of Mangoes every family members get {X/Y} part.')
print("This is the proper fractions.\n")

"""
equivalent fraction.
"""
a = int(input("Enter the numerator of fractions 1: "))
b = int(input("Enter the denominator of fractions 1: "))
c = int(input("Enter the number (x) numerator  'this number must be not zero': "))
d = int(input("Enter the number (X) denominator 'this number must be not zero': "))
eq_fraction_1 = (a/b)
eq_fraction_2 = ((a*c)/(b*d))
if (eq_fraction_1 == eq_fraction_2):
    print("This is a equivalent fractions.")
else:
    print("This is not a equivalent fractions.")



