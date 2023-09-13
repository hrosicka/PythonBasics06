def anoNeboNe(otazka):
    """
    Vrátí true nebo false podle odpovědi
    """
    while True:
        odpoved = input(otazka).lower()
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False
        else:
            print("Nerozumim. Odpověz 'ano' nebo 'ne'.")


if anoNeboNe("Hraješ?"):
    print("OK!")
else:
    print("Tak nic.")
    