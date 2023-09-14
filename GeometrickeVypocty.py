from ObsahElipsy import obsahElipsy
from ObjemEliptickehoValce import objemEEliptickehoValce
from ObsahObdelnika import obsahObdelnika

def main():
    poloosaA = float(input('Zadej délku poloosy elipsy a: '))
    poloosaB = float(input('Zadej délku poloosy elipsy b: '))
    vyskaH = float(input('Zadej výšku eliptického válce h: '))
    vyskaH = 3

    obsah = round(obsahElipsy(poloosaA, poloosaB),3)
    print('Obsah elipsy s poloosami {} a {} je {}.'.format(poloosaA, poloosaB, obsah))

    obsahObd = round(obsahObdelnika(poloosaA, poloosaB))
    print('Obsah obdélníka o stranách o velikosti poloos {} a {} je {}.'.format(poloosaA, poloosaB, obsahObd))

    objem = round(objemEEliptickehoValce(poloosaA, poloosaB, vyskaH),3)
    print('Objem eliptického válce s poloosami {} a {} a výškou {} je {}.'.format(poloosaA, poloosaB, vyskaH, objem))

if __name__ == "__main__":
    main()

    