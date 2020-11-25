import Individuo
import Cidade
import math as mt
import matplotlib.pyplot as mtp


class Populacao:

    def __init__(self):
        self.list_individuos = []

    def addIndividuo(self, cromossomo):
        ind = Individuo.Individuo()
        ind.__setCromossomo__(cromossomo)
        self.list_individuos.append(ind)

    def __getPopulacao__(self):
        if len(self.list_individuos) != 0:
            return self.list_individuos
        return []

    def __setPopulacao__(self, populacao):
        self.list_individuos = populacao.copy()

    def __getIndividuo__(self, i):
        return self.list_individuos[i]

    def calculaFitness(self, cidades):
        for individuo in self.list_individuos:
            somaDistancia = 0
            for i in range(len(individuo.__getCromossomo__()) - 1):
                id_atual = individuo.__getCromossomo__()[i]
                prox_id = individuo.__getCromossomo__()[i + 1]
                x1 = cidades[id_atual - 1].__getX__()
                y1 = cidades[id_atual - 1].__getY__()
                x2 = cidades[prox_id - 1].__getX__()
                y2 = cidades[prox_id - 1].__getY__()
                distancia = mt.sqrt(mt.fabs(((x2 - x1)**2) + ((y2 - y1)**2)))
                somaDistancia += distancia
            individuo.__setFitness__(somaDistancia)
        self.list_individuos.sort(key=Individuo.Individuo.__getFitness__, reverse=True)

    def printPopulacao(self):
        for individuo in self.list_individuos:
            print(individuo.__getCromossomo__(), " / ",
                  "Fitness : ", individuo.__getFitness__())

    def __getMediaPopulacao__(self):
        soma = 0
        for individuo in self.list_individuos:
            soma = soma + individuo.__getFitness__()
        return soma / len(self.list_individuos)

    def plotSolucao(self, cidades):
        x = []
        y = []
        i = 0
        for individuo in self.list_individuos:
            print(individuo.__getCromossomo__(), ":", individuo.__getFitness__())
            if i == (len(self.list_individuos) - 1):
                for indice in individuo.__getCromossomo__():
                    x.append(cidades.__getitem__(indice - 1).__getX__())
                    y.append(cidades.__getitem__(indice - 1).__getY__())
            i += 1
        mtp.plot(x, y, 'r o')
        mtp.plot(x, y, 'g-')
        mtp.show()
