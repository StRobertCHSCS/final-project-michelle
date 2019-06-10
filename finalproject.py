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


# -----------  Global Variables  -----------

# ---- Counters ----
timer = 0
points_counter = 0

# ---- Positions of Platforms And Balls ----
player_x = WIDTH/2
player_y = HEIGHT - (HEIGHT - 100)
ball_x = random.randrange(10, WIDTH - 10)
ball_y = random.randrange(player_y, HEIGHT - 10)  # minimum height will be changed to the top of the platform

# ---- Speed and Direction of Balls ----
ballmove_x = random.randrange(-2, 6)
ballmove_y = random.randrange(-2, 3)
'''
ball2_x = random.randrange(10, WIDTH - 10)
ball2_y = random.randrange(player_y, HEIGHT - 10)  # minimum height will be changed to the top of the platform
'''

# ---- Variables for the keys used in this program ----
left_pressed = False
right_pressed = False


def on_update(delta_time):
    global right_pressed, left_pressed, player_x, player_y, ball_y, ball_x, timer, ballmove_x, ballmove_y
    if right_pressed:
        player_x += 3
    if left_pressed:
        player_x -= 3

    # Tried to prevent platform from travelling off screen
    if player_x > WIDTH:
        player_x += -1

    while timer <= 60:
        timer += 1
        ball_x += ballmove_x
        ball_y += ballmove_y


    # arcade.check_for_collision()


def on_draw():
    global player_x, player_y, ball_x, ball_y
    arcade.start_render()
    # ---- Draw Commands Below ----
    arcade.draw_rectangle_filled(player_x, player_y, 150, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(ball_x, ball_y, 12, arcade.color.WHITE)


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
