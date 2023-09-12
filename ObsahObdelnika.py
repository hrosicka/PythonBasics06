def obsahObdelnika(a, b):
    """
    Vypočítá obsah obdélníku

    a - strana a

    b - strana b

    S = a*b
    """
    obsah = a*b
    return obsah

stranaA = 2
stranaB = 3
obsah = obsahObdelnika(stranaA, stranaB)
print('Obsah obdélníka o stranách {} a {} je {}.'.format(stranaA, stranaB, obsah))


    