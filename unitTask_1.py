def substract(a,b):
    c = a - b
    if c < 0:
        return False
    if c >= 0:
        return True


def check_in(a,b):
    c = a - b
    d = list(range(a+b))
    return c, d


def check_grater(a,b):
    c = a + b
    return c


def check_count(a, b):
    c = list(range(a))
    d = list(range(b))
    return c, d




