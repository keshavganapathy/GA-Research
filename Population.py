from Individual import Individual
import numpy
import random


class Population:
    popSize = 0
    individuals = []
    fittestScore = 0
    fittest = None
    secondFittest = None

    def __init__(self, popsize):
        self.popSize = popsize
        self.individuals = numpy.empty(popsize, dtype=Individual)
        self.fittest = Individual(0,0,0,0,0,0,0)
        self.secondFittest = Individual(0,0,0,0,0,0,0)


    def selectFittest(self):
        weights = numpy.empty(self.popSize, dtype=object)
        total = 0
        for i in range(len(self.individuals)):
            if i == 0:
                weights[i] = self.individuals[i].getFitness()
            else:
                weights[i] = self.individuals[i].getFitness() + weights[i-1]
            total = total + self.individuals[i].getFitness()
        val = random.uniform(0, total)
        for i in range (len(self.individuals)):
            if i == 0:
                if val < weights[i]:
                    self.fittest = self.individuals[i]
                    self.fittestScore = self.individuals[i].getFitness()
                    return self.individuals[i]
            else:
                if weights[i - 1] < val < weights[i]:
                    self.fittest = self.individuals[i]
                    self.fittestScore = self.individuals[i].getFitness()
                    return self.individuals[i]

    def selectSecondFittest(self):
        self.secondFittest = self.fittest
        while Population.areSame(self.fittest, self.secondFittest):
            weights = numpy.empty(self.popSize, dtype=object)
            total = 0
            for i in range(len(self.individuals)):
                if i == 0:
                    weights[i] = self.individuals[i].getFitness()
                else:
                    weights[i] = self.individuals[i].getFitness() + weights[i - 1]
                total = total + self.individuals[i].getFitness()
            val = random.uniform(0, total)
            for i in range(len(self.individuals)):
                if i == 0:
                    if val < weights[i]:
                        self.secondFittest = self.individuals[i]
                        return self.secondFittest
                else:
                    if weights[i - 1] < val < weights[i]:
                        self.secondFittest = self.individuals[i]
                        return self.secondFittest

    def getLeastFittestIndex(self):
        minFitVal = self.individuals[0].getFitness()
        minFitIndex = 0
        for i in range(len(self.individuals)):
            if minFitVal >= self.individuals[i].getFitness():
                minFitVal = self.individuals[i].getFitness()
                minFitIndex = i
        return minFitIndex

    def getIndex(self, fitness):
        for i in range(len(self.individuals)):
            if self.individuals[i].getFitness() == fitness:
                return i
        return 0

    def getFittestIndex(self):
        maxFit = 0
        maxFitIndex = 0
        for i in range(len(self.individuals)):
            if maxFit <= self.individuals[i].getFitness():
                maxFit = self.individuals[i].getFitness()
                maxFitIndex = i
        return maxFitIndex

    def getPopSize(self):
        return self.popSize

    def setPopSize(self, popsize):
        self.popSize = popsize

    def getIndividuals(self):
        return self.individuals

    def getFittestScore(self):
        return self.fittestScore

    def setFittestScore(self):
        self.fittestScore = 0
        for individual in self.individuals:
            if individual.getFitness() > self.fittestScore:
                self.fittestScore = individual.getFitness()

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