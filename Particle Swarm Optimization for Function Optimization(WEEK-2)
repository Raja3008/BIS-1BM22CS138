import random

def objective_function(x):
    return sum([xi**2 for xi in x])

num_particles = 100
max_iter = 50
dim = 2
minx = -10
maxx = 10
w = 0.5
c1 = 1.5
c2 = 1.5

class Particle:
    def __init__(self):
        self.position = [random.uniform(minx, maxx) for _ in range(dim)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dim)]
        self.best_position = self.position[:]
        self.best_fitness = objective_function(self.position)

    def update_velocity(self, global_best_position):
        r1 = random.random()
        r2 = random.random()
        for i in range(dim):
            cognitive_component = c1 * r1 * (self.best_position[i] - self.position[i])
            social_component = c2 * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive_component + social_component

    def update_position(self):
        for i in range(dim):
            self.position[i] += self.velocity[i]
            if self.position[i] < minx:
                self.position[i] = minx
            elif self.position[i] > maxx:
                self.position[i] = maxx

swarm = [Particle() for _ in range(num_particles)]

global_best_position = swarm[0].position[:]
global_best_fitness = objective_function(global_best_position)

for iteration in range(max_iter):
    for particle in swarm:
        fitness = objective_function(particle.position)

        if fitness < particle.best_fitness:
            particle.best_fitness = fitness
            particle.best_position = particle.position[:]

        if fitness < global_best_fitness:
            global_best_fitness = fitness
            global_best_position = particle.position[:]

        particle.update_velocity(global_best_position)
        particle.update_position()

    print(f"Iteration {iteration+1}:  Best Fitness = {global_best_fitness}")

print(f"Optimal solution: Position = {global_best_position}, Fitness = {global_best_fitness}")
