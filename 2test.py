def odometer(x):
    y = [x[i] for i in range(len(x)) if i % 2 == 0]
    z = [x[i] for i in range(len(x)) if i % 2 != 0]
    z.insert(0, 0)
    f = 0
    for i in range(len(y)):
        f += y[i] * (z[i + 1] - z[i])
    return(f)

