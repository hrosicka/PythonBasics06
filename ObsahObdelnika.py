def obsahObdelnika(a, b):
    """
    Vypočítá obsah obdélníku

    a - strana a

    b - strana b

    S = a*b
    """
    if a > 0 and b > 0:
        obsah = a*b
        return obsah
    else:
        raise ValueError("Strana musí být kladná")

def main():
    stranaA = 2
    stranaB = 3
    obsah = obsahObdelnika(stranaA, stranaB)
    print('Obsah obdélníka o stranách {} a {} je {}.'.format(stranaA, stranaB, obsah))

if __name__ == "__main__":
    main()


    