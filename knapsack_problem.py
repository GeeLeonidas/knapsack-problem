from copy import *
from math import *

from typing import Callable

import random


class GeneticAlgorithmn:
    def __init__(self, bits_per_individual: int, population_size: int):
        new_individual = lambda: [random.choice([0, 1]) for _ in range(bits_per_individual)]
        self.population = [ new_individual() for _ in range(population_size)]
        self.fitness = [ -inf for _ in range(population_size) ]
        self.next_population = []

    def find_best_individual(self) -> int:
        best_idx = 0
        for idx in range(len(self.population)):
            if self.fitness[idx] > self.fitness[best_idx]:
                best_idx = idx
        return best_idx

    def select_individual(self) -> list:
        pass

    def fitness_phase(self, eval_function: Callable):
        pass

    def crossover_phase(self, children_number: int):
        pass

    def mutation_phase(self, mutant_number: int):
        pass

    def selection_phase(self, selected_number: int):
        pass

    def switch_to_next_generation(self):
        self.population = deepcopy(self.next_population)
        self.next_population = []


def fitness_function(individual: list) -> float:
    items = [
        # Nome | Preço | Peso
        ("Barraca", 150, 3.5)
        ("Saco de dormir", 100, 2.0)
        ("Isolante térmico", 50, 0.5)
        ("Colchão inflável", 80, 1.0)
        ("Lanterna", 30, 0.2)
        ("Kit de primeiros socorros", 20, 0.5)
        ("Repelente de insetos", 15, 0.1)
        ("Protetor solar", 20, 0.2)
        ("Canivete", 10, 0.1)
        ("Mapa e bússola", 25, 0.3)
        ("Garrafa de água", 15, 1.8)
        ("Filtro de água", 50, 0.5)
        ("Comida (ração liofilizada)", 50, 3.0)
        ("Fogão de camping", 70, 1.5)
        ("Botijão de gás", 30, 1.2)
        ("Prato, talheres e caneca", 20, 0.5)
        ("Roupas (conjunto)", 80, 1.5)
        ("Calçados (botas)", 120, 2.0)
        ("Toalha", 20, 0.5)
        ("Kit de higiene pessoal", 30, 0.5)
    ]
    return -inf # TODO: Pontuação do indivíduo (-inf para indivíduos que passarem do limite de peso)


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
        ga.fitness_phase(fitness_function)
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
