import pgzrun, random

WIDTH = 1000
HEIGHT = 1000

items = []

for i in range(10):
    heart = Actor("heart")
    star = Actor("star")
    heart.pos = random.randint(20,950), random.randint(20,950)
    star.pos = random.randint(20,950), random.randint(20,950)
    items.append(heart)
    items.append(star)

def draw():
    screen.fill("Pink")
    for i in items:
        i.draw()
    screen.draw.text("Happy mothers day\n i love you so much mom", (100,100), fontsize = 100, color = "red", gcolor = "violet", owidth = 1.5, ocolor = "silver")
def update():
    for i in items:
        i.y+=1
        if i.y>1000:
            i.y=0



pgzrun.go()