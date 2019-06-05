import turtle
import random

turtle.shape("turtle")
turtle.speed("fastest")
turtle.color("red")

for y in range(360):
    for index in range(180):
      turtle.forward(10)
      turtle.right(170-index*2+random.random()*0.1)
    turtle.right(5)
