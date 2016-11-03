def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
l=GCD(2,4)
print (l)
















