from GeneticAlgo import GeneticALGO
from Baseline import Baseline
from InitClass import InitClass
from Individual import Individual
import numpy
import random


class Evaluator:
    arr1 = []
    arr2 = []
    one = GeneticALGO(5)
    two = Baseline(5)
    trialnum = 0
    numind = 0
    init = None
    val1 = 0
    val2 = 0

    def __init__(self, trialNum, numInd):
        self.trialnum = trialNum
        self.one = GeneticALGO(numInd)
        self.two = Baseline(numInd)
        self.val1 = 0
        self.val2 = 0
        self.init = InitClass()
        self.numind = numInd


tester = InitClass()
test = Evaluator(1000, 5)
first = 0
second = 0
test.arr1 = numpy.empty(test.trialnum, dtype=object)
test.arr2 = numpy.empty(test.trialnum, dtype=object)
for i in range(test.trialnum):
    test.arr1[i] = 0
    test.arr2[i] = 0
for x in range(test.trialnum):
    #print("--- Test Number " + str(x) + " ---")
    one = GeneticALGO(5)
    two = Baseline(5)
    a = []
    for i in range(test.numind):
        var = random.randrange(0, 150)
        a.append(Individual(test.init.getfitness()[var], test.init.getGene1()[var], test.init.getGene2()[var],
                            test.init.getGene3()[var], test.init.getGene4()[var], test.init.getGene5()[var],
                            test.init.getGene6()[var]))
    first = one.doSim(a)
    second = two.doSim(a)
    test.arr1[x] = first
    test.arr2[x] = second
    test.val1 = test.val1 + test.arr1[x]
    test.val2 = test.val2 + test.arr2[x]
print("Genetic Value is " + str(test.val1 / test.trialnum))
print("Random Value is " + str(test.val2 / test.trialnum))
