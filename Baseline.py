from Individual import Individual
from Population import Population
from InitClass import InitClass
import numpy
import random

class Baseline:
    population = None
    generationCount = 0
    numberOfIndividuals = 0
    place = None
    init = None
    maxfit = None
    numberofGenes = 0
    all = None

    def __init__(self, pop):
        self.numberOfIndividuals = pop
        self.population = Population(pop)
        self.generationCount = 1
        self.place = Individual(0, 0, 0, 0, 0, 0, 0)
        self.init = InitClass()
        self.maxfit = 0
        self.numberofGenes = 6
        self.all = []
        for individual in (self.population.getIndividuals()):
            self.all.append(individual)

    def addFittestOffspring(self):
        leastFittestIndex = self.population.getLeastFittestIndex()
        self.population.getIndividuals()[leastFittestIndex] = self.place

    def findmax(self):
        for i in range(len(self.population.getIndividuals())):
            if self.maxfit <= self.population.getIndividuals()[i].getFitness():
                self.maxfit = self.population.getIndividuals()[i].getFitness()

    @staticmethod
    def showGeneticPool(individuals):
        print("==All Individuals==")
        increment = 1
        for individual in individuals:
            print("> Individual " + str(increment) + " | " + individual.toString() + " | ")
            increment = increment + 1
        print("===============")

    def doSim(self, a):
        for i in range(len(a)):
            self.population.getIndividuals()[i] = a[i]
        print("Population of " + str(self.population.getPopSize()) + " individual(s).")
        print("Generation: " + str(1) + " Fittest Score: " + str(self.population.getFittestScore()))
        Baseline.showGeneticPool(self.population.getIndividuals())
        # have the while loop condition be whatever you want fitness to attain. For example, while self.maxfit != 16. if you want the final score to be 16
        self.findmax()
        while self.maxfit < 16:
            var = random.randrange(0, 150)
            self.place = Individual(self.init.getfitness()[var], self.init.getGene1()[var], self.init.getGene2()[var],
                                self.init.getGene3()[var], self.init.getGene4()[var], self.init.getGene5()[var],
                                self.init.getGene6()[var])
            counter = 0
            for individual in self.all:
                if individual != None:
                    if Baseline.areSame(individual,self.place):
                        counter = counter + 1
            if counter == 0:
                self.generationCount = self.generationCount + 1
                self.all.append(self.place)
                self.addFittestOffspring()
            #self.addFittestOffspring()
            self.findmax()
            print("")
            print("----------This is a Baseline Test----------")
            print("Generation: " + str(self.generationCount) + " Fittest Score: " + str(self.population.getFittestScore()))
            Baseline.showGeneticPool(self.population.getIndividuals())
            self.place = Individual(0, 0, 0, 0, 0, 0, 0)
            self.population.setFittestScore()
        print("")
        print("Solution found in generation: " + str(self.generationCount))
        print("Index of winner Individual: " + str(self.population.getFittestIndex()))
        print("Fitness: " + str(self.population.getFittestScore()));
        winGenes = numpy.empty(self.numberofGenes, dtype=Individual)
        print("Genes: ")
        for i in range(self.numberofGenes):
            print("Gene: " + str(i + 1) + " " + str(self.population.selectFittest().getGenes()[i]))
        return self.generationCount + 4

    @staticmethod
    def areSame(a, b):
        counter = 0
        for i in range (len(b.getGenes())):
            if a.getGenes()[i] == b.getGenes()[i]:
                counter = counter + 1
        if counter == 6:
            return True
        else:
            return False

'''
test = Baseline(5)
a = []
try:
    for i in range (test.numberOfIndividuals):
        var = random.randrange(0, 150)
        a.append(Individual(test.init.getfitness()[var], test.init.getGene1()[var], test.init.getGene2()[var],
                    test.init.getGene3()[var], test.init.getGene4()[var], test.init.getGene5()[var],
                    test.init.getGene6()[var]))
except:
    None
test.doSim(a)
'''