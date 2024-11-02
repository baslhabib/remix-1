import random

# Parameters
POPULATION_SIZE = 10
GENE_LENGTH = 8  # Length of the binary string
MUTATION_RATE = 0.1  # Probability of mutation

# Fitness function: counts the number of 1's in the binary string
def fitness_function(individual):
    return sum(individual)

# Create initial population
def initialize_population():
    return [[random.randint(0, 1) for _ in range(GENE_LENGTH)] for _ in range(POPULATION_SIZE)]

# Select parents based on fitness
def selection(population):
    weighted_population = [(individual, fitness_function(individual)) for individual in population]
    total_fitness = sum(fitness for _, fitness in weighted_population)
    probabilities = [fitness / total_fitness for _, fitness in weighted_population]

    return random.choices(population, weights=probabilities, k=2)

# Crossover between two parents to produce an offspring
def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENE_LENGTH - 1)
    offspring = parent1[:crossover_point] + parent2[crossover_point:]
    return offspring

# Mutate an individual
def mutate(individual):
    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]  # Flip bit
    return individual

# Genetic algorithm implementation
def genetic_algorithm():
    population = initialize_population()
    generations = 20

    for generation in range(generations):
        print(f"Generation {generation}: {population}")
        new_population = []

        for _ in range(POPULATION_SIZE):
            parent1, parent2 = selection(population)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring)
            new_population.append(offspring)

        population = new_population

    # Get the best solution
    best_solution = max(population, key=fitness_function)
    return best_solution, fitness_function(best_solution)

# Run the genetic algorithm
if __name__ == "__main__":
    best_individual, best_fitness = genetic_algorithm()
    print(f"Best Individual: {best_individual}, Fitness: {best_fitness}")
