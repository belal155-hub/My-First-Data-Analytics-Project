a = 0
b = 1
for i in range(10):
    print(a)

    next_number = a + b

    a = b
    b = next_number


def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

for i in range(0, 10):
    print(F(i))