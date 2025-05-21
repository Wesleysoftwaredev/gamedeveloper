import pgzrun

HEIGHT = 800
WIDTH = 1000
TITLE = "Question Mania!"

score = 0
totaltime = 15
question_num = 0
question_max = 0
gamefinished = False

scrollerbox = Rect(0,0,1000,100)
questionbox = Rect(10,120,800,200)
timerbox = Rect(830,120,165,200)
optionbox1 = Rect(10,340,390,200)
optionbox2 = Rect(420,340,390,200)
optionbox3 = Rect(10,550,390,200)
optionbox4 = Rect(420,550,390,200)
skipbox = Rect(830,340,165,410)
optionlist = [optionbox1, optionbox2, optionbox3, optionbox4]

questions=[]


def draw():
    screen.draw.filled_rect(scrollerbox, "red")
    screen.draw.filled_rect(questionbox, "blue")
    screen.draw.filled_rect(timerbox, "purple")
    screen.draw.filled_rect(optionbox1, "yellow")
    screen.draw.filled_rect(optionbox2, "green")
    screen.draw.filled_rect(optionbox3, "orange")
    screen.draw.filled_rect(optionbox4, "cyan")
    screen.draw.filled_rect(skipbox, "brown")
    scrollerboxmsg=f"Welcome to the quiz master -{question_num}/{question_max}"
    screen.draw.textbox(scrollerboxmsg, scrollerbox, color="black")
    screen.draw.textbox(each_q[0].strip(), questionbox, color="white")
    screen.draw.textbox(str(totaltime), timerbox, color="black")
    screen.draw.textbox("skip", skipbox, color="black")
    index = 1
    for i in optionlist:
        screen.draw.textbox(each_q[index].strip(), i, color="white")
        index+=1


def update():
    scrollerbox.x+=2
    if scrollerbox.x>=1000:
        scrollerbox.right=0

def info():
    global question_max
    with open("questions.txt", "r") as file:
        for i in file:
            questions.append(i)
            question_max+=1
def load_q():
    global question_num
    question_num+=1
    return questions.pop(0).split("|")
def timer():
    global totaltime
    if totaltime:
        totaltime-=1 
    else:
        game_over()
def game_over():
    global each_q, totaltime, gamefinished
    finalmsg = f"Game over, you got {score} correct, WELLDONE!"
    each_q = [finalmsg, "-", "-", "-", "-", 7]
    totaltime = 0
    gamefinished = True

def on_mouse_down(pos):
    index = 1
    for i in optionlist:
        if i.collidepoint(pos):
            if index is int(each_q[5]):
                c_answer()
            else:
                game_over()
        index+=1
    if skipbox.collidepoint(pos):
        skip_question()
def c_answer():
    global each_q, load_q, totaltime, score
    score+=1
    if questions:
        each_q=load_q()
        totaltime=15 
    else:
        game_over()

def skip_question():
    global each_q, load_q, totaltime
    if questions:
        each_q=load_q()
        totaltime=15 
    else:
        game_over()
 


info()
each_q=load_q()
clock.schedule_interval(timer, 1)
pgzrun.go()