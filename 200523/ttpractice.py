# from turtle import *
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# for x in range(360):
#     pencolor(colors[x % 6])
#     width(x / 100 + 1)
#     forward(x)
#     left(59)

from turtle import *

# count = 5
# while count > 0:
#     forward(100)
#     left(72)
#     count = count -1

def pentagoal():
    count = 5
    while count > 0:
        forward(100)
        left(72)
        count = count -1

pentagoal()
penup()
goto(-50, -70)
pendown()
pentagoal()
penup()
goto(40,40)
pendown()
pentagoal()
done()
