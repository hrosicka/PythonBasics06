from math import pi

def obsahElipsy(a, b):
    """
    Vypočítá obsah elipsy

    a - poloosa a

    b - poloosa b

    S = pi*a*b
    """
    obsah = pi*a*b
    return obsah

poloosaA = 2
poloosaB = 3
obsah = round(obsahElipsy(poloosaA, poloosaB),3)
print('Obsah elipsy s poloosami {} a {} je {}.'.format(poloosaA, poloosaB, obsah))


    