from sympy.plotting import plot3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, exp, sqrt
from sympy import simplify,symbols

def plot3d_functio(f,d):
    v = f.vars
    xi1, xi2= d[0].v
    xf1, xf2= d[-1].v
    eq =simplify(f.f_str)
    plot3d(eq, (symbols(str(v[0])), xi1, xf1), (symbols(str(v[1])), xi2, xf2), color='r', xlabel='x', ylabel='y')

def error(r,name_arq=None):
    maior = r[0]
    i = 1
    plt.title('Grafico Erro')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.plot(r, linestyle='-', marker='o', linewidth=2.0)

    for i in range(len(r)-1):
        if r[i] < maior:
            maior = r[i]

    ux = len(r) - 1
    aux = plt.annotate(maior, xy=(ux, maior), xytext=(ux, r[0]))
    plt.show()


def level2d(f, d, p, r):
    v = f.vars
    xi1, xi2 = d[0].v
    xf1, xf2 = d[-1].v
    xi = np.linspace(xi1,xf1, xf1-xi1/100)
    yi = np.linspace(xi2, xf2,  xf2-xi2/100)
    x1, x2 = np.meshgrid(xi, yi)

    z = eval(f.f_str)
    fig, ax = plt.subplots()
    plt.title("Curva de nivel")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")

    ax.contour(x1, x2, z, linewidths=0.5, colors='k')
    cs = ax.contourf(x1, x2, z, cmap="RdBu_r")

    maior=0
    for i in range(len(r)-1):
        if r[i] < maior:
            maior = r[i]

    #caminho
    (xponto, yponto) = zip(*p)
    ax.plot(xponto, yponto, color='black', linewidth=0.3)

    #Pontos
    for i in range(len(r)):
        plt.scatter(p[i][0], p[i][1], alpha=1, s=10, facecolor='black')
        y = p[i][1]
        x = p[i][0]

    #Anotação
    plt.annotate(maior, xy=(x, y), xytext=(x, 5), arrowprops=dict(facecolor='yellow', shrink=0.0002),)
    plt.colorbar(cs)

    plt.show()


