from math import *
from random import *

class Ponto:

    def __init__(self):
        self.v = []

    def set(self, n, p):
        self.v = []

        for i in range(0, n): self.v.append(p)

    def __copy__(self):
        aux = Ponto()
        aux.v = [i for i in self.v]

    def __str__(self):
        aux =  str(self.v).replace(',',';').replace('[','').replace(']','').replace(' ','')
        return aux


    def __add__(self, other):

        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] + other.v[i])

        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] + other)
        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] + other)
        else:
            return self
        return aux

    def __radd__(self, other):

        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] + other.v[i])

        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] + other)
        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] + other)
        else:
            return self
        return aux

    def __sub__(self, other):
        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] - other.v[i])

        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] - other)

        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] - other)
        else:
            return self
        return aux

    def __mul__(self, other):

        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] * other.v[i])
        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] * other)
        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] * other)
        else:
            return self
        return aux

    def __truediv__(self, other):

        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] / other.v[i])

        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] / other)
        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] / other)
        else:
            return self
        return aux

    def __pow__(self, power, modulo=None):

        aux = Ponto()
        if type(power) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] ** power.v[i])

        elif type(power) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] ** power)
        elif type(power) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] ** power)
        else:
            return self
        return aux



    def __rsub__(self, other):
        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] - other.v[i])

        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] - other)

        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] - other)
        else:
            return self
        return aux

    def __rmul__(self, other):

        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] * other.v[i])
        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] * other)
        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(self.v[i] * other)
        else:
            return self
        return aux

    def __rtruediv__(self, other):

        aux = Ponto()
        if type(other) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(other.v[i] / self.v[i])

        elif type(other) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(other / self.v[i])
        elif type(other) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(other / self.v[i])
        else:
            return self
        return aux

    def __rpow__(self, power, modulo=None):

        aux = Ponto()
        if type(power) == type(self):
            for i in range(0, (len(self.v))):
                aux.v.append(power.v[i] ** self.v[i])

        elif type(power) == type(1):
            for i in range(0, (len(self.v))):
                aux.v.append(power ** self.v[i])
        elif type(power) == type(0.1):
            for i in range(0, (len(self.v))):
                aux.v.append(power ** self.v[i])
        else:
            return self
        return aux

    def __abs__(self):

        aux = Ponto()
        for i in range(0, (len(self.v))): aux.v.append(abs(self.v[i]))
        return aux

    @staticmethod
    def Randon(Dominio=None, N=None):

        p_aux = Ponto()
        p_aux.v = []
        if Dominio is None:
            for i in range(0, N):
                p_aux.v.append(random())
        else:
            for i in range(0, len(Dominio[0])):
                p_aux.v.append(Dominio[0][i] + random() * (Dominio[1][i] - Dominio[0][i]))

        return p_aux

    @staticmethod
    def dist_euclidiana(v1, v2):
        soma = 0
        vetaux = []
        for i in range(0, len(v1)):
            joao = (v1[i] - v2[i]) ** 2
            soma += joao
            vetaux.append(joao)

        ponto = Ponto
        ponto.v = vetaux[:]
        return sqrt(soma)

    @staticmethod
    def validar_x(x, d):
        aux=Ponto()
        aux.v = []
        for i in range(0, len(d[1])):

            if x.v[i] < d[0][i]:
                aux.v.append(d[0][i])
            elif x.v[i] > d[1][i]:
                aux.v.append(d[1][i])
            else:
                aux.v.append(x.v[i])

        return aux
