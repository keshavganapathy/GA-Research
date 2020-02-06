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

    def __init__(self, pop):
        self.numberOfIndividuals = pop
        self.population = Population(pop)
        self.generationCount = 1
        self.place = Individual(False, 0, 0, 0, 0, 0, 0, 0)
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
        print(leastFittestIndex)
        self.population.getIndividuals()[leastFittestIndex] = self.place

    def crossover(self):
        crossOverPoint = random.randint(0, 5)
        i = 0
        print(crossOverPoint)
        while i < crossOverPoint:
            self.place.getGenes()[i] = self.fittest.getGenes()[i]
            i = i + 1
        print()
        while i < 6:
            self.place.getGenes()[i] = self.secondFittest.getGenes()[i]
            i = i + 1
        x = 0
        while x < len(self.init.getGene1()):
            try:
                if (self.place.getGenes()[0] == self.init.getGene1()[x]) & (
                    self.place.getGenes()[1] == self.init.getGene2()[x]) & (
                    self.place.getGenes()[2] == self.init.getGene3()[x]) & (
                    self.place.getGenes()[3] == self.init.getGene4()[x]) & (
                    self.place.getGenes()[4] == self.init.getGene5()[x]) & (
                    self.place.getGenes()[5] == self.init.getGene6()[x]):
                    self.place.setFitness(self.init.getfitness()[x])
                    break
            except:
                print(x)
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
one = random.randint(0, 148)
two = random.randint(0, 148)
three = random.randint(0, 148)
four = random.randint(0, 148)
five = random.randint(0, 148)
try:
    a = [Individual(True, test.init.getfitness()[one], test.init.getGene1()[one], test.init.getGene2()[one],
                    test.init.getGene3()[one], test.init.getGene4()[one], test.init.getGene5()[one],
                    test.init.getGene6()[one]),
         Individual(True, test.init.getfitness()[two], test.init.getGene1()[two], test.init.getGene2()[two],
                    test.init.getGene3()[two], test.init.getGene4()[two], test.init.getGene5()[two],
                    test.init.getGene6()[two]),
         Individual(True, test.init.getfitness()[three], test.init.getGene1()[three], test.init.getGene2()[three],
                    test.init.getGene3()[three], test.init.getGene4()[three], test.init.getGene5()[three],
                    test.init.getGene6()[three]),
         Individual(True, test.init.getfitness()[four], test.init.getGene1()[four], test.init.getGene2()[four],
                    test.init.getGene3()[four], test.init.getGene4()[four], test.init.getGene5()[four],
                    test.init.getGene6()[four]),
         Individual(True, test.init.getfitness()[five], test.init.getGene1()[five], test.init.getGene2()[five],
                    test.init.getGene3()[five], test.init.getGene4()[five], test.init.getGene5()[five],
                    test.init.getGene6()[five])]
except:
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)

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
