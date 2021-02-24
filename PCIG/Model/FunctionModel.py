from Model.Tools import *

class Function:

    def __init__(self,iter_dimenssao,dominio,dirscricao,funcao,nome):
        self.iter_dimenssao =iter_dimenssao
        self.dominio=dominio
        self.nome=nome
        self.dirscricao=dirscricao
        self.funcao=funcao

    def get_funcao(self,dimecao):
        d= [Ponto(), Ponto()]
        d[0].set(dimecao, float(self.dominio[0]))
        d[-1].set(dimecao, float(self.dominio[-1]))
        return Funcao.montaF(Dimessao=dimecao,fun=self.funcao),d




def list_new_function(list_text):
    list_Function=[]
    for text in list_text:
        try:

            iter_dimenssao,dominio,nome, dirscricao, funcao=  text.split('|')
            iter_dimenssao = iter_dimenssao.split(',')
            iter_dimenssao =[float(iter_dimenssao[0]),float(iter_dimenssao[-1])]
            dominio = dominio.split(',')
            dominio = [float(dominio[0]), float(dominio[-1])]
            list_Function.append(Function(iter_dimenssao=iter_dimenssao,dominio=dominio,dirscricao=dirscricao,funcao=funcao,nome=nome))

        except:
            pass
    return list_Function