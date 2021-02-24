#ALGORITMO DE COLÔNIA DE ABELHAS ARTIFICIAS

## Parâmetros do ABC
# CS: Colony size (número total de abelhas - população)
# Limite: quantidade máxima de tentativas de melhorar uma solução que as empregadas ou expectadoras tem antes de buscar uma nova solução, e cada solução tem seu respectivo Limite
# MCN: Número Máximo de Ciclos (Número de iterações)
# SN: Quantidade de abelhas empregadas e expectadoras
# X: soluções/fontes de alimento
# xi: fonte de alimento (cada fonte de alimento possui um Limite'i')
# D: número de dimensões

#LEIA-ME: ENTRE AS LINHAS 14 E 21 ESTÃO AS BIBLIOTECAS IMPORTADAS (NECESSÁRIAS À
# ALGUMAS FUNÇÕES DO ABC OU DE BENCHMARK); eNTRE AS LINHAS 25 E 184 ESTÃO ALGUMAS FUNÇÕES DE
# BENCHMARK UTILIZADAS PARA TESTAE O ALGORITMO (O NUMERO DE DIMENSÕES É DEFINIDO DENTRO DO ESCOPO DESSAS FUNÇÕES;
# ENTRE AS LINHAS 189 E 305 SÃO DEFINIDAS AS FUNÇÕES UTILZADAS NO ALGORITMO; E A PARTIR DA LINHA 306
# COMEÇA O ALGORITMO PROPRIAMENTE DITO.

##############  Bibliotecas importadas  ###########################
import random
import matplotlib.pyplot as plt
import math
import time
from decimal import Decimal
from decimal import ROUND_DOWN
import copy                                        #Biblioteca impotada para acessar a função copy

#------------------------- FUNÇÕES UTILIZADAS --------------------------------#

#Parâmetros função:
nomeFuncao = 'RASTRINGIN FUNCTION'
D = 10               #Número de dimensões
b_low = -600         #Limite inferior
b_upper = 600        #Limite superior

def fun_obj(x):      #entra com um x (vetor de um solução)
    resultado = 0
    for i in range(len(x)):
        resultado += x[i]**2 - 10*math.cos(2*math.pi*x[i]) + 10
    return resultado

##########GERADOR DE SOLUÇÕES ALEATÓRIAS############
#Variáveis: SN (Nº de abelhas empregadas ou assistentes), D (dimensões), b_low (limite inferior dos parâmetros),
# b_upper (limite superior dos parâmetros).
def inicializarPopulacao(SN, D, b_low, b_upper):
    matrizSolucoesIniciais = []
    for i in range(SN):
        linha = []
        [linha.append(b_low + random.random()*(b_upper - b_low)) for j in range(D)]
        matrizSolucoesIniciais.append(linha)
    return matrizSolucoesIniciais

#Função para avaliar as soluções
def aval_sol(X):
    mat_fo = []
    for i in X:
        mat_fo.append(fun_obj(i))
    return mat_fo


#CALCULA O VETOR/MATRIZ FITNESS DO CONJUNTO DE SOLUÇÕES
#Variáveis: X (matriz de soluções)
def matriz_Fitness(matriz_fo):
    Fitness = []                         #Vetor que receberá o valor de fitness de cada solução
    for fo in matriz_fo:
        if fo >= 0:                      #Condição para escolha de equação para calcular o fitness
            Fitness.append(1 / (1 + fo))
        else:
            Fitness.append(1 + abs(fo))
    return Fitness

#FUNÇÃO PARA GERAR SOLUÇÃO VIZINHA
def solucao_vizinha(xij, xkj, limite_inf, limite_sup):          #Recebe dois parâmetros onde: j e k são aleatórios, k é diferente de i
    vij = xij + random.uniform(-1, 1) * (xij - xkj)                       #Equação que calcula vij, este valor será substituido em X[i] para gera a solução vizinha
    if vij > limite_sup:                                             #Condição para que as variáveis estejam sempre dentro do limite estabelecido
        vij = limite_sup                                             #variável recebe limite superior se valor da equação for maior
    elif vij < limite_inf:
        vij = limite_inf
    return vij

