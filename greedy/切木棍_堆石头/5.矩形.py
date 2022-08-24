def rectangle():
    n = int(input())
    c = 0
    if n % 2 == 1:
        print(c)
    else:
        for a in range(1, int(n / 2)):
            b = n / 2 - a
            if a < b and a != b:
                c += 1
        print(c)


rectangle()
