'''
-------------------------------------------------------------------------------
Name:		finalproject.py
Purpose:	<a description of your program>

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


# ---- Counters ----
timer = 0
points_counter = 0
lost_ball = False

# ---- Positions of Platforms And Balls ----
player_x = WIDTH/2
player_y = 50
ball_x = random.randrange(12, WIDTH - 12)
ball_y = random.randrange(HEIGHT - 100, HEIGHT - 12)
# minimum height will be changed to the top of the platform

# ---- Speed and Direction of Balls ----

ballmove_y = 2
ballmove_x = random.randrange(-2, 4)
if ballmove_x == 0 :
    ballmove_x += 2
'''ballmove_y = random.randrange(-2, 6)'''

'''
ball2_x = random.randrange(10, WIDTH - 10)
ball2_y = random.randrange(player_y, HEIGHT - 10)  # minimum height will be changed to the top of the platform
'''

# ---- Variables for the keys used in this program ----
left_pressed = False
right_pressed = False


# ------------   Main Game Code   ------------

def on_draw():
    global player_x, player_y, ball_x, ball_y, timer, YourScore
    arcade.start_render()
    # ---- Draw Commands Below ----
    arcade.draw_rectangle_filled(player_x, player_y, 150, 15, arcade.color.WHITE)
    arcade.draw_circle_filled(ball_x, ball_y, 12, arcade.color.WHITE)
    #output = "Score: ".format(int(YourScore))
    #arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


def on_update(delta_time):
    global right_pressed, left_pressed, player_x, player_y, ball_y, ball_x, timer, ballmove_x, ballmove_y
    if right_pressed:
        player_x += 8
    if left_pressed:
        player_x -= 8

    for _ in range(3):

        if ball_y == player_y + 12:
            if player_x - 75 <= ball_x <= player_x + 75:
                ballmove_y *= -1

            else: break

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

    # arcade.check_for_collision()


def on_key_press(key, modifiers):
    global right_pressed, left_pressed
    if key == arcade.key.A:
        left_pressed = True
    if key == arcade.key.D:
        right_pressed = True


def on_key_release(key, modifiers):
    global right_pressed, left_pressed
    if key == arcade.key.A:
        left_pressed = False
    if key == arcade.key.D:
        right_pressed = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Bouncing Ball Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
