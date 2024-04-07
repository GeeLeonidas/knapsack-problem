from copy import *
from math import *
import random


class GeneticAlgorithmn:
    def __init__(self, bits_per_individual, population_size):
        new_individual = lambda: [random.choice([0, 1]) for _ in range(bits_per_individual)]
        self.population = [ new_individual() for _ in range(population_size)]
        self.fitness = [ -inf for _ in range(population_size) ]
        self.next_population = []

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
    print("Hello World!")


if __name__ == "__main__":
    main()
