for n in range(1, 101):
    count = 0
    for ii in range(1, n + 1):
        if n % ii == 0:
            count += 1
    if count == 2:  # A prime number has exactly two divisors: 1 and itself
        print(n)
