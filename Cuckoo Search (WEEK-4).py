import random
import math

def objective_function(x):
    return sum([xi ** 2 for xi in x])

def levy_flight(Lambda, dim):
    sigma = (math.gamma(1 + Lambda) * math.sin(math.pi * Lambda / 2) /
             (math.gamma((1 + Lambda) / 2) * Lambda * 2 ** ((Lambda - 1) / 2))) ** (1 / Lambda)
    u = [random.gauss(0, sigma) for _ in range(dim)]
    v = [random.gauss(0, 1) for _ in range(dim)]
    step = [ui / abs(vi) ** (1 / Lambda) for ui, vi in zip(u, v)]
    return step

def generate_new_solution(current_solution, step_size, Lambda):
    step = levy_flight(Lambda, len(current_solution))
    return [current_solution[i] + step_size * step[i] for i in range(len(current_solution))]

def initialize_nests(num_nests, dim, lower_bound, upper_bound):
    return [[random.uniform(lower_bound, upper_bound) for _ in range(dim)] for _ in range(num_nests)]

def cuckoo_search(num_nests, dim, lower_bound, upper_bound, max_iter, discovery_prob, Lambda=1.5):
    nests = initialize_nests(num_nests, dim, lower_bound, upper_bound)
    best_nest = min(nests, key=objective_function)
    best_fitness = objective_function(best_nest)

    for _ in range(max_iter):
        new_solution = generate_new_solution(best_nest, step_size=0.01, Lambda=Lambda)
        new_fitness = objective_function(new_solution)

        if new_fitness < best_fitness:
            best_nest = new_solution
            best_fitness = new_fitness

        for i in range(int(discovery_prob * num_nests)):
            nests[random.randint(0, num_nests - 1)] = [random.uniform(lower_bound, upper_bound) for _ in range(dim)]

        for nest in nests:
            fitness = objective_function(nest)
            if fitness < best_fitness:
                best_nest = nest
                best_fitness = fitness

    return best_nest, best_fitness

if __name__ == "__main__":
    num_nests = 25
    dim = 3
    lower_bound = -10
    upper_bound = 10
    max_iter = 50
    discovery_prob = 0.25

    best_solution, best_fitness = cuckoo_search(num_nests, dim, lower_bound, upper_bound, max_iter, discovery_prob)
    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
