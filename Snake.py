from turtle import Turtle

SNAKE_LENGTH = 3
SNAKE_LENGTH_INCREASE_BY  = 20
UP = 90
DOWN = 270
LEFT =180
RIGHT = 0
Snake_shape = 'square'

class Snake:
    def __init__(self, Selected_Snake_Color):
        self.snake_parts  = []
        self.snake_len = SNAKE_LENGTH
        self.snake_color = Selected_Snake_Color
        self.Create_Snake(Selected_Snake_Color)
        # Defining the snake head
        self.head = self.snake_parts[0]

    def Create_Snake(self,Snake_Color):
        for x in range(SNAKE_LENGTH):
            self.Add_Snake_Part(x)

    def Add_Snake_Part(self,position):
        snake_part = Turtle(Snake_shape)
        snake_part.color(self.snake_color)
        snake_part.penup()
        snake_part.goto(int(snake_part.xcor()) - int(position) * SNAKE_LENGTH_INCREASE_BY, int(snake_part.ycor()))
        self.snake_parts.append(snake_part)

    def Add_New_Snake_Part(self,position):
        snake_part = Turtle(Snake_shape)
        snake_part.color(self.snake_color)
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def extend_snake(self):
        self.Add_New_Snake_Part(self.snake_parts[-1].position())

    def Move_Snake(self):
        for seg in range(len(self.snake_parts) - 1, 0, -1):
            x = self.snake_parts[seg - 1].xcor()
            y = self.snake_parts[seg - 1].ycor()
            self.snake_parts[seg].goto(x, y)
        self.head.forward(SNAKE_LENGTH_INCREASE_BY)

    def Move_Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Move_Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Move_Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def Move_Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_reset(self):
        for parts in self.snake_parts:
            parts.goto(1000,1000)
        self.snake_parts.clear()
        self.Create_Snake(self.snake_color)
        self.head = self.snake_parts[0]