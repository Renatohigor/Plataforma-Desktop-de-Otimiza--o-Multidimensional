from Model.Tools import*
from random import *


class Abelha:
    # x:      posição da partícula
    # v:      velocidade da particula
    # pBest:  melhor posição encontrada da particula
    x=Ponto()
    limite = 0
    def __init__(self,x,id):
        self.idt=id
        self.x=x
        self.fo = None
        self.fit = None

    def __copy__(self):
        x=Ponto()
        x.v=[i for i in self.x.v]
        aux_belha=Abelha(x=x,id=self.idt)
        aux_belha.fo=self.fo
        aux_belha.fit=self.fit
        aux_belha.Limite= self.limite
        return aux_belha
class Colony:

    def __init__(self,name_arq):
        self.enxame=[]
        self.name_arq=name_arq
        self.arq = open("{}.csv".format(self.name_arq), 'a')



    #########GERADOR DE SOLUÇÕES ALEATÓRIAS############
    # Variáveis: SN (Nº de abelhas empregadas ou assistentes), D (dimensões), b_low (limite inferior dos parâmetros),
    # b_upper (limite superior dos parâmetros).
    def inicializarPopulacao(self,SN, dominio):

        self.enxame=[ Abelha(x=Ponto.Randon(dominio), id=i + 1) for i in range(SN)]



    # FUNÇÃO PARA GERAR SOLUÇÕES ALEATÓRIAS: PROCESSO DA ABELHA ESCOTEIRA
    def gerarNovaSolucao(self,posicaoPiorLimite, dominio):  # Recebe o número de dimensões e os limites inferiores e superiores das variáveis
        return  Abelha(x=Ponto.Randon(dominio), id=posicaoPiorLimite)


        # Função para avaliar as soluções
    # CALCULA O FITNESS DO CONJUNTO DE SOLUÇÕES
    def aval_sol_Fitness(self,f):
        for abelha in self.enxame:
            abelha.fo = (f << abelha.x)
            abelha.fit = 1 / (1 + abelha.fo) if abelha.fo >= 0 else 1 + abs(abelha.fo)


    # FUNÇÃO PARA GERAR SOLUÇÃO VIZINHA
    def solucao_vizinha(self,xij, xkj, limite_inf,limite_sup):  # Recebe dois parâmetros onde: j e k são aleatórios, k é diferente de i
        Phi = random()
        Phi *= -1 if randint(0, 9) % 2 else 1
        self.text_arq += ";;Phi [-1,+1];{};\n".format(Phi)
        self.text_arq += ";;Phi(-1,1)*(Xi,j - Xk,j);{};\n".format(Phi * (xij - xkj))
        vij = xij + Phi * (
                    xij - xkj)  # Equação que calcula vij, este valor será substituido em X[i] para gera a solução vizinha

        self.text_arq += ";;Vij=Xi,j+Phi(-1,1)*(Xi,j - Xk,j);{};\n".format(vij)

        if vij > limite_sup:  # Condição para que as variáveis estejam sempre dentro do limite estabelecido
            vij = limite_sup  # variável recebe limite superior se valor da equação for maior
        elif vij < limite_inf:
            vij = limite_inf
        return vij

    # FUNÇÃO ATUALIZAR SOLUÇÃO:
    # PROCESSO EM QUE TANTO AS ABELHAS EMPREGADAS, QUANTO AS ASSISTENTES TENTAM MELHORAR O CONJUNTO DE SOLUÇÕES
    def atualizarSolucao(self ,indice,roleta=None,text=None):

        # Aplicar Estrutura De Vizinhanca para escolha dos parâmetros para a função solucao_vizinha
        self.text_arq+=";I={};(ORIGINAL BEE = {});Xi;{}\n\n".format(
            indice,
            self.enxame[indice].idt,
            trat_list(self.enxame[indice].x.v)
        )
        xi =self.enxame[indice].__copy__() # Variável que recebe a solução a ser melhorada
        if roleta is not None:
             self.text_arq += text
             self.text_arq += ";;Roullet whell bee (0, 1);Roleta;{};\n".format(roleta)

        k = choice(range(self.SN))  # Indice que representa a linha (ou solução) vizinha a ser trabalhada
        while k == indice:  # Loop para assegurar que k seja diferente se i
            k = choice(range(self.SN))  # Enquanto k é igual a i gera-se novas soluções
        self.text_arq+=";;neighbor solution (1 < k < Npop) excluded i bee;k;{};xk;{}\n".format(
            k,
            trat_list(self.enxame[k].x.v)
        )

        j=len(self.domain_vet[-1])-1
        j = randint(0,j) # indice que representa a coluna (é escolhida aleatórimente)
        self.text_arq+=";;aleatory dimension (1 < j < D);j;{};\n".format(j)

        xij = xi.x.v[j]  # Definição de xij, um dos parâmetros da função solucao_vizinha
        xkj = self.enxame[k].x.v[j]  # Definição do segundo parâmetro (xkj) da função solucao_vizinha
        self.text_arq+=";;Xi.j;{};\n".format(xij)
        self.text_arq+=";;Xk.j;{};\n".format(xkj)


        vij = self.solucao_vizinha(xij, xkj,self.domain_vet[0][j], self.domain_vet[-1][j])  # Variável recebe o valor da função solucao_vizinha
        xi.x.v[j] = vij  # Na solução a ser melhorada, adiciona-se o valor de vij, e so então é que se tem a solução vizinha
        print('xi.fo',xi.fo)
        xi.fo = (self.f << xi.x)
        print('xi.fo',xi.fo)
        xi.fit = 1 / (1 + xi.fo) if xi.fo >= 0 else 1 + abs(xi.fo)
        self.text_arq += ";;New Xi;{};\n".format(trat_list(xi.x.v))
        self.text_arq += ";;FO New Xi (Vi);{};\n".format(xi.fo)
        self.text_arq += ";;FIT New Xi (Vi);{};\n".format(xi.fit)

        ## Avaliar fitness da nova solução
        if (xi.fo)  < self.enxame[indice].fo :  # Condição para troca da solução antiga pela solução vizinha
            self.enxame[indice].x.v = [i  for i in xi.x.v]  # Se a condição for verdade, o item da matriz Fitness que corresponde ao valor indice, recebe o novoFitness
            self.enxame[indice].fo = (self.f << self.enxame[indice].x)
            self.enxame[indice].fit = 1 / (1 + self.enxame[indice].fo) if self.enxame[indice].fo >= 0 else 1 + abs(self.enxame[indice].fo)# Se verdade, a solução antiga é substituida pela novaSolução
            self.enxame[indice].limite = 0  # Se verdade, a solução foi melhorada e o contador de limite recebe 0(zero)
            Accept_moviment="Yes"
        else:
            Accept_moviment="No"
            self.enxame[indice].limite += 1  # Se for falso nada acontece e o contador recebe um incremento de 1(um)


        self.text_arq += ";;Accept moviment ?;{};\n".format(Accept_moviment)
        self.text_arq += ";;X[i] = New Xi;{};\n".format(trat_list( self.enxame[indice].x.v))
        self.text_arq += ";;Limit[i];{};\n\n".format(self.enxame[indice].limite)


    # ROLETA PROBABILISTICA USADA PELA ABELHA ASSISTENTE PARA ESCOLHER QUAL SOLUÇÃO IRÁ TRABALHAR
    def aplicarRoletaProbabilistica(self):
        # Calcular matriz de probabilidade de cada solução e normaliza-la
        valorTotalFitness = sum([abelha.fit for abelha in self.enxame])
        probabilidadePi = [(abelha.fit  / valorTotalFitness) for abelha in self.enxame ]  # Variável que receberá as probabilidades de cada solução da matriz X
          # A probabilidade é adicionada a matriz probabilidadePi

        probabilidadeNormalizada = []  # Variável que receberá as probabilidades normalizadas
        aux2 = 0  # Variável que auxiliará na soma acumulativa das probabilidades
        for i in probabilidadePi:
            aux2 += i
            probabilidadeNormalizada.append(aux2)  # Normalização

        roleta = random() # Gera-se um valor aleatório entre 0 e 1 para escolha da solução a ser melhorada pela onlooker bee
        posicao = 0  # Variável que receberá de aux3 a posição da solução escolhida
        for i in range(self.SN):  # Loop para acessar os valores da matriz probabilidadeNormalizada

            if roleta >= probabilidadeNormalizada[i]:  # Condição para encontrar o maior valor de i que satisfaça: roleta <= i
                posicao = i  # Se verdade posição recebe aux3 (indice da matriz)
            else:
                posicao = i
                break  # Se falso aux3 recebe incremento e retorna o Loop
        return posicao,roleta ,";;Normalized probability;{};\n".format(trat_list( probabilidadeNormalizada)) # Retorno da função

        # METODO: RANNQUIANDO OS INDIVIDUOS
        # NESSE METODO A POPULAÇÃO DO ENXAME E RANQUEADA DE ACORDO COM SEU VALOR DE FUNÇÃO OBJETIVO

    def ranking(self):
        media = 0

        self.enxame.sort(key=lambda x: x.fo)
        for i in self.enxame:
            media += i.fo
        return media
    def print_pop(self):
        self.aval_sol_Fitness(self.f)
        self.text_arq += "Solution (Xi);INIDIVIDUAL;{};FO;FIT".format(
            trat_list(
                ['Xj{}'.format(i + 1) for i in range(len(self.domain_vet[-1]))]
            )
        )
        self.text_arq += "\n"
        for i in self.enxame:
            self.text_arq += ";{};{};{};{}\n".format(i.idt, trat_list(i.x.v), i.fo, i.fit)
        self.text_arq += "\n"

    def ABC(self, f,domain,SN,MCN,NT,D,limite,functiom_descr ):

        self.f = f
        self.domain = domain
        self.domain_vet = [domain[0].v, domain[-1].v]
        self.SN = SN
        self.CS = SN * 2
        self.limite = SN * D
        self.D = D
        self.MCN = MCN
        self.NT = NT
        self.limite = limite
        Melhor_fo = MelhorSolucao = inf

        self.text_arq=";GENERAL SETUP\n"
        self.text_arq+=";Npop;{}\n".format(self.SN)
        self.text_arq+=";Nger;{}\n".format(self.NT)
        self.text_arq+=";Stop criteria;Nger\n"
        self.text_arq+=";AGORITHM SETUP\n"
        self.text_arq+=";Limit for Scout Bee = ;{}\n".format(self.SN*D)
        self.text_arq+=";PROBLEM\n"
        self.text_arq+=";NAME;{}\n".format(functiom_descr[-2])
        self.text_arq+=";Number of Dimensions (D);{}\n".format(functiom_descr[-1])
        self.text_arq += ";INTERVAL\n"
        self.text_arq += ";INTERVAL MIN.;{}\n".format(trat_list(self.domain_vet[0]))
        self.text_arq += ";INTERVAL MAX.(D);{}\n".format(trat_list(self.domain_vet[-1]))

        # GERAR SOLUÇÕES ALEATÓRIAS A AVALIA-LAS (CALCULAR FITNESS)
        self.text_arq+="INITIAL POPULATION (X)\n"
        self.text_arq += "Solution (Xi);INIDIVIDUAL;{};{};{}".format(
            trat_list(
                ['Xj{}'.format(i + 1) for i in range(len(self.domain_vet[-1]))]
            ),
            "FO",
            "FIT"
        )
        self.text_arq += "\n"
        self.inicializarPopulacao(self.SN, self.domain_vet)  # Variável que recebe a matriz de soluções iniciais
        self.aval_sol_Fitness(self.f)
        for i in self.enxame:
            self.text_arq += "x{};{};{};{};{}\n".format(self.enxame.index(i) + 1, self.enxame.index(i) + 1,
                                                        trat_list(i.x.v), i.fo, i.fit)
        self.text_arq += "\n\n"
        list_fo = [i.fo for i in self.enxame]
        Melhor_fo = list_fo.index(min(list_fo))
        self.text_arq += ";Best_fo;{}\n".format(self.enxame[Melhor_fo].fo)
        self.text_arq += ";Best_solution;{}\n\n".format(trat_list(self.enxame[Melhor_fo].x))
        cont=1
        for i in range(self.NT):


            # INÍCIO DAS ITERAÇÕES DE CADA SIMULÇÃO (NT)
            for cont1 in range(MCN):
                self.text_arq += ";ITERATION;{}\n".format(cont)
                cont += 1

                # INÍCIO DO PROCESSO DAS ABELHAS EMPREGADAS:
                self.text_arq += ";EMPLOYED BEE PHASE\n"
                for cont2 in range(SN): self.atualizarSolucao(cont2) # Recebe o conjunto de soluções X e tenta melhora-las por greedy selection
                self.print_pop()
                # INÍCIO DO PROCESSO DAS ABELHAS ASSISTENTES:
                self.text_arq += "; Onlooker BEE PHASE\n"
                for cont3 in range( SN):  # Loop para acionar cada abelha assistente e enviá-las pra melhorar as soluções escolhidas
                    posicaoEscolhida,roleta,text= self.aplicarRoletaProbabilistica()  # Variável recebe a posição escolhida
                    self.atualizarSolucao(posicaoEscolhida,roleta,text)  # Função que atualiza as solução da posição escolhida

                self.print_pop()

                # INÍCIO DO PROCESSO DA ABELHA ESCOTEIRA
                posicaoPiorLimite = [ab.limite for ab in self.enxame].index(
                    max([ab.limite for ab in self.enxame]))  # Define-se qual é a pior solução, ou seja, qual é a mai
                if [ab.limite for ab in self.enxame][posicaoPiorLimite] >= self.limite:  # Se a condição for verdade:
                    self.enxame[posicaoPiorLimite] = self.gerarNovaSolucao(dominio=self.domain_vet,posicaoPiorLimite=posicaoPiorLimite)


                # DEFINIR MELHOR SOLUÇÃO DE CADA ITERAÇÃO MCN:
                self.aval_sol_Fitness(self.f)
                best_fo_cycle = min([i.fo for i in self.enxame])
                list_fo = [i.fo for i in self.enxame]
                best_sol_cycle = list_fo.index(min(list_fo))

                fo_bool="NO"
                # MEMORIZAR MELHOR SOLUÇÃO
                if best_fo_cycle < Melhor_fo:

                    Melhor_fo = best_fo_cycle
                    MelhorSolucao = best_sol_cycle
                    fo_bool="Yes"

                self.text_arq += ";Memorize Best Solution\n"
                self.text_arq += ";;Best_fo_cycle;{}\n".format(best_sol_cycle)
                self.text_arq += ";;Best_fo_cycle < Melhor_fo?;{}\n".format(fo_bool)
                self.text_arq += ";Best_fo;{}\n".format(Melhor_fo)

            # GERAR SOLUÇÕES ALEATÓRIAS A AVALIA-LAS (CALCULAR FITNESS)
            self.inicializarPopulacao(self.SN, self.domain_vet)  # Variável que recebe a matriz de soluções iniciais
            self.aval_sol_Fitness(self.f)
            list_fo = [i.fo for i in self.enxame]
            Melhor_fo = list_fo.index(min(list_fo))
        self.arq.write(self.text_arq.replace('.',','))

        return Melhor_fo,MelhorSolucao




