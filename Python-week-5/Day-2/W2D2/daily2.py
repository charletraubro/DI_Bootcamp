import random

ZERO_ONE = [0,1]

class Gene:

    def __init__(self):
        self.val = random.choice(ZERO_ONE)

    def __flip(self):
        # 1 - 1 => 0
        # 1 - 0 => 1
        self.val = 1 - self.val 
    
    def mutate(self):
        self.__flip()

    def __str__(self):
        return str(self.val)

class Chromosome:
    
    def __init__(self):
        self.genes = [Gene() for i in range(10)]

    def mutate(self, threshold: int):
        for gene in self.genes:
            random_int = random.randint(0, 101)
            if threshold <= random_int:
                gene.mutate()
   
    def __str__(self):
        output = "|".join(list(map(str, self.genes)))
        return output

class DNA:
    
    def __init__(self) -> object:
        self.chromosomes = [Chromosome() for i in range(1)]

    def mutate(self, threshold: int):
        for chromosome in self.chromosomes:
            random_int = random.randint(0, 101)
            if threshold <= random_int:
                chromosome.mutate(threshold)

    def __str__(self):
        output = "\n".join(list(map(str, self.chromosomes)))
        return output 


class Organism:

    def __init__(self, dna: DNA, environment: int) -> object:
        self.dna = dna
        self.environment = environment




def check_ones(dna):
    results = []
    for chromosome in dna.chromosomes:
        result = all(gene == 1 for gene in chromosome.genes)
        results.append(result)
    result_total = all(res == True for res in results)

    return result_total

dna = DNA()
human = Organism(dna, 20)

i = 0
while check_ones(human.dna) == False:
    human.dna.mutate(20)
    print(f'Iteration: {i}\n' + str(human.dna) + '\n')
    i += 1
