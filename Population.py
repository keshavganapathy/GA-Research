from Individual import Individual
import numpy


class Population:
    popSize = 0
    individuals = []
    fittestScore = 0

    def __init__(self, popsize):
        self.popSize = popsize
        self.individuals = numpy.empty(popsize, dtype=Individual)

    def selectFittest(self):
        maxFit = 0
        maxFitIndex = 0
        i = 0
        while i < len(self.individuals):
            if maxFit <= self.individuals[i].getFitness():
                maxFit = self.individuals[i].getFitness()
                maxFitIndex = i
            i = i + 1
        self.fittestScore = self.individuals[maxFitIndex].getFitness()
        return self.individuals[maxFitIndex]

    def selectSecondFittest(self):
        maxFit1 = 0
        maxFit2 = 0
        i = 0
        while i < len(self.individuals):
            if (self.individuals[i].getFitness() > self.individuals[maxFit1].getFitness()):
                maxFit2 = maxFit1
                maxFit1 = 0
            elif (self.individuals[i].getFitness() > self.individuals[maxFit2].getFitness()):
                maxFit2 = i
            i = i + 1
        return self.individuals[maxFit2]

    def getLeastFittestIndex(self):
        minFitVal = self.individuals[0].getFitness()
        minFitIndex = 0
        i = 0
        while i < len(self.individuals):
            if minFitVal >= self.individuals[i].getFitness():
                minFitVal = self.individuals[i].getFitness()
                minFitIndex = i
            i = i + 1
        return minFitIndex

    def getFittestIndex(self):
        maxFit = 0
        maxFitIndex = 0
        i = 0
        while i < len(self.individuals):
            if maxFit <= self.individuals[i].getFitness():
                maxFit = self.individuals[i].getFitness()
                maxFitIndex = i
            i = i + 1
        return maxFitIndex

    def getPopSize(self):
        return self.popSize

    def setPopSize(self, popsize):
        self.popSize = popsize

    def getIndividuals(self):
        return self.individuals

    def getFittestScore(self):
        return self.fittestScore

    def setFittestScore(self, fittestscore):
        self.fittestScore = fittestscore
