from turtle import *
import time
import random
screen=Screen()
screen.setup(1030, 500)
screen.bgpic("123-1000.png")

screen.bgcolor("light blue")
penup()

def main(x):
   color("white")
   for step in range(6): 
     speed(10)
     goto(-400,x)
     x-=60
     pendown()
     if step==0:
         color("green")
         write('START', font=("Arial", 10, "bold"))
         color("white")
         right(90)
         forward(300)
         backward(300)
         left(90)
     else:
         backward(10)
         write(step,align="center",font=("Arial", 10, "bold"))
         forward(10)
     
     forward(750)
     if step==0:
         color("red")
         write('END', font=("Arial", 10, "bold"))
         color("white")
         right(90)
         forward(300)
         backward(300)
         left(90)
     penup()
     backward(510)
     

def initial(x):
    #for y in range(5):
    #animals=["bat1.gif","fawn.gif","ferret1.gif","zebra2.gif","olw.gif","elephant2.gif","hummingbird.gif","camel2.gif",
                 #"dogani.gif","dogrungray.gif","horse.gif","mouse.gif","dino.gif"]
    #i = random.choice(random.sample(animals, k=2))
    animals = ["bat1.gif", "fawn.gif", "ferret1.gif", "zebra2.gif", "olw.gif"]
    for y,i in enumerate(animals):

        if y==0:
            A=Turtle()
            
            A.screen.addshape(i)
            A.shape(i)
            A.penup()
            A.goto(-420,x)
            x-=60
            
        elif y==1:
            B=Turtle()
            
            B.screen.addshape(i)
            B.shape(i)
            B.penup()
            B.goto(-420,x)
            x-=60
            
        elif y==2:
            C=Turtle()
            
            C.screen.addshape(i)
            C.shape(i)
            C.penup()
            C.goto(-420,x)
            x-=60
            
        elif y==3:
            D=Turtle()
            
            D.screen.addshape(i)
            D.shape(i)
            D.penup()
            D.goto(-420,x)
            x-=60
        elif y==4:
            E=Turtle()
            
            E.screen.addshape(i)
            E.shape(i)
            E.penup()
            E.goto(-420,x)
            x-=60
               
    
    for i in range(100):
        speed(5)
        A.forward(random.randint(1,14))     
        B.forward(random.randint(1,14))
        C.forward(random.randint(1,14))
        D.forward(random.randint(1,14))
        E.forward(random.randint(1,14))
        
        
    print(A.position())
    print(B.position())
    print(C.position())
    print(D.position())
    print(E.position())

    print(A.xcor())
    
   
    speed(10)
    goto(450,110)
    color("yellow")
    if A.xcor()>B.xcor() and A.xcor()>C.xcor() and A.xcor()>D.xcor() and A.xcor()>E.xcor():
       goto(420,110)    
       write("\'* WINNER *'",font=("Arial", 10, "bold",'italic'))
    elif B.xcor()>A.xcor() and B.xcor()>C.xcor() and B.xcor()>D.xcor() and B.xcor()>E.xcor():
       goto(420,50)
       write("\'* WINNER *'",font=("Arial", 10, "bold",'italic'))
    elif C.xcor()>A.xcor() and C.xcor()>B.xcor() and C.xcor()>D.xcor() and C.xcor()>E.xcor():
       goto(420,-10)
       write("\'* WINNER *'",font=("Arial", 10, "bold",'italic'))
    elif D.xcor()>A.xcor() and D.xcor()>B.xcor()and D.xcor()>C.xcor() and D.xcor()>E.xcor():
       goto(420,-70)
       write("\'* WINNER *'",font=("Arial", 10, "bold",'italic'))
    else:
       goto(420,-130)
       write("\'* WINNER *'",font=("Arial", 10, "bold",'italic'))   
    time.sleep(3)
if __name__=="__main__":
   main(150)
   initial(120)



              



