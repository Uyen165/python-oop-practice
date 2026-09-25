x = 1

def test():
    global x

    x = 10
    print(x)

    x = x + 5
    print(x)

test()
print(x)

test()
print(x)