'''
-------------------------------------------------------------------------------
Name:		finalproject.py
Purpose:	A game in which you try and keep the ball from falling
            by bouncing it off a bar

Author:	    Tu.M

Created:	04/06/2019
------------------------------------------------------------------------------
'''

# ---- Import Statements ----
import arcade
import random


# ---- Window Dimensions ----
WIDTH = 700
HEIGHT = 580


# ------------   Global Variables   ------------

# ---- Miscellaneous Variables ----
number_of_balls = 2
fail_message_x = 100
fail_message = ""

# ---- Positions of Platforms And Balls ----
bar_x = WIDTH/2
bar_y = 50
ball_x = random.randrange(12, WIDTH - 12)
ball_y = HEIGHT - 12

# ---- Speed and Direction of Balls ----
ballmove_y = 2
ballmove_x = random.randrange(-2, 4)
if ballmove_x == 0:
    ballmove_x += 2

# ---- True-False Variables ----
left_pressed = False
right_pressed = False
space_pressed = False
ball_paddle_collision = True
game_over = False

# ---- Counters ----
points = 0
time = 0

# ------------   Main Game Code   ------------


def on_update(delta_time, sound=None):
    global right_pressed, left_pressed, bar_x, bar_y, ball_y, ball_x, time, ballmove_x, ballmove_y, points, time, \
        fail_message, number_of_balls, ball_paddle_collision, fail_message_x
    if right_pressed:
        if bar_x + 75 < WIDTH:
            bar_x += 10
    if left_pressed:
        if bar_x - 75 > 0:
            bar_x -= 10

    if space_pressed is True:
        if ball_paddle_collision is False:
            number_of_balls -= 1

    for _ in range(3):

        if ball_y == bar_y + 12:
            if bar_x - 75 <= ball_x <= bar_x + 75:
                ballmove_y *= -1
                ball_paddle_collision is True
                points += 1
        elif ball_y < bar_y + 12:
            ball_paddle_collision = False
            ballmove_x = 0
            ballmove_y = 0
            if number_of_balls < 1:
                fail_message = "Game Over"
                fail_message_x = 250
                game_over is True
            else:
                fail_message = "Press Space Bar to Play Again"

        ball_x += ballmove_x
        ball_y += ballmove_y

        if ball_x < 12:
            ballmove_x *= -1

        if ball_y < 12:
            ballmove_y *= -1

        if ball_x > WIDTH - 12:
            ballmove_x *= -1

        if ball_y > HEIGHT - 12:
            ballmove_y *= -1

    time += delta_time


def on_draw():
    global bar_x, bar_y, ball_x, ball_y, points, ball_paddle_collision, fail_message, number_of_balls, fail_message_x
    arcade.start_render()
    # ---- Draw Commands Below ----
    # - Main Game Drawings -
    arcade.draw_rectangle_filled(bar_x, bar_y, 150, 15, arcade.color.WHITE)
    arcade.draw_circle_filled(ball_x, ball_y, 12, arcade.color.BANANA_YELLOW)
    # - Points Counter Drawing -
    arcade.draw_text("Points: " + str(points), 20, 550, arcade.color.WHITE, 18)
    # - Timer Drawing -
    seconds = round(time % 100)
    timer = f"Time: {seconds}"
    arcade.draw_text(timer, 590, 550, arcade.color.WHITE, 18)
    # - Balls Left & Fail Message Drawings -
    arcade.draw_text(fail_message,fail_message_x , 300, arcade.color.WHITE, 30)
    arcade.draw_text("Balls Left: " + str(number_of_balls), 300, 550, arcade.color.WHITE, 18)


def on_key_press(key, modifiers):
    global right_pressed, left_pressed, space_pressed, number_of_balls, ball_paddle_collision, bar_x, bar_y, \
        ball_x, ball_y, ballmove_x, ballmove_y, time, points, fail_message
    if key == arcade.key.A:
        left_pressed = True
    if key == arcade.key.D:
        right_pressed = True
    if key == arcade.key.SPACE:
        if (ball_paddle_collision is False) and (number_of_balls >= 1):
            ball_paddle_collision is True
            number_of_balls -= 1
            bar_x = WIDTH / 2
            bar_y = 50
            ball_x = random.randrange(12, WIDTH - 12)
            ball_y = HEIGHT - 12

            # ---- Speed and Direction of Balls ----
            ballmove_y = 2
            ballmove_x = random.randrange(-2, 4)
            if ballmove_x == 0:
                ballmove_x += 2

            # ---- Variables for the keys used in this program ----
            left_pressed = False
            right_pressed = False
            space_pressed = False
            ball_paddle_collision = True

            fail_message = ""
            # ---- Counters ----
            points = 0
            time = 0


def on_key_release(key, modifiers):
    global right_pressed, left_pressed, space_pressed
    if key == arcade.key.A:
        left_pressed = False
    if key == arcade.key.D:
        right_pressed = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Bouncing Ball Game")
    arcade.set_background_color(arcade.color.BLUEBONNET)
    arcade.schedule(on_update, 1/100)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
