from Model.FunctionModel import *
from Model.M_deter import *
from Model.M_prob import *
class FunctiinControler:
    def __init__(self,name_aqr='..\Data\list_function.fb'):
        self.name_arq=name_aqr
        arq = open(self.name_arq,'r')
        self.list_functon = list_new_function(arq.readlines())
        arq.close()

    def listar_fu(self):
        return [i.nome for i in self.list_functon]

    def set_functio(self,obf_f=Function()):
        try:
            iter_dimenssao="{},{}".format(obf_f.dirscricao[0],obf_f.dirscricao[-1])
            dominio="{},{}".format(obf_f.dominio[0],obf_f.dominio[-1])
            nome=obf_f.nome
            dirscricao=obf_f.dirscricao
            funcao=obf_f.função
            str_text='\n{}|{}|{}|{}|{} '.format(iter_dimenssao,dominio,nome, dirscricao, funcao)
            arq = open(self.name_arq,'a')
            arq.write(str_text)
            arq.close()
            self.list_functon.append(obf_f)
        except:
            pass

class MetodoControler:
    def __init__(self):
        self.list_metodo=[ "ACV_01",
                            "ACV_01_1",
                            "ACV_03",
                            "ACV_03_1",
                            "PSO_01",
                            "PSO_02",
                            "PS0_03",
                            "AG",
                            "Maxima Descida",
                            "Gradiente Conjudado ",
                        ]
        self.list_moz=['bissecao','aure','fibonacci']


    def exec(self, n,parametro):

        if n< 8:
            return metodoPROB(n,parametro)
        print(parametro)
        return metodoOrdemUM01(n-7,parametro)