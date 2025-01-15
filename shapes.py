import pgzrun, random
WIDTH = 500
HEIGHT = 500

def draw():
    w=500
    y=100
    screen.fill("black")
    for i in range(20):

        r=random.randint(0, 255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        obj = Rect(0,0,w,y)
        obj.center=250,250
        screen.draw.rect(obj, (r, g, b))
        w -= 20
        y += 20



pgzrun.go()