"""import pgzrun,random

WIDTH = 500
HEIGHT = 500

bee = Actor("bee")
flower = Actor("flower")

score = 0
bee.pos = 250,250
flower.pos = 125,125
game_over = False
def draw():
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),color="red",topleft=(250,10))
    if game_over:
        screen.fill("purple")
        screen.draw.text("time is up your final score is:"+str(score),color="white",topleft=(100,10))

def update():
    global score
    if keyboard.left and bee.x>0:
        bee.x-=5
    if keyboard.right and bee.x<500:
        bee.x+=5
    if keyboard.down and bee.y<500:
        bee.y+=5
    if keyboard.up and bee.y>0:
        bee.y-=5
    if bee.colliderect(flower):
        score+=10
        flower.pos = random.randint(10,450),random.randint(10,450)

def to():
    global game_over
    game_over = True
    
clock.schedule(to,120)
pgzrun.go()"""





import pgzrun,random

WIDTH = 500
HEIGHT = 500

bee = Actor("bee")
flower = Actor("flower")

score = 0
bee.pos = 175,250
flower.pos = 125,125
game_over = False
def draw():
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),color="red",topleft=(250,10))
    if game_over:
        screen.fill("purple")
        screen.draw.text("time is up your final score is:"+str(score),color="white",topleft=(100,10))

def update():
    global score
    flower.x+=5
    if flower.x>500:
        flower.right=0
        flower.y=random.randint(50,450) 
    if keyboard.down and bee.y>0:
        bee.y+=5
    if keyboard.up and bee.y<500:
        bee.y-=5
    if bee.colliderect(flower):
        score+=10
        flower.pos = 0,random.randint(10,350)

def to():
    global game_over
    game_over = True
    
clock.schedule(to,120)
pgzrun.go()