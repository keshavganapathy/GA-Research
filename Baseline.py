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

    def __init__(self, pop):
        self.numberOfIndividuals = pop
        self.population = Population(pop)
        self.generationCount = 1
        self.place = Individual(0, 0, 0, 0, 0, 0, 0)
        self.init = InitClass()
        self.maxfit = 0

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

    def doSimulation(self, arr):
        a = arr
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
            self.generationCount = self.generationCount + 1
            counter = 0
            if self.place.getFitness() > 16:
                self.maxfit = self.place.getFitness()
                self.population.fittestScore = self.place.getFitness()
            else:
                self.findmax()
            print("")
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
