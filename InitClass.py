import numpy
import pandas as pd


class InitClass:
    fitness = None
    gene1 = None
    gene2 = None
    gene3 = None
    gene4 = None
    gene5 = None
    gene6 = None

    def __init__(self):
        print("start")
        filename1 = 'ja-en.evals'
        filename2 = 'ja-en.hyps'
        tab1 = pd.read_csv(filename1)
        tab2 = pd.read_csv(filename1)
        print(tab1.dtypes)
        print(tab2.dtypes)
        print("end")

    def getGene1(self):
        return self.gene1

    def getGene2(self):
        return self.gene2

    def getGene3(self):
        return self.gene3

    def getGene4(self):
        return self.gene4

    def getGene5(self):
        return self.gene5

    def getGene6(self):
        return self.gene6

    def getfitness(self):
        return self.fitness

test = InitClass()