from Model.M_deter.M_Deter_model import *

def metodoOrdemUM01(ID, parametro):


    if ID == 0: return MOU.otmizar(f=parametro[0], ponto_inicial=parametro[1], pre=parametro[2],
                                   metodoOZ=parametro[3], ni=parametro[4], dim=parametro[5])
    if ID == 1: return MOU.FletcherReeves(f=parametro[0], ponto_inicial=parametro[1], pre=parametro[2],
                                          metodoOZ=parametro[3], ni=parametro[4], dim=parametro[5])