import pgzrun, random
WIDTH = 750
HEIGHT = 550

def draw():
    z=550
    x=150
    screen.fill("black")
    for i in range(25):
        r=random.randint(0, 255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        obj = Rect(0,0,z,x)
        obj.center=300,300
        #screen.draw.rect(obj, (r,g,b))
        z -= 20
        x += 20
    screen.draw.filled_circle((375,225),50,"red")

    screen.draw.line((375,225),(415,285),"yellow")

    screen.draw.text(("Skibidi Toilet"),(375,225),fontsize=45,color="yellow")
pgzrun.go()

