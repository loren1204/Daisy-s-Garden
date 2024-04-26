# Daisy's Garden
Re-imagined Space Invaders game. 
This project utilizes the basic functions of a Space Invaders game  while expanding upon newer features such as the following:
* character customization, using .png and .gif files to personalize frontend development of game
* lives function, 3 hearts are used to function as extra lives 
*our error handling, in functions such as key bindings, check for lives, and alien collision  

# external libraries 
About Turtle 
* creates basic graphics and imagery in the game environment
About Random
* random module spawns "aliens" in random positions within window boundaries

# PyCharm files 
place the following  image file into directory in PyCharm (preferrably) for code to run:

*![pixeldaisy](https://github.com/loren1204/Daisy-s-Garden/assets/166956027/7a922b80-329e-4609-8ca7-6ff582bf7d92)
*![DAISY’S GARDEN (1)](https://github.com/loren1204/Daisy-s-Garden/assets/166956027/6d4ba7e1-23b6-https://github.com/notifications4f42-9799-7cedd6b104b4)
*![vines](https://github.com/loren1204/Daisy-s-Garden/assets/166956027/75125662-4791-4e26-b21c-3df668079417)
* need to add smaller hearts link 

  
# start
import random
import time
import turtle

#defining 
turtle.register_shape("smaller_heart.gif")

#settings for cannon, laser and aliens
FRAME_RATE = 30  # Frames per second
TIME_FOR_1_FRAME = 1 / FRAME_RATE  # Seconds

CANNON_STEP = 10
LASER_LENGTH = 20
LASER_SPEED = 60
ALIEN_SPAWN_INTERVAL = 1 # Seconds
ALIEN_SPEED = 2.5
MAX_HEALTH = 3  # Maximum health value for the player

#Set up Window  
window = turtle.Screen()
window.tracer(0)
window.setup(0.5, 0.75)

window.bgpic("background.png")
window.title("Daisy's Garden")

#window size
LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_height() / 2
BOTTOM = -window.window_height() / 2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * window.window_width()

turtle.register_shape("pixeldaisy.gif")
turtle.register_shape("vines.gif")
cannon = turtle.Turtle()
cannon.penup()
cannon.color(1, 1, 1)
cannon.shape("pixeldaisy.gif")
cannon.setposition(0, FLOOR_LEVEL + 115)
cannon.cannon_movement = 0  # -1, 0 or 1 for left, stationary, right

# Create lives indicator (hearts) #added contribution
lives = []
for i in range(MAX_HEALTH): #max health is set to 3 so, for i in rannge 0, 1, 2 
   life = turtle.Turtle()
   life.penup()
   life.color("red")
   life.shape("smaller_heart.gif")
   life.setposition(RIGHT - 30 - i * 30, TOP - 30)
   life.showturtle()
   lives.append(life)

# Create turtle for writing text
text = turtle.Turtle() 
text.penup()
text.hideturtle()
text.setposition(LEFT * 0.8, TOP * 0.8)
text.color(1, 1, 1)

lasers = []
aliens = []

player_lives = MAX_HEALTH

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
    # Move laser to just above cannon tip
    laser.forward(10)
    # Prepare to draw the laser
    laser.pendown()
    laser.pensize(7)

    lasers.append(laser)

def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    # Draw the laser
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)

def create_alien():
    alien = turtle.Turtle()
    alien.penup()
    alien.turtlesize(0.05)
    alien.setposition(
        random.randint(
            int(LEFT + 100), #fixed contribution 
            int(RIGHT - 100), #fixed contribution
        ),
        TOP,
    )
alien.shape("vines.gif")
    alien.setheading(-90)
    aliens.append(alien)

def remove_sprite(sprite, sprite_list):
    sprite.clear()
    sprite.hideturtle()
    window.update()
    sprite_list.remove(sprite)
    turtle.turtles().remove(sprite)

# Key bindings
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeyrelease(stop_cannon_movement, "Left")
window.onkeyrelease(stop_cannon_movement, "Right")
window.onkeypress(create_laser, "space")
window.onkeypress(turtle.bye, "q")
window.listen()

draw_cannon()

# Game loop 
alien_timer = 0
game_timer = time.time()
score = 0
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
    new_x = cannon.xcor() + CANNON_STEP * cannon.cannon_movement
    if LEFT + GUTTER <= new_x <= RIGHT - GUTTER:
        cannon.setx(new_x)
        draw_cannon()
    # Move all lasers
    for laser in lasers.copy():
        move_laser(laser)
        # Remove laser if it goes off screen
        if laser.ycor() > TOP:
            remove_sprite(laser, lasers)
            break
        # Check for collision with aliens
        for alien in aliens.copy():
            if laser.distance(alien) < 20:
                remove_sprite(laser, lasers)
                remove_sprite(alien, aliens)
                score += 1
                break
    # Spawn new aliens when time interval elapsed
    if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
        create_alien()
        alien_timer = time.time()
 # Move all aliens LIFE HEART!!! #added contribution
    for alien in aliens:
        alien.forward(ALIEN_SPEED)
        # Check for game over
        if alien.ycor() < FLOOR_LEVEL:
            player_lives -= 1
            if player_lives == -1:
                game_running = False
            else:
                # Remove a heart from the display
                life = lives.pop()
                life.clear()
                life.hideturtle()
            remove_sprite(alien, aliens)

            
    # Check for collision with player
    for alien in aliens.copy():
        if alien.distance(cannon) < 20:  # Adjust collision distance as needed
            player_lives -= 1  # Decrease player's lives upon collision
            if player_lives == -1:
                game_running = False
            else:
                # Remove a heart from the display
                life = lives.pop()
                life.clear()
                life.hideturtle()

            remove_sprite(alien, aliens)


    time_for_this_frame = time.time() - timer_this_frame
    if time_for_this_frame < TIME_FOR_1_FRAME:
        time.sleep(TIME_FOR_1_FRAME - time_for_this_frame)
    window.update()

splash_text = turtle.Turtle()
splash_text.hideturtle()
splash_text.color(1, 1, 1)
splash_text.write("GAME OVER", font=("Courier", 40, "bold"), align="center")

turtle.done()
window.update()
