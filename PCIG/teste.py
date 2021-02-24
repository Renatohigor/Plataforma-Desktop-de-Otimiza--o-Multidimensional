# from Model.FunctionModel import *
# from Model.GraficFunctionModel import *
from Controller.Otmiz import *
from Model.M_prob.ABC_01 import *
# from Model.M_deter import metodoOrdemUM01
# from time import sleep


# arq = open("Data\list_function.fb",'r')
# list_F=[list_new_function(arq.readlines())]
list_F=list_new_function(['2,inf|-600,600|Esfera|Função|x;suma{x**2,x,2} '])
for i in list_F[:1]:
    print(i.iter_dimenssao)
    print(i.dominio)
    print(i.dirscricao)
    print(i.nome)
    n_dim=2
    f,d=i.get_funcao(2)
    ponto_inicial=Ponto()
    ponto_inicial.set(2,0)
    #plot3d_functio(f,d).save("DATA\\functo_img\{}_{}
    functiom_descr=(i.iter_dimenssao,i.dominio,i.dirscricao,i.nome,n_dim)
    colony_ab=Colony("test")
    a=colony_ab.ABC(f=f,domain=d,SN=3,MCN=1,NT=1,D=2,limite=1,functiom_descr=functiom_descr)
    print(a)



