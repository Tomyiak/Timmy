def ff(x, f):   # x - число в десятичной    f - система счисления
    alf = '0123456789ABCDEFGH'
    r = ''
    while x != 0:
        r = alf[x%f] + r
        x //= f
    return r


print(ff(42, 2))

print()