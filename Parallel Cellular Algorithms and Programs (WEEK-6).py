def objective_function(x):
    return x**2
def initialize_parameters():
    grid_size = 5
    num_iterations = 50
    lower_bound, upper_bound = 0, 5
    return grid_size, num_iterations, lower_bound, upper_bound

def initialize_population(grid_size, lower_bound, upper_bound):
    import random
    grid = [[random.uniform(lower_bound, upper_bound) for _ in range(grid_size)] for _ in range(grid_size)]
    return grid

def evaluate_fitness(grid):
    fitness_grid = [[objective_function(cell) for cell in row] for row in grid]
    return fitness_grid

def update_states(grid, fitness_grid):
    grid_size = len(grid)
    updated_grid = [[0] * grid_size for _ in range(grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            neighbors = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        neighbors.append(grid[ni][nj])

            if neighbors:
                updated_grid[i][j] = sum(neighbors) / len(neighbors)
            else:
                updated_grid[i][j] = grid[i][j]

    return updated_grid

def parallel_cellular_algorithm():
    grid_size, num_iterations, lower_bound, upper_bound = initialize_parameters()
    grid = initialize_population(grid_size, lower_bound, upper_bound)

    best_solution = None
    best_fitness = float('-inf')

    for iteration in range(num_iterations):
        fitness_grid = evaluate_fitness(grid)

        for i in range(grid_size):
            for j in range(grid_size):
                if fitness_grid[i][j] > best_fitness:
                    best_fitness = fitness_grid[i][j]
                    best_solution = grid[i][j]

        grid = update_states(grid, fitness_grid)

    return best_solution, best_fitness

best_solution, best_fitness = parallel_cellular_algorithm()
print(f"Best Solution: {best_solution}, Best Fitness: {best_fitness}")
