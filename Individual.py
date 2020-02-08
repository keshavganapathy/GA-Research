import numpy


class Individual:
    geneLength = 0
    fitness = 0
    gene = []

    def __init__(self, Fitness, gene1, gene2, gene3, gene4, gene5, gene6):
        # set to the total num of genes desired
        self.geneLength = 6
        self.gene = numpy.empty(self.geneLength, dtype=object)
        self.gene[0] = (gene1)
        self.gene[1] = (gene2)
        self.gene[2] = (gene3)
        self.gene[3] = (gene4)
        self.gene[4] = (gene5)
        self.gene[5] = (gene6)
        self.fitness = Fitness

    def getGeneLength(self):
        return self.geneLength

    def setGeneLength(self, geneLength):
        self.geneLength = geneLength

    def toString(self):
        returnVal = ""
        returnVal = returnVal + "Fitness " + str(self.fitness) + " Genes:"
        returnVal = returnVal + " "
        i = 0
        while (i < 6):
            returnVal += str(self.gene[i])
            returnVal += " "
            i = i + 1
        return returnVal

    def getFitness(self):
        return self.fitness

    def setFitness(self, Fitness):
        self.fitness = Fitness

    def getGenes(self):
        return self.gene

    def setGenes(self, Genes):
        self.gene = Genes

