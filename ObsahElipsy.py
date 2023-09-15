from math import pi

def obsahElipsy(a, b):
    """
    Vypočítá obsah elipsy

    a - poloosa a

    b - poloosa b

    S = pi*a*b
    """
    if a > 0 and b > 0:
        obsah = pi*a*b
        return obsah
    else:
        raise ValueError("Poloosa musí být kladná")

def main():
    poloosaA = 2
    poloosaB = 3
    obsah = round(obsahElipsy(poloosaA, poloosaB),3)
    print('Obsah elipsy s poloosami {} a {} je {}.'.format(poloosaA, poloosaB, obsah))

if __name__ == "__main__":
    main()
    