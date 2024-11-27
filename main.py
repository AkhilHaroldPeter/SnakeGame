from turtle import Screen, Turtle
import turtle
import pandas as pd
from Snake import *
from Food import *
from Scoreboard import *
from Helper import *
import time
import sys

Turtle_Color_List = ['Red','White','Green','Yellow','Purple','Pink','Orange']
tcl_lower = [str(x).lower() for x in Turtle_Color_List]
SCREEN_BACKGROUND_COLOR = 'black'
GAME_TITLE = 'Snake Game'

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)


turtle.TK.messagebox.showinfo(title="Instructions", message="Welcome to the Snake Game!\n\nInstructions:\n- Use the 'Up' arrow key to move the snake up.\n- Use the 'Down' arrow key to move the snake down.\n- Use the 'Left' arrow key to move the snake left.\n- Use the 'Right' arrow key to move the snake right.\n\nEnjoy the game!")

Selected_Snake_Color = turtle.textinput("Snake Color", "Please type in the snake color you prefer:\n1.Red\n2.White\n3.Green\n4.Yellow\n5.Purple\n6.Pink\n7.Orange")
if str(Selected_Snake_Color).lower() in tcl_lower:
    pass
else:
    turtle.TK.messagebox.showerror(title="Snake Color", message=f'Error!"{Selected_Snake_Color}" is not a valid color!') #code from stackoverflow - https://stackoverflow.com/questions/67152310/alert-box-in-python-using-turtle
    sys.exit()

snake = Snake(Selected_Snake_Color)
food = Food()
Scoreboard = Scoreboard()

snake.Create_Snake(Selected_Snake_Color)

screen.listen()
screen.onkey(snake.Move_Up, "Up")
screen.onkey(snake.Move_Down, "Down")
screen.onkey(snake.Move_Left, "Left")
screen.onkey(snake.Move_Right, "Right")

def setup_event_listeners():
    screen.onkey(None, "Up")  # Clear the previous event listener
    screen.onkey(None, "Down")
    screen.onkey(None, "Left")
    screen.onkey(None, "Right")

    screen.listen()
    screen.onkey(snake.Move_Up, "Up")
    screen.onkey(snake.Move_Down, "Down")
    screen.onkey(snake.Move_Left, "Left")
    screen.onkey(snake.Move_Right, "Right")

def Game_Options(final_score):
    Choice_for_player_to_continue = turtle.textinput("Snake Game","Please type in an number for option:\n1.Restart the Game\n2.Quit\n3.Save Score\n4.View Highscore")  # \n5.Purple\n6.Pink\n7.Orange")
    if not Choice_for_player_to_continue.isdigit():
        turtle.TK.messagebox.showinfo(title="Snake Game",message=f'Error!"{Choice_for_player_to_continue}" is not a valid option!')
        sys.exit()
    if int(Choice_for_player_to_continue) == 1:
        # Game_Over = False
        # screen.clear()
        setup_event_listeners()
    elif int(Choice_for_player_to_continue) == 2:
        sys.exit()
    elif int(Choice_for_player_to_continue) == 3:
        top_ten_scores_list, df = View_Score()
        Player_Name = turtle.textinput("Scoreboard","Please type in your name")
        print(final_score)
        new_data = pd.DataFrame({"Name": [Player_Name], "Score": [final_score]})
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv('Scorebook.csv',index=None)
        sys.exit()

    elif int(Choice_for_player_to_continue) == 4:
        top_ten_scores_list , df = View_Score()
        show_table(top_ten_scores_list)
        sys.exit()
    else:
        turtle.TK.messagebox.showerror(title="Snake Game",message=f'Error!"{Choice_for_player_to_continue}" is not a valid option!')
        sys.exit()



Game_Over = False
while not Game_Over:
    screen.update()
    time.sleep(0.1)
    snake.Move_Snake()

    #To identify if the snake has come into contact with the food.
    if snake.head.distance(food) < 15:
        food.refresh_food()
        Scoreboard.Increase_Score()
        snake.extend_snake()
    #To identify if the snake has come into contact with wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        # Scoreboard.game_over()
        player_final_score = Scoreboard.final_score
        Scoreboard.reset_scoreboard()
        snake.snake_reset()
        # Game_Over = True
        Game_Options(player_final_score)

    #To detect if head collides with tail
    for parts in snake.snake_parts[1:]:
        if snake.head.distance(parts) < 10:
            # Scoreboard.game_over()
            # Game_Over = True
            player_final_score = Scoreboard.final_score
            Scoreboard.reset_scoreboard()
            snake.snake_reset()
            Game_Options(player_final_score)


screen.exitonclick()