from Individual import Individual
from Population import Population
from InitClass import InitClass
import numpy
import random


class GeneticALGO:
    population = None
    fittest = None
    secondFittest = None
    generationCount = 0
    # number of Genes in each ALGO
    numberofGenes = 0
    # total initial pool size
    numberOfIndividuals = 0
    # total generations watned
    genTotal = 5
    # placeholder individual
    place = None
    # data class
    init = None
    # maxfit
    maxfit = None

    def __init__(self, pop):
        self.numberOfIndividuals = pop
        self.population = Population(pop)
        self.generationCount = 1
        self.fittest = Individual(0, 0, 0, 0, 0, 0, 0)
        self.secondFittest = Individual(0, 0, 0, 0, 0, 0, 0)
        self.place = Individual(0, 0, 0, 0, 0, 0, 0)
        self.init = InitClass()
        self.maxfit = 0

    def selection(self):
        self.fittest = self.population.selectFittest()
        self.secondFittest = self.population.selectSecondFittest()

    def addFittestOffspring(self):
        leastFittestIndex = self.population.getLeastFittestIndex()
#        print("Fittest Genes are " + self.fittest.toString())
#        print("Second Fittest Genes are " + self.secondFittest.toString())
#        print("New Genes are " + self.place.toString())
#        print("Least Fittest Index " + str(leastFittestIndex))
        self.population.getIndividuals()[leastFittestIndex] = self.place

    def crossover(self):
        crossOverPoint = random.randrange(1, 5)
        i = 0
        for x in range(crossOverPoint):
            self.place.getGenes()[x] = self.fittest.getGenes()[x]
            i = i + 1
        while i < 6:
            self.place.getGenes()[i] = self.secondFittest.getGenes()[i]
            i = i + 1
        for x in range(149):
            try:
                if (self.place.getGenes()[0] == self.init.getGene1()[x]) & (
                        self.place.getGenes()[1] == self.init.getGene2()[x]) & (
                        self.place.getGenes()[2] == self.init.getGene3()[x]) & (
                        self.place.getGenes()[3] == self.init.getGene4()[x]) & (
                        self.place.getGenes()[4] == self.init.getGene5()[x]) & (
                        self.place.getGenes()[5] == self.init.getGene6()[x]):
                    self.place.setFitness(self.init.getfitness()[x])
            except:
                print("Exception Throwin")
    def findmax(self):
        for i in range(len(self.population.getIndividuals())-1):
            if self.maxfit <= self.population.getIndividuals()[i].getFitness():
                self.maxfit = self.population.getIndividuals()[i].getFitness()

    @staticmethod
    def showGeneticPool(individuals):
        print("==All Individuals==")
        increment = 1
        for individual in individuals:
            print("> Individual " + str(increment) + " | " + individual.toString() + " | ")
            increment +=1
        print("===============")

#pass initial population size
test = GeneticALGO(10)
# number of Genes in each ALGO
test.numberofGenes = 6
# fitness, gene1, gene2, gene3, gene4, gene5, gene6
a = []
try:
    for i in range (test.numberOfIndividuals):
        one = random.randrange(0, 149)
        a.append(Individual(test.init.getfitness()[one], test.init.getGene1()[one], test.init.getGene2()[one],
                    test.init.getGene3()[one], test.init.getGene4()[one], test.init.getGene5()[one],
                    test.init.getGene6()[one]))
except:
    None
i = 0
while i < len(a):
    test.population.getIndividuals()[i] = a[i]
    i += 1
print("Population of " + str(test.population.getPopSize()) + " individual(s).")
print("Generation: " + str(1) + " Fittest Score: " + str(test.population.getFittestScore()))
GeneticALGO.showGeneticPool(test.population.getIndividuals())
i = 0
while test.maxfit < 16:
    test.generationCount = test.generationCount + 1
    test.selection()
    test.crossover()
    # Need to know potential values
    #    if(chance of mutation):
    #        test.mutation()
    counter = 0
    for individual in test.population.individuals:
        if test.place.getFitness() == individual.getFitness():
            counter = counter + 1
    if counter == 0:
        test.addFittestOffspring()
    test.findmax()
    print("")
    print("Generation: " + str(test.generationCount) + " Fittest Score: " + str(test.population.getFittestScore()))
    GeneticALGO.showGeneticPool(test.population.getIndividuals())
    test.place = Individual(0,0,0,0,0,0,0)
    i = i + 1
test.population.setFittestScore()
print("")
print("Solution found in generation: " + str(test.generationCount))
print("Index of winner Individual: " + str(test.population.getFittestIndex()))
print("Fitness: " + str(test.population.getFittestScore()));
winGenes = numpy.empty(test.numberofGenes, dtype=Individual)
print("Genes: ")
for i in range(test.numberofGenes):
    print("Gene: " + str(i + 1) + " " + str(test.population.selectFittest().getGenes()[i]))
