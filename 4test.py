def MadMax(n, tele):
    tele.sort()
    x = tele[ : (n // 2)]
    y = tele[(n // 2) : ]
    y.sort(reverse = True)
    z = x + y
    return(z)




