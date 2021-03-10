
def fast_exp(a, e, m):
    r = 1
    if 1 & e:
        r = a
    while e:
        e >>= 1
        a = (a * a) % m
        if e & 1: r = (r * a) % m
    return r




### testing purposes only ####
def test():
    a = int(input("Enter a:"))
    e = int(input("Enter e:"))
    m = int(input("Enter m:"))
    r = fast_exp(a, e, m)
    print("{} ^ {} ≡ {} (mod {})".format(a, e, r, m))





