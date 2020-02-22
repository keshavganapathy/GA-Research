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
    numberOfIndividuals = 0
    place = None
    init = None
    maxfit = None
    numberofGenes = 0

    def __init__(self, pop):
        self.numberOfIndividuals = pop
        self.population = Population(pop)
        self.generationCount = 1
        self.fittest = Individual(0, 0, 0, 0, 0, 0, 0)
        self.secondFittest = Individual(0, 0, 0, 0, 0, 0, 0)
        self.place = Individual(0, 0, 0, 0, 0, 0, 0)
        self.init = InitClass()
        self.maxfit = 0
        self.numberofGenes = 6

    def selection(self):
        self.fittest = self.population.selectFittest()
        self.secondFittest = self.population.selectSecondFittest()

    def addFittestOffspring(self):
        leastFittestIndex = self.population.getLeastFittestIndex()
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
        for x in range(150):
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
        for i in range(len(self.population.getIndividuals())):
            if self.maxfit <= self.population.getIndividuals()[i].getFitness():
                self.maxfit = self.population.getIndividuals()[i].getFitness()

    def mutation(self):
        ran = random.randrange(0, len(self.population.getIndividuals()))
        ran1 = random.randrange(0, len(self.population.getIndividuals()[0].getGenes()) + 1)
        var = random.randrange(0, 150)
        if ran1 == 0:
            self.population.getIndividuals()[ran].getGenes()[ran1] = self.init.getGene1()[var]
        elif ran1 == 1:
            self.population.getIndividuals()[ran].getGenes()[ran1] = self.init.getGene2()[var]
        elif ran1 == 2:
            self.population.getIndividuals()[ran].getGenes()[ran1] = self.init.getGene3()[var]
        elif ran1 == 3:
            self.population.getIndividuals()[ran].getGenes()[ran1] = self.init.getGene4()[var]
        elif ran1 == 4:
            self.population.getIndividuals()[ran].getGenes()[ran1] = self.init.getGene5()[var]
        elif ran1 == 5:
            self.population.getIndividuals()[ran].getGenes()[ran1] = self.init.getGene6()[var]
        elif ran1 == 6:
            self.population.getIndividuals()[ran].setFitness(self.init.getfitness()[var])
        for x in range(150):
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

    @staticmethod
    def showGeneticPool(individuals):
        print("==All Individuals==")
        increment = 1
        for individual in individuals:
            print("> Individual " + str(increment) + " | " + individual.toString() + " | ")
            increment = increment + 1
        print("===============")

# pass initial population size
test = GeneticALGO(5)
a = []
try:
    for i in range (test.numberOfIndividuals):
        var = random.randrange(0, 150)
        a.append(Individual(test.init.getfitness()[var], test.init.getGene1()[var], test.init.getGene2()[var],
                    test.init.getGene3()[var], test.init.getGene4()[var], test.init.getGene5()[var],
                    test.init.getGene6()[var]))
except:
    None
for i in range (len(a)):
    test.population.getIndividuals()[i] = a[i]
print("Population of " + str(test.population.getPopSize()) + " individual(s).")
print("Generation: " + str(1) + " Fittest Score: " + str(test.population.getFittestScore()))
GeneticALGO.showGeneticPool(test.population.getIndividuals())
# have the while loop condition be whatever you want fitness to attain. For example, while test.maxfit != 16. if you want the final score to be 16
while test.maxfit < 16:
    test.generationCount = test.generationCount + 1
    test.selection()
    test.crossover()
    var = random.randrange(0, 8)
    if var == 1:
        test.mutation()
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
test.population.setFittestScore()
print("")
print("Solution found in generation: " + str(test.generationCount))
print("Index of winner Individual: " + str(test.population.getFittestIndex()))
print("Fitness: " + str(test.population.getFittestScore()));
winGenes = numpy.empty(test.numberofGenes, dtype=Individual)
print("Genes: ")
for i in range(test.numberofGenes):
    print("Gene: " + str(i + 1) + " " + str(test.population.selectFittest().getGenes()[i]))
