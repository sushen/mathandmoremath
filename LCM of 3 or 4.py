print("enter tow numbers to calculate LCM")
a =int(input(":"))
b =int(input(":"))

for i in range (1, a*b +1):
    if i%a ==0 and i%b== 0:
        print(i)
        break
if (a>b):
    min1 = a
else:
    min1 = b
    while(1):
        if (min1%a==0 and min1%b==0):
            print(min1)
            break
            min1 = min1=1