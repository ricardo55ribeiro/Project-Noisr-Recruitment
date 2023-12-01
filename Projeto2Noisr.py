#Projeto2Noisr

import random
import matplotlib.pyplot as plt

def random_walk(num_steps, prob_right, num_particles):
    particles_paths = []

    for particle in range(num_particles):
        particle_path = [0]
        for step in range(1, num_steps + 1):
            x = random.uniform(0,1)
            if x <= prob_right:
                new_position = particle_path[-1] + 1
            else:
                new_position = particle_path[-1] - 1
            particle_path.append(new_position)

        particles_paths.append(particle_path)
    
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

num_steps = int(input("Número de Movimentos: "))
while True:
    try:
        prob_right = float(input("Probabilidade de Ir para a Direita (de 0 a 1): "))
        if 0 < prob_right < 1:
            break
        else:
            raise ValueError
    except:
        print("Probabilidade tem de ser entre 0 e 1 !\n")

num_particles = int(input("Número de Partículas: "))


random_walk(num_steps, prob_right, num_particles)