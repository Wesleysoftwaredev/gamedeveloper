import pgzrun,random,time

WIDTH = 500
HEIGHT = 500
start_time = 0
end_time = 0
satnum = 10
st1 = []
start_time = time.time()
for i in range(10):
    sat = Actor("satelites")
    sat.pos = random.randint(50,450), random.randint(50,450)
    st1.append(sat) 
def draw():
    screen.blit("bg1", (0,0))
    num=1
    for i in st1:
        i.draw()
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20))
        num+=1
    end_time=time.time()-start_time
    screen.draw.text(str(round(end_time)),(30,30))
def update():
    pass
pgzrun.go()