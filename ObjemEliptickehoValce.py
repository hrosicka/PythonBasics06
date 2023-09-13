from ObsahElipsy import obsahElipsy

def objemEEliptickehoValce(a, b, h):
    """
    Vypočítá objem eliptick0ho válce

    a - poloosa a

    b - poloosa b

    h - výška válce

    V = pi*a*b*h
    """
    objem = obsahElipsy(a, b)*h
    return objem

def main():
    poloosaA = 2
    poloosaB = 3
    vyskaH = 3
    objem = round(objemEEliptickehoValce(poloosaA, poloosaB, vyskaH),3)
    print('Objem eliptického válce s poloosami {} a {} a výškou {} je {}.'.format(poloosaA, poloosaB, vyskaH, objem))

if __name__ == "__main__":
    main()

    