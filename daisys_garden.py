"""Daisy's Garden - a re-imagined Space Invaders game built with turtle.

Controls: Left/Right arrows to move, Space to fire, Q to quit.
Image files (background.png, pixeldaisy.gif, vines.gif, smaller_heart.gif)
must be in the same folder as this script.
"""

import random
import time
import turtle

from game_logic import clamp_move, is_hit, lose_life, spawn_x_range

# Settings for cannon, laser and aliens
FRAME_RATE = 30  # Frames per second
TIME_FOR_1_FRAME = 1 / FRAME_RATE  # Seconds
CANNON_STEP = 10
LASER_LENGTH = 20
LASER_SPEED = 60
ALIEN_SPAWN_INTERVAL = 1  # Seconds
ALIEN_SPEED = 2.5
MAX_HEALTH = 3  # Maximum health value for the player

# Set up window
window = turtle.Screen()
window.tracer(0)
window.setup(0.5, 0.75)
window.bgpic("background.png")
window.title("Daisy's Garden")

LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_height() / 2
BOTTOM = -window.window_height() / 2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * window.window_width()

turtle.register_shape("pixeldaisy.gif")
turtle.register_shape("vines.gif")
turtle.register_shape("smaller_heart.gif")

# Player (the daisy cannon)
cannon = turtle.Turtle()
cannon.penup()
cannon.color(1, 1, 1)
cannon.shape("pixeldaisy.gif")
cannon.setposition(0, FLOOR_LEVEL + 115)
cannon.cannon_movement = 0  # -1, 0 or 1 for left, stationary, right

# Lives indicator (hearts)
lives = []
for i in range(MAX_HEALTH):
    life = turtle.Turtle()
    life.penup()
    life.color("red")
    life.shape("smaller_heart.gif")
    life.setposition(RIGHT - 30 - i * 30, TOP - 30)
    life.showturtle()
    lives.append(life)

# Turtle for writing the timer and score
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.setposition(LEFT * 0.8, TOP * 0.8)
text.color(1, 1, 1)

lasers = []
aliens = []


def move_left():
    cannon.cannon_movement = -1


def move_right():
    cannon.cannon_movement = 1


def stop_cannon_movement():
    cannon.cannon_movement = 0


def create_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color(0, 1, 1)
    laser.hideturtle()
    laser.setposition(cannon.xcor() + 90, cannon.ycor() + 15)
    laser.setheading(90)
    laser.forward(10)  # Move laser to just above cannon tip
    laser.pendown()
    laser.pensize(7)
    lasers.append(laser)


def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)


def create_alien():
    alien = turtle.Turtle()
    alien.penup()
    alien.turtlesize(0.05)
    low, high = spawn_x_range(LEFT, RIGHT)
    alien.setposition(random.randint(low, high), TOP)
    alien.shape("vines.gif")
    alien.setheading(-90)
    aliens.append(alien)


def remove_sprite(sprite, sprite_list):
    sprite.clear()
    sprite.hideturtle()
    window.update()
    sprite_list.remove(sprite)
    turtle.turtles().remove(sprite)


def remove_heart():
    if lives:
        heart = lives.pop()
        heart.clear()
        heart.hideturtle()


# Key bindings
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeyrelease(stop_cannon_movement, "Left")
window.onkeyrelease(stop_cannon_movement, "Right")
window.onkeypress(create_laser, "space")
window.onkeypress(turtle.bye, "q")
window.listen()

# Game loop
alien_timer = 0
game_timer = time.time()
score = 0
player_lives = MAX_HEALTH
game_running = True

while game_running:
    timer_this_frame = time.time()

    time_elapsed = time.time() - game_timer
    text.clear()
    text.write(
        f"Time: {time_elapsed:5.1f}s\nScore: {score:5}",
        font=("Courier", 20, "bold"),
    )

    # Move cannon
    cannon.setx(clamp_move(cannon.xcor(), CANNON_STEP,
                           cannon.cannon_movement, LEFT, RIGHT, GUTTER))

    # Move all lasers
    for laser in lasers.copy():
        move_laser(laser)
        if laser.ycor() > TOP:  # Laser left the screen
            remove_sprite(laser, lasers)
            continue
        for alien in aliens.copy():
            if is_hit(laser.distance(alien)):
                remove_sprite(laser, lasers)
                remove_sprite(alien, aliens)
                score += 1
                break

    # Spawn new aliens when time interval elapsed
    if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
        create_alien()
        alien_timer = time.time()

    # Move all aliens; lose a heart if one reaches the floor or the daisy
    for alien in aliens.copy():
        alien.forward(ALIEN_SPEED)
        if alien.ycor() < FLOOR_LEVEL or is_hit(alien.distance(cannon)):
            player_lives, game_over = lose_life(player_lives)
            if game_over:
                game_running = False
            else:
                remove_heart()
            remove_sprite(alien, aliens)

    time_for_this_frame = time.time() - timer_this_frame
    if time_for_this_frame < TIME_FOR_1_FRAME:
        time.sleep(TIME_FOR_1_FRAME - time_for_this_frame)
    window.update()

splash_text = turtle.Turtle()
splash_text.hideturtle()
splash_text.color(1, 1, 1)
splash_text.write("GAME OVER", font=("Courier", 40, "bold"), align="center")
window.update()
turtle.done()
