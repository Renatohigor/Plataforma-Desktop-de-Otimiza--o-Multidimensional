
from Model.Tools import *

class MOZ:

    @staticmethod
    def metodoOrdemZero(nome,f,ponto1,ponto2,pre,i=10):

        if nome == "bissecao"       :return  MOZ.bissecao(f,ponto1,ponto2,pre)
        if nome == "aure"           : return MOZ.aure(f, ponto1, ponto2, pre)
        if nome == "fibonacci"      :return  MOZ.fibonacci(f, ponto1, ponto2,pre,i)
    @staticmethod
    def bissecao(f, pi, pf, pre):
        fu = f
        pm = (pi+pf)/2.0

        while (abs((f<<pf) - (f<<pi) )> pre and (f<<pm) != 0.0):

            if f<<pi > f<<pm:
                pf = pm
            elif f<<pi > f<<pf:
                pi = pm
            else:
                pi =(pi+pm)/2.0
                pf = (pm+pf)/2.0
            pm = (pi+pf)/2.0

        return pm

    @staticmethod
    def aure(f, pi, pf, pre):

        p_aux =pf- pi
        num_aure = (1+ sqrt(5)) / 2.0
        pa = pi+(p_aux*num_aure)
        pb = pi+(p_aux*(1 - num_aure))
        while abs((f<<pa) - (f<<pb)) > pre:
            if f<<pa >= f<<pb:
                pi = pa
            else:
                pf = pb
            p_aux = pf- pi
            pa = pi+(p_aux*num_aure)
            pb =  pi+(p_aux*(1 - num_aure))
        return (pi+pf)/2

    @staticmethod
    def fibonacci(f, pi, pf, pre, i):
        fu = f
        F = {}
        F[1] = 1
        F[2] = 2
        for j in range(3, i + 3): F[j] = F[j - 1] + F[j - 2]
        k = 1
        Lambda = 1 - (F[i - k + 1] / F[i - k + 2])
        x1 = pi + ((pf- pi)*Lambda)
        x2 = pf+((pf- pi)*(-Lambda))
        while (k <= i and not MOZ.orin(x2-x1)):

            if fu.subs(x1) < fu.subs(x2):
                pf = x2
                x2 = x1
                x1 =pi + ((pf- pi)*Lambda)
            else:
                pi = x1
                x1 = x2
                x2 =pf+((pf- pi)*(-Lambda))

            k += 1
        if k == i:
            x1 = pi + ((pf- pi)*Lambda)
            x2 = x1+(x1+pre)
            if fu<<x1 > fu<<x2:
                pi = x1
            elif fu<<x1 < fu<<x2:
                pf = x2
        else:
            pi = x1
            pf = x2
        pm =((pf+pi)/ 2.0)
        return pm

    @staticmethod
    def orin(ponto):
        for i in ponto.v:
            if i==0: return False
        return True

class MOU:

    @staticmethod
    def otmizar(f,ponto_inicial,pre,metodoOZ,ni,dim):
        p = ponto_inicial
        caminho = []
        aux = []
        caminho.append((p.v,f<<p))

        aux.clear()
        i = 0
        while i < ni:
            p1 = Funcao.Gradient_no_ponto(f,p)
            p1=p1*(-1)
            p_aux=p+p1
            p1 = MOZ.metodoOrdemZero(metodoOZ,f, p,p_aux,pre)

            p1=Ponto.validar_x(p1,dim)
            caminho.append((p1.v, f << p1))


            if (f<<p) <= (f<<p1): break
            p = p1
            i = i + 1
        return caminho

    @staticmethod
    def FletcherReeves(f,ponto_inicial,pre,metodoOZ,ni,dim):
        fun =f
        p = ponto_inicial
        caminho = []
        caminho.append((p.__copy__(), f << p))
        g = Funcao.Gradient_no_ponto(f=f,p=p)
        num = 0
        S = g*-1

        while ~MOZ.orin(S) and num < ni:

            p1 = MOZ.metodoOrdemZero(nome=metodoOZ,f=f, ponto1=p,
                                     ponto2=(p+ S),pre=pre)

            g1 =Funcao.Gradient_no_ponto(f=f,p=p1)

            beta_dv = beta_ds = 0
            p_g = g**2
            p_g1 = g1**2

            beta_dv = beta_dv + p_g1
            beta_ds = beta_ds + p_g
            S = (g1 *-1)+S*(beta_dv / beta_ds)
            p1 = Ponto.validar_x(p1, dim)
            caminho.append((p1.__copy__(), f << p1))
            if (f << p) <= (f << p1): break
            p = p1
            num = num + 1

        print(caminho[len(caminho) - 1])
        return caminho


