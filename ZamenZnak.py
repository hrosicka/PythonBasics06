def zamen(slovo, pozice, novyZnak):
    """
        Funkce pro záměnu znaku ve slově

        Parametry:

        slovo - původní slovo

        pozice - pozice, na které se zaměňuje znak (počítáno od 1)

        novyZnak - znak, který bude použit místo původního

        """
    noveSlovo = slovo[:pozice] + novyZnak + slovo[(pozice + 1):]
    return noveSlovo
       
print("MĚNIČ PÍSMEN - FUNKCE")
print("---------------------")

slovo = input('Slovo: ')

while True:
            pozStr = input('Které písmeno zaměnit (počítá se od jedničky)? ')
            try:
                pozice = int(pozStr) - 1
                break
            except ValueError:
                print("Zadaná hodnota není číslo! Zkus to znovu", end = "!!\n") 

novyZnak = input('Nové písmeno (nebo skupina písmen): ')

noveSlovo = zamen(slovo, pozice, novyZnak)

print("Slovo {} se změnilo na slovo {}.".format(slovo.upper(), noveSlovo.upper()))


