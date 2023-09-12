def napisHlasku(nazev, skore):
    """
    Popíše skóre

    nazev - přídavné jméno

    skore - dosažené skóre
    """
    print(nazev, 'skóre je', skore)
    if skore > 1000:
        print("Super!!! Jsi jednička!!!")
    elif skore > 100:
        print("Dobře ty!!!")
    elif skore > 0:
        print("Lepší než nic!!!")
    else:
        print("Příště to bude lepší!!!")

napisHlasku('Hančino', 200)
napisHlasku('Moničino', 2000)
napisHlasku('Lukášovo', 70)
napisHlasku('Markovo', -80)

    