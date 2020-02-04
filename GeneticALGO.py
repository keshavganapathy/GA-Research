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
    #placeholder individual
    place = None
    #data class
    init = None

    def __init__(self, pop):
        self.numberOfIndividuals = pop
        self.population = Population(pop)
        self.generationCount = 1
        self.place = Individual(False, 10000, 15.45, 624.7407, 9.238378, 600000, 6791, 36382484)
        self.init = InitClass()

    def selection(self):
        self.fittest = self.population.selectFittest()
        self.secondFittest = self.population.selectSecondFittest()

    def getFittestOffspring(self):
        if self.fittest.getFitness() > self.secondFittest.getFitness():
            return self.fittest
        else:
            return self.secondFittest

    def addFittestOffspring(self):
        leastFittestIndex = self.population.getLeastFittestIndex()
        self.population.getIndividuals()[leastFittestIndex] = self.place

    def crossover(self):
        crossOverPoint = random.randint(0, 5)
        i = 0
        while i < crossOverPoint:
            self.place.getGenes()[i] = self.fittest.getGenes()[i]
            i = i + 1
        i = crossOverPoint
        while i < 6:
            self.place.getGenes()[i] = self.secondFittest.getGenes()[i]
            i = i + 1
        x = 0
        while x < len(self.init.getGene1()):
            if self.place.getGenes()[0] == self.init.getGene1()[x]:
                self.place.setFitness(self.init.getFitness()[x])
                break
            else:
                x = x + 1


    @staticmethod
    def showGeneticPool(individuals):
        print("==All Individuals==")
        increment = 1
        for individual in individuals:
            print("> Individual " + str(increment) + " | " + individual.toString() + " | ")
            increment = increment + 1
        print("===============")


test = GeneticALGO(5)
# change to amount of generations wanted
test.genTotal = 3
# number of Genes in each ALGO
test.numberofGenes = 6
# fitness, gene1, gene2, gene3, gene4, gene5, gene6
a = [Individual(True ,10000, 15.45, 624.7407, 9.238378, 600000, 6791, 36382484),
     Individual(True ,50000, 16.04, 642.0832, 13.622618, 230000, 10739, 106259284),
     Individual(True, 10000, 14.49, 466.7179, 10.352072, 656000, 5685, 3007874),
     Individual(True, 30000, 13.01, 628.8233, 16.078326, 340000, 6555, 26754356),
     Individual(True, 10000, 14.66, 508.1231, 10.122333, 312000, 10745, 64329492)]
i = 0
while i < test.numberOfIndividuals:
    test.population.getIndividuals()[i] = a[i]
    i = i + 1
print("Population of " + str(test.population.getPopSize()) + " individual(s).")
i = 0
print("Generation: " + str(1) + " Fittest Score: " + str(test.population.getFittestScore()))
GeneticALGO.showGeneticPool(test.population.getIndividuals())
while i < test.genTotal:
    test.generationCount = test.generationCount + 1
    test.selection()
    test.crossover()
    # Need to know potential values
    #    if(chance of mutation):
    #        test.muation()
    test.addFittestOffspring()
    test.population.selectFittest()
    print("")
    print("Generation: " + str(test.generationCount) + " Fittest Score: " + str(test.population.getFittestScore()))
    GeneticALGO.showGeneticPool(test.population.getIndividuals())
    i = i + 1
print("")
print("Solution found in generation: " + str(test.generationCount))
print("Index of winner Individual: " + str(test.population.getFittestIndex()))
print("Fitness: " + str(test.population.getFittestScore()));
winGenes = numpy.empty(test.numberofGenes, dtype=Individual)
i = 0
print("Genes: ")
while i < test.numberofGenes:
    print("Gene: " + str(i + 1) + " " + str(test.population.selectFittest().getGenes()[i]))
    i = i + 1
