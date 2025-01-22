import pgzrun, random

HEIGHT = 500
WIDTH  = 850
TITLE = "Alien Rush"
msg = ""
glooboda = Actor("alien")
glooboda.pos = (250,250)

def draw():
    screen.clear()
    screen.fill("purple")
    glooboda.draw()
    screen.draw.text(msg,(325,50),fontsize=45)

def on_mouse_down(pos):
    global msg
    if glooboda.collidepoint(pos):
        glooboda.pos = (random.randint(50,450),random.randint(40,450))
        msg = "Good Hit"
    else:
        msg = "Sorry,Buddy get him next time"

pgzrun.go()