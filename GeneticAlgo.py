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
    all = None

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
        self.all = []
        for individual in (self.population.getIndividuals()):
            self.all.append(individual)

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
        ran1 = random.randrange(0, len(self.population.getIndividuals()[0].getGenes()))
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

    def doSim(self, arr):
        a = arr
        for i in range(len(a)):
            self.population.getIndividuals()[i] = a[i]
        print("Population of " + str(self.population.getPopSize()) + " individual(s).")
        print("Generation: " + str(1) + " Fittest Score: " + str(self.population.getFittestScore()))
        GeneticALGO.showGeneticPool(self.population.getIndividuals())
        # have the while loop condition be whatever you want fitness to attain. For example, while self.maxfit != 16. if you want the final score to be 16
        while self.maxfit < 16:
            self.selection()
            self.crossover()
            var = random.randrange(0, 8)
            if var == 1:
                self.mutation()
            counter = 0
            for individual in self.all:
                if individual != None:
                    if GeneticALGO.areSame(individual,self.place):
                        counter = counter + 1
            if counter == 0:
                self.generationCount = self.generationCount + 1
                self.all.append(self.place)
                self.addFittestOffspring()
            self.findmax()
            print("")
            print("Generation: " + str(self.generationCount) + " Fittest Score: " + str(
                self.population.getFittestScore()))
            GeneticALGO.showGeneticPool(self.population.getIndividuals())
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
        return self.generationCount + 5

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