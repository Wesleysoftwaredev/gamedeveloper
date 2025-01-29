import pgzrun, random, time

HEIGHT = 500
WIDTH = 850
TITLE = "Peppa Rush"
msg= ""
glooboda = Actor("peppa")
glooboda.pos = (250,250)

def draw():
    screen.clear()
    screen.fill("Pink")
    glooboda.draw()
    screen.draw.text(msg,(325,50),fontsize=40)

def on_mouse_down(pos):
    global msg
    if glooboda.collidepoint(pos):
        sounds.eep.play()
        msg = "What a hit girl!"
    else:
        msg = "Unlucky Jessica!"

def update():
    glooboda.x+=10
    if glooboda.left>850:
        glooboda.right = 0

   

pgzrun.go()