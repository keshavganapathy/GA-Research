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
    numval = 0
    init = None
    def __init__(self, trialNum, numVal):
        self.trialnum = trialNum
        self.arr1 = numpy.empty(trialNum, dtype=object)
        self.arr2 = numpy.empty(trialNum, dtype=object)
        self.one = GeneticALGO(numVal)
        self.two = Baseline(numVal)
        self.val1 = 0
        self.val2 = 0
        self.init = InitClass()
        self.numval = numVal

tester = InitClass()
a= []
test = Evaluator(100,5)
val1 = 0
val2 = 0
for i in range(test.numval):
    var = random.randrange(0, 150)
    a.append(Individual(test.init.getfitness()[var], test.init.getGene1()[var], test.init.getGene2()[var],
                        test.init.getGene3()[var], test.init.getGene4()[var], test.init.getGene5()[var],
                        test.init.getGene6()[var]))
for i in range (test.trialnum):
    val1 = test.one.doSimulation(a)
    val2 = test.two.doSimulation(a)
    test.arr1[i] = val1
    test.arr2[i] = val2
for i in range (len(test.arr1)):
    val1 += test.arr1[i]
    val2 += test.arr2[i]
print("Genetic Value is " + str(val1/test.trialnum))
print("Random Value is " + str(val2/test.trialnum))

