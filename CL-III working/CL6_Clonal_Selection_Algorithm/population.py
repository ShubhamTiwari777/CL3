import numpy as np

# Objective Function: Sphere Function (minimize the sum of squares)
def objective_function(x):
    return np.sum(x**2)

# Initialize population of antibodies
def initialize_population(population_size, dimension):
    return np.random.uniform(-10, 10, (population_size, dimension))

# Calculate affinity (fitness) of each antibody
def calculate_affinity(population):
    return np.array([objective_function(individual) for individual in population])

# Select top antibodies based on fitness (lower is better)
def select_antibodies_for_cloning(population, fitness, num_selected):
    selected_indices = np.argsort(fitness)[:num_selected]
    return population[selected_indices]

# Clone selected antibodies
def clone_antibodies(selected_antibodies, num_clones):
    return np.repeat(selected_antibodies, num_clones, axis=0)

# Mutate cloned antibodies
def mutate_antibodies(cloned_antibodies, mutation_rate):
    mutations = np.random.normal(0, mutation_rate, cloned_antibodies.shape)
    return cloned_antibodies + mutations

# Select best antibodies from mutated clones for the next generation
def select_next_generation(mutated_antibodies, mutated_fitness, population_size, dimension):
    best_indices = np.argsort(mutated_fitness)[:population_size // 2]
    best_clones = mutated_antibodies[best_indices]
    new_random = initialize_population(population_size // 2, dimension)
    return np.vstack((best_clones, new_random))

# Get best antibody from population
def best_antibody(population):
    fitness = calculate_affinity(population)
    best_index = np.argmin(fitness)
    return population[best_index], fitness[best_index]

# Clonal Selection Algorithm
def clonal_selection_algorithm(population_size, mutation_rate, num_generations, num_clones, dimension):
    # Step 1: Initialization
    population = initialize_population(population_size, dimension)

    for generation in range(num_generations):
        # Step 2: Affinity Calculation
        fitness = calculate_affinity(population)

        # Step 3: Clonal Selection
        selected_antibodies = select_antibodies_for_cloning(population, fitness, population_size // 2)

        # Step 4: Cloning
        cloned_antibodies = clone_antibodies(selected_antibodies, num_clones)

        # Step 5: Mutation
        mutated_antibodies = mutate_antibodies(cloned_antibodies, mutation_rate)

        # Step 6: Evaluate mutated clones
        mutated_fitness = calculate_affinity(mutated_antibodies)

        # Step 7: Selection
        population = select_next_generation(mutated_antibodies, mutated_fitness, population_size, dimension)

        # Print best antibody in this generation
        best, best_fit = best_antibody(population)
        print(f"Generation {generation + 1}: Best Solution = {best}, Fitness = {best_fit:.6f}")

    # Final best solution
    best, best_fit = best_antibody(population)
    print(f"\nBest Solution Found: {best}, Fitness = {best_fit:.6f}")
    return best, best_fit

# --- Main Execution ---

# Parameters
population_size = 100
mutation_rate = 0.1
num_generations = 50
num_clones = 10
dimension = 5

# Run the Clonal Selection Algorithm
clonal_selection_algorithm(population_size, mutation_rate, num_generations, num_clones, dimension)
