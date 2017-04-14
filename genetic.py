import random
import board
import console
import time

cross = 0.7
mutation = 0.001
pop_size = 100
chromo_length = 104
gene_length = 4
max_gens = 400
gens = 0

def fitness(population):
    for i in range(0, len(population)):
        chromosome = population[i]['dna']
        splitUp = [chromosome[j:j+4] for j in range(0, len(chromosome), 4)]
        decoded = [int(byte, 2) for byte in splitUp]
        for j in range(0, 13):
            if board.move(decoded[j], decoded[j+1]):
                population[i]['fitness'] += 1
                console.printBoard()
            j += 1
        board.setBoard()
        console.println("Generation: " + str(gens) + " Genome: " + str(i) + " Fitness: " + str(population[i]['fitness']))
        #time.sleep()

def chooseParent(population):
    maximum = sum([child['fitness'] for child in population])
    pick = random.uniform(0, maximum)
    current = 0
    for child in population:
        current += child['fitness']
        if current > pick:
            return child['dna']

def crossover(a, b):
    if random.uniform(0, 1) <= cross:
        length = len(a)
        gene = int(random.uniform(0, length))
        new_a = a[:gene] + b[gene:]
        new_b = b[:gene] + a[gene:]
        splitUp_a = [a[i:i+4] for i in range(0, len(a), 4)]
        splitUp_b = [b[i:i+4] for i in range(0, len(b), 4)]
        decoded_a = [int(byte, 2) for byte in splitUp_a]
        decoded_b = [int(byte, 2) for byte in splitUp_b]
        splitUp_aNew = [new_a[i:i+4] for i in range(0, len(new_a), 4)]
        splitUp_bNew = [new_b[i:i+4] for i in range(0, len(new_b), 4)]
        decoded_aNew = [int(byte, 2) for byte in splitUp_aNew]
        decoded_bNew = [int(byte, 2) for byte in splitUp_bNew]
        print("Gene: " + str(gene))
        print("Old a: ",end='')
        print(decoded_a, end='')
        print(" | New a: ", end='')
        print(decoded_aNew)
        print("Old b: ", end='')
        print(decoded_b, end='')
        print(" | New b: ", end='')
        print(decoded_bNew)
        a = new_a
        b = new_b

def mutate(dna):
    for bit in dna:
        if random.uniform(0, 1) <= mutation:
            if bit == '0':
                bit = '1'
            else:
                bit = '0'

def randomBits(length):
    bits = ""
    for i in range(0, length):
        if random.uniform(0, 1) > 0.5:
            bits += '1'
        else:
            bits += '0'
    return bits

population = [None] * pop_size
for i in range(0, pop_size):
    population[i] = {'dna': randomBits(chromo_length), 'fitness': 0}
gens = 0
found = False
while not found:
    fitness(population)
    for child in population:
        if child['fitness'] == 13:
            found = True
            break
    temp = [None] * pop_size
    cPop = 0
    while cPop < pop_size:
        offspring1 = chooseParent(population)
        offspring2 = chooseParent(population)
        crossover(offspring1, offspring2)
        mutate(offspring1)
        mutate(offspring2)
        temp[cPop] = {'dna': offspring1, 'fitness': 0}
        cPop += 1
        temp[cPop] = {'dna': offspring2, 'fitness': 0}
        cPop += 1
    population = temp
    gens += 1
    if gens > max_gens:
        console.println("No solution found this run")
        found = True
