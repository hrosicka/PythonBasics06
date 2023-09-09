def zamen(slovo, pozice, novyZnak):
    """
        Funkce pro záměnu znaku ve slově

        Parametry:

        slovo - původní slovo

        pozice - pozice, na které se zaměňuje znak (počítáno od 1)

        novyZnak - znak, který bude použit místo původního

        Return:

        nove slovo, kde je na dané pozici zaměněn znak

        """
    noveSlovo = slovo[:pozice] + novyZnak + slovo[(pozice + 1):]
    return noveSlovo


def nacti():
    """
        Funkce načte slovo, pořadí znaku pro výměnu a nový znak

        Return:

        tuple

        slovo - původní slovo

        pozice - pozice, na které měníme

        novyZnak - znak nebo skupina znaků, který se použijí místo původního
        """
    slovo = input('Slovo: ')

    while True:
                pozStr = input('Které písmeno zaměnit (počítá se od jedničky)? ')
                try:
                    pozice = int(pozStr) - 1
                    break
                except ValueError:
                    print("Zadaná hodnota není číslo! Zkus to znovu", end = "!!\n") 

    novyZnak = input('Nové písmeno (nebo skupina písmen): ')
    return (slovo, pozice, novyZnak)
      
       
print("MĚNIČ PÍSMEN - FUNKCE")
print("---------------------")

zamena1 = nacti()
slovo = zamena1[0]
pozice = zamena1[1]
novyZnak = zamena1[2]

noveSlovo = zamen(slovo, pozice, novyZnak)

print("Slovo {} se změnilo na slovo {}.".format(slovo.upper(), noveSlovo.upper()))


