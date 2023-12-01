#Projeto2Noisr

import random
import matplotlib.pyplot as plt

def random_walk(num_steps, prob_right, num_particles):
    #escrever aqui
    
    create_plot(num_steps, particles_paths)
    return particles_paths

def create_plot(num_steps, particles_paths):
    time = [x for x in range(len(particles_paths[0]))]
    for particle_path in particles_paths:
        plt.plot(particle_path, time)
    plt.title("Random Walk - N particles")
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.show()

num_steps = 100
prob_right = 0.5
num_particles = 10

random_walk(num_steps, prob_right, num_particles)