import random

def fitness_function(individual):
    # Example fitness function (maximize the sum of the individual's genes)
    return sum(individual)

def selection(population):
    # Select individuals based on fitness
    population.sort(key=fitness_function, reverse=True)
    return population[:len(population)//2]

def crossover(parent1, parent2):
    # Simple crossover
    split = random.randint(1, len(parent1) - 1)
    return parent1[:split] + parent2[split:]

def mutate(individual):
    # Simple mutation
    if random.random() < 0.1:  # 10% mutation chance
        index = random.randint(0, len(individual) - 1)
        individual[index] = random.randint(0, 1)  # Assuming binary genes
    return individual

def run_genetic_algorithm():
    population_size = 10
    gene_length = 5
    generations = 20

    # Initialize population
    population = [[random.randint(0, 1) for _ in range(gene_length)] for _ in range(population_size)]

    for _ in range(generations):
        selected = selection(population)
        offspring = []

        while len(offspring) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            offspring.append(child)

        population = selected + offspring  # Replace the old population

    return population

if __name__ == "__main__":
    final_population = run_genetic_algorithm()
    print("Final Population:", final_population)
