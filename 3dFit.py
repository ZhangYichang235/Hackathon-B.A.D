import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define the problem parameters
BOX_SIZE = [2, 1, 3]  # Dimensions of each box
BOX_COUNT = 50  # Number of boxes to be fitted
SPACE_SIZE = [10, 10, 10]  # Dimensions of the limited 3D space

# Define the genetic algorithm parameters
POPULATION_SIZE = 50
GENERATION_COUNT = 1000
MUTATION_RATE = 0.1

# Generate the initial population
def generate_population():
    population = []
    for i in range(POPULATION_SIZE):
        boxes = np.zeros((BOX_COUNT, 3))
        for j in range(BOX_COUNT):
            boxes[j, :] = [random.uniform(0, SPACE_SIZE[0] - BOX_SIZE[0]),
                           random.uniform(0, SPACE_SIZE[1] - BOX_SIZE[1]),
                           random.uniform(0, SPACE_SIZE[2] - BOX_SIZE[2])]
        population.append(boxes)
    return population

# Calculate the fitness of a solution
def calculate_fitness(boxes):
    fitness = 0
    for i in range(BOX_COUNT):
        for j in range(i+1, BOX_COUNT):
            distance = np.linalg.norm(boxes[i] - boxes[j])
            fitness += max(0, distance - np.sqrt(sum(BOX_SIZE)**2))
    return fitness

# Select parents using tournament selection
def tournament_selection(population):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    best = tournament[0]
    for i in range(1, tournament_size):
        if calculate_fitness(tournament[i]) < calculate_fitness(best):
            best = tournament[i]
    return best

# Crossover two parents to create a new child
def crossover(parent1, parent2):
    child = np.zeros((BOX_COUNT, 3))
    for i in range(BOX_COUNT):
        for j in range(3):
            if random.random() < 0.5:
                child[i,j] = parent1[i,j]
            else:
                child[i,j] = parent2[i,j]
    return child

# Mutate a solution by randomly changing the position of a box
def mutate(boxes):
    for i in range(BOX_COUNT):
        if random.random() < MUTATION_RATE:
            boxes[i, :] = [random.uniform(0, SPACE_SIZE[0] - BOX_SIZE[0]),
                           random.uniform(0, SPACE_SIZE[1] - BOX_SIZE[1]),
                           random.uniform(0, SPACE_SIZE[2] - BOX_SIZE[2])]
    return boxes

# Visualize the solution
def visualize(boxes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(BOX_COUNT):
        x, y, z = boxes[i, :]
        ax.scatter(x, y, z, c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Main genetic algorithm loop
population = generate_population()
for generation in range(GENERATION_COUNT):
    # Select the parents
    parent1 = tournament_selection(population)
    parent2 = tournament_selection(population)
    # Create the child
    child = crossover(parent1, parent2)
    # Mutate the child
    child = mutate(child)

   
child_fitness = calculate_fitness(child)
# Replace the weakest member of the population with the child
population_fitness = [calculate_fitness(p) for p in population]
weakest_index = population_fitness.index(max(population_fitness))
population[weakest_index] = child
# Visualize the current best solution
best_solution = population[np.argmin(population_fitness)]
print(f"Generation {generation+1}, Best Fitness: {calculate_fitness(best_solution)}")
visualize(best_solution)
