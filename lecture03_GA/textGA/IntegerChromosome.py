
from random import randint, seed, uniform, sample

def generateNewValue(lim1, lim2):
    return randint(lim1, lim2)
 
# integer representation
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        # # random values, without constraints
        # self.__repres = [generateNewValue(0,problParam['noChars']) for _ in range(problParam['noDiffChars'])] 
        # random values with constraints
        indexes = [i for i in range(problParam['noChars'])]
        self.__repres = sample(indexes, problParam['noDiffChars'])
        self.__fitness = 0.0
    
    @property
    def repres(self):
        return self.__repres 
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
    
    def crossover(self, c):
        offspring = Chromosome(self.__problParam)
        cuttingPoint = randint(0, self.__problParam['noDiffChars'] - 1)
        offspring.__repres = [self.__repres[i] if i < cuttingPoint else c.__repres[i] for i in range(self.__problParam['noDiffChars'])]    
        return offspring
    
    def mutation(self):
        pos = randint(0, self.__problParam['noDiffChars'] - 1)
        self.__repres[pos] = generateNewValue(0,self.__problParam['noChars'])
        
    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness