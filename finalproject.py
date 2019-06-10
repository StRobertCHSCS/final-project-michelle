'''
-------------------------------------------------------------------------------
Name:		finalproject.py
Purpose:	a description of your program>

Author:	    Tu.M

Created:	04/06/2019
------------------------------------------------------------------------------
'''

import arcade


WIDTH = 700
HEIGHT = 580

# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT - (HEIGHT - 100)

# Variables to record if certain keys are being pressed.
left_pressed = False
right_pressed = False


def on_update(delta_time):
    global right_pressed, left_pressed, player_x
    if right_pressed:
        player_x += 3
    if left_pressed:
        player_x -= 3


def on_draw():
    global player_x, player_y
    arcade.start_render()
    # Draw in here...
    arcade.draw_rectangle_filled(player_x, player_y, 150, 20, arcade.color.WHITE)


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
