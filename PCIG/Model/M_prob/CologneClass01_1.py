#@Author: RENATO HIGOR RODRIGUES DA SILVA
#ALGORITMO COLONIA DE VAGALUME (ACV)
#
#
from Model.Tools import *
from Model.pointClass import *

class Firefly:
    position = Ponto()

    #Construtor
    def __init__(self, position,of=None,fit=None, id=None):
        self.position = position
        self.of = of
        self.fit = fit
        self.id = id

    def __str__(self):
        return '{}\t{}\t{}\t{}\n'.format(str(self.id), str(self.position), str(self.of), str(self.fit))

    def __copy__(self):
        return Firefly(position=self.position,of=self.of,fit=self.fit, id=self.id)

    def update_toMove(self, alpha, position_j, beta, d,f):
        dominInferior = Ponto()
        dominSuperior = Ponto()
        dominInferior.v,dominSuperior.v = d[0], d[-1]
        scale= abs(dominSuperior - dominInferior)
        aux_Rand = Ponto.Randon(N = len(self.position.v))
        aux_p = self.position + beta * (position_j - self.position) + alpha * (aux_Rand -0.5)*scale
        aux_p=self.validar_x(aux_p, d)
        aux_fo=f<<aux_p
        aux_fit = 1/(1+aux_fo) if aux_fo >= 0 else 1 + abs(aux_fo)
        aceito_movimento="NAO"
        if self.of >= aux_fo:
            aceito_movimento ="SIM"
            self.position=aux_p
            self.of = aux_fo
            self.fit = aux_fit

        return aceito_movimento is "SIM"

    def validar_x(self, x, d):
        aux= Ponto()
        aux.v=[]
        for i in range(0, len(d[1])):

            if x.v[i] < d[0][i]:
                aux.v.append(d[0][i])
            elif x.v[i] > d[1][i]:
                aux.v.append(d[1][i])
            else:
                aux.v.append(x.v[i])


        return aux



class Colony_01_1:
	#Parametros
    def __init__(self):
        self.n = 0
        self.beta0 = 1.0
        self.alpha = 0.0
        self.numGer = 0
        self.colony = []
        self.last_found = Ponto()
        self.paraAbsorcao = 0.0



    #METODO: GERADOR DE POPULAÇÃO INCIAL
    #NESSE METODO DA POPULAÇÃO INICIAL DO ENXAME É GERADA PELA REGRA DE AMPLITUDE Xk = Xmin + (Xmanx-Xmin).rand
    def generate_Colony(self, dominio):
        self.colony.clear()

        for i in range(0, self.n):
            positionRandom = Ponto.Randon(dominio)
            #print(type(positionRandom))
            self.colony.append(Firefly(position=positionRandom,id=i+1))

    def maximum(self, f):
        maior = self.colony[0].position
        valor_maior = f << maior
        for i in range(1, len(self.colony) - 1):
            valor = f << self.colony[i].position
            if valor_maior < valor:
                valor_maior = valor
                maior = self.colony[i].position
        return maior


    #METODO: AVALIAÇÃO DA FUNÇÃO OBJETIVO
    #NESSE METODDO AVALIA-SE O VALOR DA FUNÇÃO OBJETIVO(FO) E APTIDÃO PARA CADA INDIVIDUO DA POPULAÇÃO
    def evaluateNewSolutions(self, f):
         for firefly in self.colony:
            firefly.of = (f << firefly.position)
            firefly.fit = 1/(1+firefly.of) if firefly.of >= 0 else 1 + abs(firefly.of)

    #METODO: RANNQUIANDO OS INDIVIDUOS
    #NESSE METODO A POPULAÇÃO DO ENXAME E RANQUEADA DE ACORDO COM SEU VALOR DE FUNÇÃO OBJETIVO
    def ranking(self):
        media=0

        self.colony.sort(key=lambda x:x.of)
        for i in self.colony:
            media+=i.of
        return media

    def moveUndivided(self,dim,x):
        ns0 =  [i. __copy__() for i in self.colony]
        aux =''
        for i in range(1, len(self.colony)):

            for j in range(0, i):

                # DISTANCIA EUCLIDIANA
                eucle= Ponto.dist_euclidiana(ns0[i].position.v, ns0[j].position.v)

                # ATRATIVIDADE
                A = eucle ** 2.0
                B = -self.paraAbsorcao * A
                beta = self.beta0 * exp(B)
                mudou=self.colony[i].update_toMove(alpha=self.alpha,position_j= ns0[j].position, beta=beta, d=dim,f=self.f)
                if mudou:
                    i_id = self.colony[i].id - 1
                    j_id = self.colony[j].id
                    self.list_j[i_id]=[j_id,x]

    def main(self, f, dim, n, beta0, alpha, numGer, paraAbsorcao, tetha):
        dim=[dim[0].v,dim[-1].v]
        self.f = f
        self.paraAbsorcao = paraAbsorcao
        self.numGer = int(numGer)
        self.n = n
        self.beta0 = beta0
        self.alpha = alpha
        self.tetha = tetha
        self.generate_Colony(dim)
        self.evaluateNewSolutions(f)
        self.list_j = [[i,0] for i in range(n) ]
        list_conver=[]

        x = 1
        while x <= self.numGer:
            self.ranking()
            list_conver.append(( self.colony[0].position.__copy__(),f<< self.colony[0].position))
            self.alpha = alpha * tetha ** x

            self.moveUndivided(dim,x)

            self.evaluateNewSolutions(f)
            x+=1

        self.ranking()
        list_conver.append((self.colony[0].position.__copy__(), f << self.colony[0].position))

        return list_conver