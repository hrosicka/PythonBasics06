from turtle import exitonclick, bgcolor, screensize, title, setworldcoordinates
import turtle
import math

def domecek(t, rozmer):
    """vykreslí domeček
    
    t - želva
    
    rozmer - délka dolní hrany domečku
    
    po vykleslení se želva vrátí do pozice 0,0"""

    if rozmer > 0:
        t.pendown()

        for _ in range(4):
            t.forward(rozmer)
            t.left(90)
        
        t.left(45)
        t.forward(math.sqrt(2*math.pow(rozmer,2)))

        t.right(135)
        t.penup()
        t.forward(rozmer)

        t.right(135)
        t.pendown()
        t.forward(math.sqrt(2*math.pow(rozmer,2)))

        t.right(90)
        t.forward(math.sqrt(2*math.pow(rozmer,2))/2)

        t.right(90)
        t.forward(math.sqrt(2*math.pow(rozmer,2))/2)

        t.penup()
        # želva na pozici 0,0
        t.home()
    
    else:
        raise ValueError("Základna domečku musí být kladná")


def main(): 

    # barva pozadí okna
    bgcolor("lightgray")
    # velikost okna
    screensize(250,250)
    # název okna
    title("Domecek")

    # Vytvoříme novou želvu
    t = turtle.Turtle()
    
    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = slabý obrys
    t.pensize(2)

    #vykresleni domečku
    t.penup()
    #jdi na souřadnice
    t.goto(-60,0)
    domecek(t, 30)

    #vykresleni domečku
    domecek(t, 60)

    t.penup()
    #jdi na souřadnice
    t.goto(100,0)
    #vykresleni domečku
    domecek(t, 90)
    
    # zavření okna
    exitonclick()

if __name__ == "__main__":
    main()