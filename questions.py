import pgzrun

HEIGHT = 800
WIDTH = 1000
TITLE = "Question Mania!"

score = 0
totaltime = 15
question_num = 0
question_max = 0

scrollerbox = Rect(0,0,1000,100)
questionbox = Rect(10,120,800,200)
timerbox = Rect(830,120,165,200)
optionbox1 = Rect(10,340,390,200)
optionbox2 = Rect(420,340,390,200)
optionbox3 = Rect(10,550,390,200)
optionbox4 = Rect(420,550,390,200)
skipbox = Rect(830,340,775,410)

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
info()
print(questions)
pgzrun.go()