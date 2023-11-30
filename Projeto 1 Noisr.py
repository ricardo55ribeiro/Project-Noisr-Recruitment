#Projeto 1 Noisr

#imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#variables
radius = 0.1
initial_pos1 = 1
initial_pos2 = 3
initial_velocity1 = 0.1
initial_velocity2 = -0.1
mass1 = 2.0
mass2 = 2.5
num_frames = 500
box_size = 5

#collision function
def simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size):
    #lists to save ball positions (***)
    ball1_x = [initial_pos1]
    ball2_x = [initial_pos2]
    
    #give first velocities to the balls
    ball1_velocity = initial_velocity1
    ball2_velocity = initial_velocity2

    #repeat actions below in each frame (from animation)
    for eachframe in range(num_frames):
        #change positions due to velocity
        ball1_newpos = ball1_x[-1] + ball1_velocity
        ball2_newpos = ball2_x[-1] + ball2_velocity

        #collisions with walls, so the balls stay inside the box
        if ball1_newpos + radius >= box_size or ball1_newpos - radius <= 0:
            ball1_velocity = -ball1_velocity
        if ball2_newpos + radius >= box_size or ball2_newpos - radius <= 0:
            ball2_velocity = -ball2_velocity
        
        #collisions between balls: had to put together energy conservation and linear momentum equations to get an equation independent of final velocity of each ball
        #because otherwise it wasn't working, because I couldn't solve both at the same time, and with the "newball1_velocity , newball2_velocity = ..." wasn't working either
        if abs(ball2_newpos - ball1_newpos) <= 2 * radius:
            newball1_velocity = (2 * mass2 / (mass1 + mass2)) * ball2_velocity + ((mass1 - mass2) / (mass1 + mass2)) * ball1_velocity 
            newball2_velocity = (2 * mass1 / (mass1 + mass2)) * ball1_velocity + ((mass2 - mass1) / (mass1 + mass2)) * ball2_velocity

            ball1_velocity = newball1_velocity
            ball2_velocity = newball2_velocity
        
        #append new positions to the list, so it gets updated in ***
        ball1_x.append(ball1_newpos)
        ball2_x.append(ball2_newpos)

    #create animation (function below)
    create_animation(ball1_x , ball2_x, box_size)

#animation function
def create_animation(positions1, positions2, box_size):
    num_frames = len(positions1)

    fig, ax = plt.subplots()
    ax.set_xlim(0, box_size)
    ax.set_ylim(-0.1, 0.1)

    ball1 , = ax.plot(positions1[0], 0, 'bo', markersize=10) 
    ball2 , = ax.plot(positions2[0], 0, 'ro', markersize=10)  

    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1 , ball2
    
    ani = FuncAnimation(fig , update, frames=num_frames, blit=True)
    plt.show()

    plt.close()

#execute code
simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size)