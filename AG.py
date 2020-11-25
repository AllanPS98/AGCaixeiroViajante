import Populacao
import Individuo
import Cidade
import random as rnd


class AlgoritmoGenetico:

    def __init__(self):
        self.taxaCruzamento = 0
        self.taxaMutacao = 0
        self.geracoes = 0
        self.populacao = []

    def executaAG(self, tam_populacao, geracoes, taxaCruzamento, taxaMutacao):
        cidades = self.criarCidades(10, 20, 20)
        self.populacao = self.criarPopulacao(cidades, tam_populacao)
        self.populacao.printPopulacao()
        self.calulos(cidades)
        self.geracoes = geracoes
        self.taxaCruzamento = taxaCruzamento
        self.taxaMutacao = taxaMutacao
        i = 0
        while i < self.geracoes:
            nova_geracao = []
            print("Geracao {}".format(i + 1))

            for j in range(tam_populacao):
                if j >= (tam_populacao - 40):
                    nova_geracao.append(self.populacao.__getPopulacao__()[j])

            while len(nova_geracao) < tam_populacao:
                posicao1 = rnd.randint(0, tam_populacao - 1)
                posicao2 = rnd.randint(0, tam_populacao - 1)
                pai = self.populacao.__getPopulacao__()[posicao1]
                mae = self.populacao.__getPopulacao__()[posicao2]
                filho1, filho2 = self.cruzamento(pai, mae, taxaCruzamento, len(cidades))
                #print("cruzou", filho2, filho1)
                if filho1 is not None and filho2 is not None:
                    f1, f2 = self.mutacao(filho1, filho2, taxaMutacao)
                    #print("mutou")
                    nova_geracao.append(f1)
                    nova_geracao.append(f2)
            self.populacao.__setPopulacao__(nova_geracao)
            #print("adicionou nova geracao")
            self.calulos(cidades)
            i += 1
        self.populacao.plotSolucao(cidades)

    def cruzamento(self, pai, mae, taxaCruzamento, tam_cromossomo):
        filho1 = None
        filho2 = None
        if rnd.random() < taxaCruzamento:
            mascara1 = []
            mascara2 = []
            for j in range(tam_cromossomo):
                bit = rnd.randint(0, 1)
                mascara1.append(bit)
                bit = rnd.randint(0, 1)
                mascara2.append(bit)
            cromossomo1 = []
            sobras1 = []
            cromossomo2 = []
            sobras2 = []
            #gera o primeiro filho
            for i in range(tam_cromossomo):
                if mascara1[i] == 1:
                    cromossomo1.append(pai.__getCromossomo__()[i])
                else:
                    cromossomo1.append(-1)
                    sobras1.append(pai.__getCromossomo__()[i])
            for gene in mae.__getCromossomo__():
                if sobras1.__contains__(gene):
                    for i in range(len(sobras1)):
                        if sobras1[i] == gene:
                            posicao = i
                            for j in range(len(cromossomo1)):
                                if cromossomo1[j] == -1:
                                    cromossomo1[j] = sobras1[posicao]
                                    break
                            break
            filho1 = Individuo.Individuo()
            filho1.__setCromossomo__(cromossomo1)

            #gera o segundo filho
            for i in range(tam_cromossomo):
                if mascara2[i] == 1:
                    cromossomo2.append(mae.__getCromossomo__()[i])
                else:
                    cromossomo2.append(-1)
                    sobras2.append(mae.__getCromossomo__()[i])
            for gene in pai.__getCromossomo__():
                if sobras2.__contains__(gene):
                    posicao = 0
                    for i in range(len(sobras2)):
                        if sobras2[i] == gene:
                            posicao = i
                            for j in range(len(cromossomo2)):
                                if cromossomo2[j] == -1:
                                    cromossomo2[j] = sobras2[posicao]
                                    break
                            break
            filho2 = Individuo.Individuo()
            filho2.__setCromossomo__(cromossomo2)
            '''
            print("Pai = ", pai.__getCromossomo__())
            print("Mae = ", mae.__getCromossomo__())
            print("Mascara 1 = ", mascara1)
            print("Filho 1 = ", filho1.__getCromossomo__())
            print("Mascara 2 = ", mascara2)
            print("Filho 2 = ", filho2.__getCromossomo__())
            '''
        return filho1, filho2

    def mutacao(self, filho1, filho2, taxaMutacao):
        if rnd.random() < taxaMutacao:
            posicao1 = rnd.randint(0, len(filho1.__getCromossomo__()) - 1)
            posicao2 = rnd.randint(0, len(filho1.__getCromossomo__()) - 1)
            a = filho1.__getCromossomo__()[posicao1]
            filho1.__getCromossomo__()[posicao1] = filho1.__getCromossomo__()[posicao2]
            filho1.__getCromossomo__()[posicao2] = a

        if rnd.random() < taxaMutacao:
            posicao1 = rnd.randint(0, len(filho2.__getCromossomo__()) - 1)
            posicao2 = rnd.randint(0, len(filho2.__getCromossomo__()) - 1)
            a = filho2.__getCromossomo__()[posicao1]
            filho2.__getCromossomo__()[posicao1] = filho2.__getCromossomo__()[posicao2]
            filho2.__getCromossomo__()[posicao2] = a

        return filho1, filho2

    def criarPopulacao(self, cidades, tam_populacao):
        populacao = Populacao.Populacao()
        for i in range(tam_populacao):
            individuo = []
            for cidade in cidades:
                individuo.append(cidade.__getID__())
            rnd.shuffle(individuo)
            populacao.addIndividuo(individuo)
        return populacao

    def criarCidades(self, qtdCidade, limite_x, limite_y):
        cidades = []
        for i in range(qtdCidade):
            cidade = Cidade.Cidade(i + 1, rnd.randint(0, limite_x), rnd.randint(0, limite_y))
            cidades.append(cidade)
        return cidades

    def calulos(self, cidades):
        self.populacao.calculaFitness(cidades)

