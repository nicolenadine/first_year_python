import colorgram
import turtle as turtle_module
import random

# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

color_list = [(246, 245, 243), (234, 240, 246), (240, 246, 243), (247, 239, 243),
              (131, 165, 206), (225, 151, 100), (32, 41, 59), (200, 134, 147),
              (235, 212, 87), (166, 56, 46), (39, 104, 153), (141, 184, 161),
              (153, 58, 65), (170, 29, 33), (217, 80, 69), (158, 32, 29),
              (15, 96, 71), (236, 165, 156), (50, 111, 90), (58, 50, 47),
              (50, 42, 46), (228, 164, 168), (34, 61, 56), (170, 188, 222),
              (190, 99, 108), (32, 59, 108), (103, 127, 163), (34, 151, 210),
              (175, 200, 188), (66, 66, 56)]

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)

total_dots = 100

for dot_count in range(1, total_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
