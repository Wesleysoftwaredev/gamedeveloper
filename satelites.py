import pgzrun,random,time

WIDTH = 500
HEIGHT = 500
start_time = 0
end_time = 0
satnum = 10
cursat = 0
st1 = []
ln1 = []
start_time = time.time()
for i in range(10):
    sat = Actor("satelites")
    sat.pos = random.randint(50,450), random.randint(50,450)
    st1.append(sat) 
def draw():
    global end_time
    screen.blit("bg1", (0,0))
    num=1
    for i in st1:
        i.draw()
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20))
        num+=1
    if cursat<satnum:

       end_time=time.time()-start_time

       screen.draw.text(str(round(end_time)),(30,30))
    else:
        screen.draw.text(str(round(end_time)),(30,30))
    for i in ln1:
        screen.draw.line(i[0],i[1],"yellow")

def update():
    pass

def on_mouse_down(pos):
    global cursat,ln1
    if cursat<satnum:
        if st1[cursat].collidepoint(pos):
            if cursat:
                ln1.append((st1[cursat-1].pos,st1[cursat].pos))
            cursat+=1
        else:
            cursat=0
            ln1=[]
             


pgzrun.go()