from turtle import exitonclick, bgcolor, screensize, title, setworldcoordinates
import turtle
import math
from domecek import domecek 

def vesnice(t, pocet, rozmer):
    """
    vykreslí vesnici
    
    t - želva
    
    pocet - počet domečků ve vesnici

    rozmer - délka dolní hrany domečku
    """

    if rozmer > 0 and pocet > 0:
        
        for x in range(pocet):
            pozice = x*80 + 2*rozmer
            t.goto(pozice, 0)
            domecek(t, rozmer)
            
    else:
        raise ValueError("Základna domečku a počet domů ve vesnici musí být kladné")


def main(): 

    # barva pozadí okna
    bgcolor("lightgray")
    # velikost okna
    screensize(250,250)
    # název okna
    title("Vesnice")

    # Vytvoříme novou želvu
    t = turtle.Turtle()
    
    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = slabý obrys
    t.pensize(2)

    #vykresleni vesnice
    t.penup()
    vesnice(t, 5, 30)

    # zavření okna
    exitonclick()

if __name__ == "__main__":
    main()