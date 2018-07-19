import better_exceptions

def test(x, y):
    return sub_test(x + y -3)

def sub_test(z):
    return 1/z

test(1, 2)
