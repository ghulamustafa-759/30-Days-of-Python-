import turtle as t
from turtle import Screen
import random as r
import colorgram

tim = t.Turtle() 
rgb_colors = []
colors = colorgram.extract("./R.jpeg", 6)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    tim.dot(20, r.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(98)
        tim.forward(50)
        tim.setheading(188)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()