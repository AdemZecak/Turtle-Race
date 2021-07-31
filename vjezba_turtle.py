import turtle
import time 
from turtle import * 
import random

turtle.Screen = bgcolor("lightgreen")

t1 = Turtle()
t1.penup()
t1.shape("turtle")
t1.left(90)
t1.speed(0)
t1.color("red")


t2 = t1.clone()
t2.color("yellow")

t3 = t1.clone()
t3.color("purple")

t4 = t1.clone()
t4.color("white")

t1.goto(-200, -200)
t2.goto(160,-200)
t3.goto(-70,-200)
t4.goto(50,-200)


# Finish


finish_1 = Turtle()
finish_1.penup()
finish_1.goto(-200,200)
finish_1.pendown()
finish_1.circle(20)
finish_1.hideturtle()


finish_2 = Turtle()
finish_2.penup()
finish_2.goto(160,200)
finish_2.pendown()
finish_2.circle(20)
finish_2.hideturtle()


finish_3 = Turtle()
finish_3.penup()
finish_3.goto(50,200)
finish_3.pendown()
finish_3.circle(20)
finish_3.hideturtle()


finish_4 = Turtle()
finish_4.penup()
finish_4.goto(-70,200)
finish_4.pendown()
finish_4.circle(20)
finish_4.hideturtle()


def main():
    for x in range(300):
        t1.fd(random.randrange(10))
        t2.fd(random.randrange(10))
        t3.fd(random.randrange(10))
        t4.fd(random.randrange(10))

        if (t1.position()[1]) >= 220:
            style = ('Courier', 25, 'italic')
            turtle.write('Crvena kornjača je pobjednik!', font=style, align='center')
            turtle.hideturtle()
            break

        elif (t2.position()[1]) >= 220:
            style = ('Courier', 25, 'italic')
            turtle.write('Žuta kornjača je pobjednik!', font=style, align='center')
            turtle.hideturtle()
            break

        elif (t3.position()[1]) >= 220:
            style = ('Courier', 25, 'italic')
            turtle.write('Ljubičasta kornjača je pobjednik!', font=style, align='center')
            turtle.hideturtle()
            break

        elif (t4.position()[1]) >= 220:
            style = ('Courier', 25, 'italic')
            turtle.write('Bijela kornjača je pobjednik!', font=style, align='center')
            turtle.hideturtle()
            break
        

    
main()





turtle.mainloop()