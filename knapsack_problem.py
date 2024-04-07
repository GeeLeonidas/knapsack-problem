from copy import *
from math import *
import random


class GeneticAlgorithmn:
    def __init__(self, bits_per_individual, population_size):
        new_individual = lambda: [random.choice([0, 1]) for _ in range(bits_per_individual)]
        self.population = [ new_individual() for _ in range(population_size)]
        self.fitness = [ -inf for _ in range(population_size) ]
        self.next_population = []

    def find_best_individual(self):
        best_idx = 0
        for idx in range(len(self.population)):
            if self.fitness[idx] > self.fitness[best_idx]:
                best_idx = idx
        return best_idx

    def fitness_phase(self, eval_function):
        pass

    def crossover_phase(self, children_number):
        pass

    def mutation_phase(self, mutant_number):
        pass

    def selection_phase(self, selected_number):
        pass

    def switch_to_next_generation(self):
        self.population = deepcopy(self.next_population)
        self.next_population = []


def main():
    random.seed()
    
    bits_per_individual = 20
    children_number = 20
    mutant_number = 10
    selected_number = 30
    generations = 250
    
    population_size = children_number + mutant_number + selected_number
    ga = GeneticAlgorithmn(bits_per_individual, population_size)
    for n in range(generations):
        ga.fitness_phase(lambda individual: -inf)
        ga.crossover_phase(children_number)
        ga.mutation_phase(mutant_number)
        ga.selection_phase(selected_number)

        best_idx = ga.find_best_individual()
        print("\nGENERATION ", n+1)
        print("Best fitness: ", ga.fitness[best_idx])
        print("Individual:   ", ga.population[best_idx])

        ga.switch_to_next_generation()


if __name__ == "__main__":
    main()
