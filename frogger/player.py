from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.return_to_start()
        self.setheading(90)  # face north

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.back(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def is_off_screen(self):
        if self.ycor() < -300:
            return True
        else:
            return False

    def return_to_start(self):
        self.goto(STARTING_POSITION)
