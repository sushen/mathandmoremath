def lcm(a, b):
    i = 1
    if a > b:
        c = a
        d = b
    else:
        c = b
        d = a
    while True:
        if ((c * i) / d).is_integer():
            return c * i
        i += 1;


print(lcm(10, 12))
