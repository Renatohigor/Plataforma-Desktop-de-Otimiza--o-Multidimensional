from Model.Tools import*
from random import random


class Particle:
    # x:      posição da partícula
    # v:      velocidade da particula
    # pBest:  melhor posição encontrada da particula


    x=Ponto()
    pBest=Ponto()
    v=Ponto()
    def __init__(self,x,v,id):

        self.idt=id
        self.x=x
        self.pBest= x
        self.v= v
        self.of = None
        self.fit = None
        self.it_pb = 1
    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\n'.format(str(self.idt), str(self.x), str(self.pBest), str(self.of), str(self.fit), str(self.v))
    def __copy__(self):
        aux = Particle(self.x, self.v, self.idt)
        aux.pBest = self.pBest
        aux.of = self.of
        aux.fit = self.fit
        aux.it_pb = self.it_pb
        return aux


    def update_pBest(self,f,itr):
        if f<<self.x < f<<self.pBest :
            self.pBest=self.x
            self.it_pb = itr

    def update_speed_and_position(self,w,gBest,c1,c2,d):
        aux_x, aux_v = self.x, self.v
        pbest_xi = self.pBest - self.x
        gbest_xi = gBest - self.x
        rand1 = Ponto.Randon(N=len(self.x.v))
        rand2 = Ponto.Randon(N=len(self.x.v))
        tc = pbest_xi * c1 * rand1
        ts = gbest_xi * c2 * rand2
        vw = w * self.v
        self.v = vw + tc + ts
        self.x = self.x + self.v
        self.x = Ponto.validar_x(self.x, d)
        return self.idt, vw, pbest_xi, rand1, tc, gbest_xi, rand2, ts, aux_v, self.v, aux_x, self.x

class Swarm_2:

    # n:          Tamanho da população
    # gBest:      melhor posição encontrada da população
    # population: população de particulas
    # f:          fumção
    def __init__(self,n):
        self.n = n
        self.gBest = Ponto()
        self.population = []
        self.domain = None
        nomeAlgo = 'PSO-W  08/08/2019'
        artigoBase = 'J. Kennedy and R. Eberhart, "Particle swarm optimization," Proceedings of ICNN\'95-\n' \
                     'International Conference on Neural Networks, Perth, WA, Australia, 1995, pp. 1942-1948 \n' \
                     'vol.4.doi: 10.1109/ICNN.1995.488968 '
        versao = '0.1'


    #Inicialize a população inicial
    def boot_the_population(self, domain, initial_velocity):
        self.population.clear()
        for i in range(0, self.n):
            self.population.append(Particle(x=Ponto.Randon(domain), v=initial_velocity, id=i))

    def minimum(self, f):
        media = 0

        lower_position = self.population[0].x
        maximo = self.population[0].of = lower_value = f << lower_position
        iaux = self.population[0].idt
        for i in range(0, self.n):
            self.population[i].of = value = f << self.population[i].x
            self.population[i].fit = 1 + abs(self.population[i].of) if self.population[i].of <= 0 else 1 / (
                        1 + self.population[i].of)
            media += self.population[i].of
            if lower_value > value:
                lower_value = value
                lower_position = self.population[i].pBest
                iaux = self.population[i].idt
            elif maximo < value:
                maximo = value
        return iaux, lower_position, maximo, media / len(self.population), self.population[iaux].__copy__()

        # Atualiza as  velocidades é posições

    def update_population_position_velocity(self,iter):
        for i in range(0, len(self.population)):
           self.population[ i].update_speed_and_position(self.w,self.gBest,self.c1,self.c2 ,self.domain)
           self.population[i].update_pBest(self.f,iter)


    def PSO(self, f, w,c1,c2,domain, itr,initial_velocity):
        self.f=f
        self.w=w
        self.c1=c1
        self.c2=c2
        self.domain = [domain[0].v, domain[-1].v]
        self.itr=itr
        self.itr = itr
        self.boot_the_population(domain=self.domain, initial_velocity=initial_velocity)
        self.gBest_iter, self.gBest, maximo, media, gbest_idv = self.minimum(self.f)
        aux = self.f << self.gBest
        list_conver = []
        list_conver.append((self.gBest.v, aux))

        i = 1
        while i <=itr:
            self.update_population_position_velocity(i)
            aux_gBest_iter, aux_gBest, aux_maximo, aux_media, _aux_gbest_idv = self.minimum(self.f)
            if (f << aux_gBest) < (f << self.gBest):
                self.gBest_iter = aux_gBest_iter
                self.gBest = aux_gBest
            aux = self.f << self.gBest
            list_conver.append((self.gBest.v, aux))

            i += 1
        print('list_conver',list_conver)
        return list_conver