# FUNÇÃO ATUALIZAR SOLUÇÃO:
# PROCESSO EM QUE TANTO AS ABELHAS EMPREGADAS, QUANTO AS ASSISTENTES TENTAM MELHORAR O CONJUNTO DE SOLUÇÕES
def atualizarSolucao(X, matriz_fo, Limite, D, indice):
    #Aplicar Estrutura De Vizinhanca para escolha dos parâmetros para a função solucao_vizinha
    xi = copy.copy(X[indice])                 #Variável que recebe a solução a ser melhorada
    j = random.choice(range(D))                        #indice que representa a coluna (é escolhida aleatórimente)
    xij = xi[j]                               #Definição de xij, um dos parâmetros da função solucao_vizinha
    k = random.choice(range(SN))                   #Indice que representa a linha (ou solução) vizinha a ser trabalhada
    while k == indice:                                 #Loop para assegurar que k seja diferente se i
        k = random.choice(range(SN))               #Enquanto k é igual a i gera-se novas soluções
    xkj = X[k][j]                                      #Definição do segundo parâmetro (xkj) da função solucao_vizinha
    vij = solucao_vizinha(xij, xkj, b_low, b_upper)    #Variável recebe o valor da função solucao_vizinha
    xi[j] = vij                               #Na solução a ser melhorada, adiciona-se o valor de vij, e so então é que se tem a solução vizinha

    ## Avaliar fitness da nova solução
    if fun_obj(xi) < matriz_fo[indice]:                  #Condição para troca da solução antiga pela solução vizinha
        matriz_fo[indice] = fun_obj(xi)                  #Se a condição for verdade, o item da matriz Fitness que corresponde ao valor indice, recebe o novoFitness
        X[indice] = xi                       #Se verdade, a solução antiga é substituida pela novaSolução
        Limite[indice] = 0                             #Se verdade, a solução foi melhorada e o contador de limite recebe 0(zero)
    else:
        Limite[indice] += 1                            #Se for falso nada acontece e o contador recebe um incremento de 1(um)
    return X, matriz_fo, Limite                          #Retorna os valores de X, Fitness e Limite, todos atualizados na posição do índice analisado

# ROLETA PROBABILISTICA USADA PELA ABELHA ASSISTENTE PARA ESCOLHER QUAL SOLUÇÃO IRÁ TRABALHAR
def aplicarRoletaProbabilistica(Fitness):
    #Calcular matriz de probabilidade de cada solução e normaliza-la
    valorTotalFitness = sum(Fitness)
    probabilidadePi = []                                                 # Variável que receberá as probabilidades de cada solução da matriz X
    [probabilidadePi.append(i/valorTotalFitness) for i in Fitness]       #A probabilidade é adicionada a matriz probabilidadePi

    probabilidadeNormalizada = []                                        #Variável que receberá as probabilidades normalizadas
    aux2 = 0                                                             #Variável que auxiliará na soma acumulativa das probabilidades
    for i in probabilidadePi:
        aux2 += i
        probabilidadeNormalizada.append(aux2)                        #Normalização

    roleta = random.random()                        #Gera-se um valor aleatório entre 0 e 1 para escolha da solução a ser melhorada pela onlooker bee
    posicao = 0                                     #Variável que receberá de aux3 a posição da solução escolhida
    for i in range(SN):                             #Loop para acessar os valores da matriz probabilidadeNormalizada
        if roleta >= probabilidadeNormalizada[i]:                             #Condição para encontrar o maior valor de i que satisfaça: roleta <= i
            posicao = i                          #Se verdade posição recebe aux3 (indice da matriz)
        else:
            posicao = i
            break                               #Se falso aux3 recebe incremento e retorna o Loop
    return posicao                                  #Retorno da função

#FUNÇÃO PARA GERAR SOLUÇÕES ALEATÓRIAS: PROCESSO DA ABELHA ESCOTEIRA
def gerarNovaSolucao(D, b_low, b_upper):                                                #Recebe o número de dimensões e os limites inferiores e superiores das variáveis
    novaSolucao = []                                                                    #Matriz com a nova solução Gerada pela abelha escoteira
    [novaSolucao.append(b_low + random.random()*(b_upper - b_low)) for i in range(D)]   #A cada iteração a matriz recebe o valor aleatório gerado                                                  #Loop para gerar um valor aleatório para cada variável
    return novaSolucao                                                                  #Retorna a nova solução

