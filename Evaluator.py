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

#avg number test
arrFirst = numpy.empty(3, dtype=object)
arrSecond = numpy.empty(3, dtype=object)
for u in range (3):
    tester = InitClass()
    test = Evaluator(100, 10)
    first = 0
    second = 0
    test.arr1 = numpy.empty(test.trialnum, dtype=object)
    test.arr2 = numpy.empty(test.trialnum, dtype=object)
    for i in range(test.trialnum):
        test.arr1[i] = 0
        test.arr2[i] = 0
    arr = numpy.empty(4, dtype=object)
    ar = numpy.empty(4, dtype=object)
    for i in range (len(arr)):
        arr[i] = 0
        ar[i] = 0
    for x in range(test.trialnum):
        #print("--- Test Number " + str(x) + " ---")
        one = GeneticALGO(test.numind)
        two = Baseline(test.numind)
        a = []
        print(str(test.numind))
        for i in range(test.numind):
            var = random.randrange(0, 150)
            a.append(Individual(test.init.getfitness()[var], test.init.getGene1()[var], test.init.getGene2()[var],
                                test.init.getGene3()[var], test.init.getGene4()[var], test.init.getGene5()[var],
                                test.init.getGene6()[var]))
        first = one.doSim(a)
        if first < 50:
            arr[0] = arr[0] + 1
        elif 50 <= first < 150:
            arr[1] = arr[1] + 1
        elif 150 <= first <= 250:
            arr[2] = arr[2] + 1
        else:
            arr[3] = arr[3] + 1
        second = two.doSim(a)
        if second < 50:
            ar[0] = ar[0] + 1
        elif 50 <= second < 150:
            ar[1] = ar[1] + 1
        elif 150 <= second <= 250:
            ar[2] = ar[2] + 1
        else:
            ar[3] = ar[3] + 1
        test.arr1[x] = first
        test.arr2[x] = second
        test.val1 = test.val1 + test.arr1[x]
        test.val2 = test.val2 + test.arr2[x]
    firstWin = 0
    secondWin = 0
    for i in range (len(test.arr1)):
        if test.arr1[i] < test.arr2[i]:
            firstWin = firstWin + 1
        else:
            secondWin = secondWin + 1
    print("Genetic ALGO out performs baseline " + str(firstWin * 100/(len(test.arr1))) + " percent of the time.")
    print("Baseline out performs Genetic ALGO " + str(secondWin * 100/(len(test.arr1))) + " percent of the time.")
    print("Genetic Value is " + str(test.val1 / test.trialnum))
    print("Random Value is " + str(test.val2 / test.trialnum))
    arrFirst[u] = test.val1 / test.trialnum
    arrSecond[u] = test.val2 / test.trialnum
    for i in range (len(arr)):
        print("Range " + str(i + 1) + " " + str(arr[i]))
    print("----------------------")
    for i in range (len(test.arr1)):
        if test.arr1[i] >= 150:
            print(str(test.arr1[i]))
    print("----------------------")
    print("----------------------")
    print("----------------------")
    print("----------------------")
    print("----------------------")
    for i in range (len(ar)):
        print("Range " + str(i + 1) + " " + str(ar[i]))
    print("----------------------")
    for i in range (len(test.arr2)):
        if test.arr2[i] >= 150:
            print(str(test.arr2[i]))
for i in range (3):
    print("First is " + str(arrFirst[i]))
    print("Second is " + str(arrSecond[i]))