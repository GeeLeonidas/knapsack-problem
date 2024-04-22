from copy import *
from math import *

from typing import Callable

import random
import matplotlib.pyplot as plt

# Constants
bits_per_individual = 20
children_number = 20
mutant_number = 10
selected_number = 30
generations = 250

population_size = children_number + mutant_number + selected_number

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

    def select_individual(self, tornament_size = 4) -> list:
        """
        Selects an individual for crossover using tournament selection
        """
        idxs = []

        for _ in range(tornament_size):
            idxs.append(random.randint(0, len(self.population) - 1))

        selected = self.population[idxs[0]]
        best_fitness = self.fitness[idxs[0]]
        for idx in idxs[1:]:
            if self.fitness[idx] > best_fitness:
                best_fitness = self.fitness[idx]
                selected = self.population[idx]
        
        return deepcopy(selected)

    def fitness_phase(self, eval_function: Callable):
        self.fitness = [ eval_function(individual) for individual in self.population ]

    def crossover_phase_one_point(self, children_number: int):
        """
        Executes a one-point crossover on the population
        """
        children = []
        for _ in range(children_number):
            parents = [ self.select_individual(), self.select_individual() ]

            crossover_point = random.randint(1, len(parents[1]) - 2)

            children.append(parents[0][:crossover_point] + parents[1][crossover_point:])

        self.next_population.extend(children)

    def crossover_phase_two_point(self, children_number: int):
        """
        Executes a two-point crossover on the population
        """
        children = []
        for _ in range(children_number):
            parents = [ self.select_individual(), self.select_individual() ]

            crossover_point_1 = random.randint(1, len(parents[0]) - 2)
            crossover_point_2 = random.randint(1, len(parents[1]) - 2)

            children.append(parents[0][:crossover_point_1] + parents[1][crossover_point_1:crossover_point_2] + parents[0][crossover_point_2:])

        self.next_population.extend(children)

    # Mutação que seleciona m (m = mutant_number) indivíduos diferentes para gerar os mutantes
    def mutation_phase(self, mutant_number: int):
        mutant_idxs = random.sample(range(0, len(self.population) - 1), mutant_number)
        for idx in range(mutant_number):
            mutant_idx = mutant_idxs[idx]
            mutant_bit_idx = random.randint(0, len(self.population[mutant_idx]) - 1)
            mutant = deepcopy(self.population[mutant_idx])
            mutant[mutant_bit_idx] = 1 - mutant[mutant_bit_idx]
            self.next_population.append(mutant)

    # Mutação que pode selecionar o mesmo indivíduo para gerar mais de um mutante
    # Necessidade de armazenar os mutantes para não haver perda de mutante que sofra nova mutação
    def mutation_phase_option_2(self, mutant_number: int):
        mutants = []
        for idx in range(mutant_number):
            mutant_idx = random.randint(0, len(self.population) - 1)
            mutant_bit_idx = random.randint(0, len(self.population[mutant_idx]) - 1)
            mutant = deepcopy(self.population[mutant_idx])
            mutant[mutant_bit_idx] = 1 - mutant[mutant_bit_idx]
            mutants.append(mutant)
        self.next_population.extend(mutants)

    def selection_phase(self, selected_number: int):
        pass # TODO: Selecionar k indivíduos para a próxima geração (k = `selected_number`)

    def switch_to_next_generation(self):
        self.population = self.next_population
        self.next_population = []


def fitness_function(individual: list, items: list) -> float:
    total_weight = 0
    total_cost = 0
    for idx, bit in enumerate(individual):
        if bit != 0:
            total_cost += items[idx][1]
            total_weight += items[idx][2]
        
    if total_weight <= 15:
        return total_cost # O fitness do indivíduo é o custo total (maior custo => melhor fitness)

    return -inf # Ultrapassou o limite de peso


def fitness_function_option_2(individual: list, items: list) -> float:
    total_weight = 0
    total_cost = 0
    for idx, bit in enumerate(individual):
        if bit != 0:
            total_cost += items[idx][1]
            total_weight += items[idx][2]
        
    if total_weight <= 15:
        return total_cost # O fitness do indivíduo é o custo total (maior custo => melhor fitness)

    return total_cost - (0.5 * total_weight) # Penalidade por passar o limite


def plot_fitness_graphic(fitness: list, generations: int):
    plt.plot(list(range(0, generations)), fitness)
    plt.title("Melhor indivíduo pelas gerações")
    plt.xlabel("Número de gerações")
    plt.ylabel("Melhor fitness")
    plt.show()


def main():
    random.seed()
    
    items = [
        # Nome | Preço | Peso
        ("Barraca", 150, 3.5),
        ("Saco de dormir", 100, 2.0),
        ("Isolante térmico", 50, 0.5),
        ("Colchão inflável", 80, 1.0),
        ("Lanterna", 30, 0.2),
        ("Kit de primeiros socorros", 20, 0.5),
        ("Repelente de insetos", 15, 0.1),
        ("Protetor solar", 20, 0.2),
        ("Canivete", 10, 0.1),
        ("Mapa e bússola", 25, 0.3),
        ("Garrafa de água", 15, 1.8),
        ("Filtro de água", 50, 0.5),
        ("Comida (ração liofilizada)", 50, 3.0),
        ("Fogão de camping", 70, 1.5),
        ("Botijão de gás", 30, 1.2),
        ("Prato, talheres e caneca", 20, 0.5),
        ("Roupas (conjunto)", 80, 1.5),
        ("Calçados (botas)", 120, 2.0),
        ("Toalha", 20, 0.5),
        ("Kit de higiene pessoal", 30, 0.5),
    ]
    
    eval_function = lambda individual: fitness_function(individual, items)
    ga = GeneticAlgorithmn(bits_per_individual, population_size)
    fitness_history = [] # Armazena melhor fitness por geração
    for n in range(generations):
        ga.fitness_phase(eval_function)
        ga.crossover_phase_one_point(children_number)
        ga.mutation_phase(mutant_number)
        ga.selection_phase(selected_number)

        best_idx = ga.find_best_individual()
        fitness_history.append(ga.fitness[best_idx])
        print("\nGENERATION ", n+1)
        print("Best fitness: ", ga.fitness[best_idx])
        print("Individual:   ", ga.population[best_idx])

        ga.switch_to_next_generation()

    plot_fitness_graphic(fitness_history, generations)

if __name__ == "__main__":
    main()
