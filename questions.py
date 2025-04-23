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





def draw():
    screen.draw.filled_rect(scrollerbox, "red")
    screen.draw.filled_rect(questionbox, "blue")
    screen.draw.filled_rect(timerbox, "purple")
    screen.draw.filled_rect(optionbox1, "yellow")
    screen.draw.filled_rect(optionbox2, "green")



pgzrun.go()