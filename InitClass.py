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
        filename1 = 'ja-en.evals'
        filename2 = 'ja-en.hyps'
        tab1 = pd.read_csv(filename1, sep="\t", header=None)
        tab2 = pd.read_csv(filename2, sep="\t", header=None)
        temp1 = []
        temp2 = []
        for column in tab1:
            temp1.append(tab1[column].to_numpy())
        for column in tab2:
            temp2.append(tab2[column].to_numpy())
        self.gene1 = temp2[0]
        self.gene2 = temp2[1]
        self.gene3 = temp2[2]
        self.gene4 = temp2[3]
        self.gene5 = temp2[4]
        self.gene6 = temp2[5]
        self.fitness = temp1[0]

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

print("starting code")
test = InitClass()
for i in range (150):
    print("entered loop")
    print()
    if test.getGene1()[i]  == 10000 and test.getGene2()[i]  == 4 and test.getGene3()[i]  == 512 and test.getGene4()[i]  == 2048 and test.getGene5()[i]  == 16 and test.getGene6()[i]  == .0003:
        print(test.getfitness()[i])
print("did not find anything that fit criteria")