# CONFIGURAÇÃO DOS PARÂMETROS DO ALGORITMO ABC (KARABOGA, 2005)
SN = 10
CS = SN*2
limite = SN*D
MCN = 2000
NT = 30
arquivo_teste = open('arquivo.txt', 'w')  #abre arquivo de texto para salvar as melhores soluções de cada rodada

for i in range(NT):
    # GERAR SOLUÇÕES ALEATÓRIAS A AVALIA-LAS (CALCULAR FITNESS)
    X = inicializarPopulacao(SN, D, b_low, b_upper)    #Variável que recebe a matriz de soluções iniciais
    matriz_fo = aval_sol(X)

    Limite = []
    [Limite.append(0) for i in range(SN)]               #Variável que recebe a matriz inicial dos limites

    MelhorSolucao = X[matriz_fo.index(min(matriz_fo))]                                  #Variável que receberá melhor solução. Usada para auxiliar o processo de memorizar a melhor solução dentro dos ciclos de forrageamento
    Melhor_fo = min(matriz_fo)                                  #Idem.

    x = []                                             #Eixo x do gráfico de convergência
    y = []                                             #Eixo y do gráfico de convergência

    tempo = time.time()                                 #Tempo inicial para calcular a execução do algoritmo
    #INÍCIO DAS ITERAÇÕES DE CADA SIMULÇÃO (NT)
    for cont1 in range(MCN):
        x.append(cont1 + 1)                             #Adiciona valores a lista x para construir gráfico de convergência

        #INÍCIO DO PROCESSO DAS ABELHAS EMPREGADAS:
        [atualizarSolucao(X, matriz_fo, Limite, D, cont2) for cont2 in range(SN)]   #Recebe o conjunto de soluções X e tenta melhora-las por greedy selection

        Fitness = matriz_Fitness(matriz_fo)
        #INÍCIO DO PROCESSO DAS ABELHAS ASSISTENTES:
        for cont3 in range(SN):                                                      #Loop para acionar cada abelha assistente e enviá-las pra melhorar as soluções escolhidas
            posicaoEscolhida = aplicarRoletaProbabilistica(Fitness)              #Variável recebe a posição escolhida
            atualizarSolucao(X, matriz_fo, Limite, D, posicaoEscolhida)               #Função que atualiza as solução da posição escolhida

        #INÍCIO DO PROCESSO DA ABELHA ESCOTEIRA
        posicaoPiorLimite = Limite.index(max(Limite))                                #Define-se qual é a pior solução, ou seja, qual é a maior
        if Limite[posicaoPiorLimite] >= limite:                                      #Se a condição for verdade:
            nova_solucao = gerarNovaSolucao(D, b_low, b_upper)
            X[posicaoPiorLimite] = nova_solucao                                      #A abelha exploradora gera uma nova solução aleatória
            Limite[posicaoPiorLimite] = 0                                            #O contador de limite recebe 0 (zero)
            matriz_fo[posicaoPiorLimite] = fun_obj(nova_solucao)

        #DEFINIR MELHOR SOLUÇÃO DE CADA ITERAÇÃO MCN:
        matriz_fo = aval_sol(X)
        best_fo_cycle = min(matriz_fo)
        best_sol_cycle = X[matriz_fo.index(min(matriz_fo))]

        #MEMORIZAR MELHOR SOLUÇÃO
        if best_fo_cycle < Melhor_fo:
            Melhor_fo = best_fo_cycle
            MelhorSolucao = best_sol_cycle
        y.append(Melhor_fo)                                           #Adiciona um valor a lista y para construir gráfico

    arquivo_teste.write(str(Melhor_fo) + "\n")            #Entro com as variáveis da melhor solução para calcular a função objetivo
    print('f(xi) = ', MelhorSolucao)
    print('f(x*) = ', Melhor_fo)
    print("Tempo",time.time()-tempo)                                   #calcula o tempo total de execução do algoritmo


#Plotagem do gráfico
plt.xlabel('iterações')
plt.ylabel('função objetivo')
plt.title(nomeFuncao)
plt.plot(x, y)
plt.show()

