import random

def objective_function(x):
    return x ** 2

POPULATION_SIZE = 10
GENE_LENGTH = 8
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
GENERATIONS = 50
RANGE = (-10, 10)

def initialize_population():
    return [[random.randint(0, 1) for _ in range(GENE_LENGTH)] for _ in range(POPULATION_SIZE)]

def decode_gene(gene):
    binary_str = ''.join(map(str, gene))
    decimal_value = int(binary_str, 2)
    max_value = 2 ** GENE_LENGTH - 1
    return RANGE[0] + (RANGE[1] - RANGE[0]) * decimal_value / max_value

def evaluate_fitness(population):
    return [1 / (1 + objective_function(decode_gene(gene))) for gene in population]  # Minimize function

def select(population, fitness):
    total_fitness = sum(fitness)
    probabilities = [f / total_fitness for f in fitness]
    cumulative = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    selected = []
    for _ in range(len(population)):
        r = random.random()
        for i, c in enumerate(cumulative):
            if r <= c:
                selected.append(population[i])
                break
    return selected

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, GENE_LENGTH - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

def mutate(gene):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in gene]

def evolve(population):
    fitness = evaluate_fitness(population)
    selected = select(population, fitness)
    next_generation = []
    for i in range(0, len(selected), 2):
        parent1 = selected[i]
        parent2 = selected[(i+1) % len(selected)]
        offspring1, offspring2 = crossover(parent1, parent2)
        next_generation.append(mutate(offspring1))
        next_generation.append(mutate(offspring2))
    return next_generation

population = initialize_population()
for generation in range(GENERATIONS):
    population = evolve(population)
    fitness = evaluate_fitness(population)
    best_gene = population[fitness.index(max(fitness))]
    best_solution = decode_gene(best_gene)
    print(f"Generation {generation + 1}: Best solution = {best_solution}, Fitness = {max(fitness)}")

best_gene = population[fitness.index(max(fitness))]
best_solution = decode_gene(best_gene)
print(f"Best solution found: {best_solution}, Objective value: {objective_function(best_solution)}")
