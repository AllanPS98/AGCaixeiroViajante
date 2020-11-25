class Individuo:

    def __init__(self):
        self.cromossomo = []
        self.fitness = 0

    def __getCromossomo__(self):
        if len(self.cromossomo) != 0:
            return self.cromossomo

    def __setCromossomo__(self, cromossomo):
        self.cromossomo = cromossomo.copy()

    def __getFitness__(self):
        return self.fitness

    def __setFitness__(self, fitness):
        self.fitness = fitness

    def mudarBit(self, i):
        if self.cromossomo[i] == 1:
            self.cromossomo[i] = 0
        self.cromossomo[i] = 1

    def printCromossomo(self):
        print(self.cromossomo)