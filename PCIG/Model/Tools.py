from sympy import *
from math import *
import os, shutil
from Model.pointClass import *
from datetime import datetime
import logging ,abc
from unicodedata import normalize


class Tools(metaclass=abc.ABCMeta):
    # CRIA UM DIRETÓRIO
    @staticmethod
    def new_path(folder_nome):
        try:
            os.makedirs(folder_nome, 0o777, False)
            return True
        except Exception:
            return False

    # DELETA UM DIRETÓRIO
    @staticmethod
    def delete_path(folder_nome):
        try:
            shutil.rmtree(folder_nome, ignore_errors=True)
            return True
        except Exception:
            return False
        # DELETA UM DIRETÓRIO

    # RENOMEIA UM ARQUIVO 'nome_atual' PARA 'nome_novo'
    # RECORTA OS ARQUIVOS CONTIDOS EM UM DIRETÓRIO 'de' E COLA EM 'para'
    @staticmethod
    def transfer_and_rename_files(antigo_nome, nome_novo, de, para, log):
        ext = str(antigo_nome).split('.')[-1]
        try:
            nome_novo += "." + ext
            shutil.move(str(de) + "/" + str(antigo_nome), str(para) + "/" + nome_novo)
        except OSError as err:

            log.insert_log(str(err))
            # sleep(60*60)

        # RETIRAR QUALQUER FORMA DE ACENTUAÇÃO

    @staticmethod
    def setStrVetor(txt,dim):
        aux=''
        for i in range(dim):
            aux += txt + str(i + 1)
            if i< dim -1:
                aux+=';'
        return aux

class Funcao:
    vars = {}
    diffs = {}

    def __init__(self, variaveis_sinbolicas, funcao):
        self.vars = variaveis_sinbolicas
        self.f_str = funcao
        self.n = len(variaveis_sinbolicas)
        self.f_lambda = self._set_lambda()

    def _set_lambda(self,test=None):
        aux_f_str=self.f_str if test is None else test
        for i in range(self.n):
            aux_f_str= aux_f_str.replace(str(self.vars[i]),'f[{}]'.format(i))
        return eval("lambda f: {}".format(aux_f_str))
    @staticmethod
    def _set_diffis_lambda(f):
        for i in range(f.n):
            f.diffs[i]=f._set_lambda(str( diff(f.f_str, f.vars[i], 1)))



    def set_variaveis(self, variaveis_sibolicas):
        self.vars = variaveis_sibolicas

    def set_funcao(self, funcao):
        self.f_str = funcao

    '''
    str(pickle.dumps(dict_aux))
     pickle.loads(eval(row_database))
     mult = eval("lambda x,y: y*x")
     >>> exec("lambda x,y : (x*y)")
     map(multiply2, [1, 2, 3, 4])

    '''

    @staticmethod
    def Gradient_no_ponto(f, p):
        vetor = Ponto()
        if len(f.diffs.keys()) == 0:
            Funcao._set_diffis_lambda(f)

        for i in range(f.n):
            vetor.v.append(f.diffs[i](p.v))


        return vetor

    def __lshift__(self, ponto):
        v=ponto.v
        return float(self.f_lambda(v))

    @staticmethod
    def montaF(fun,Dimessao):

        Dimessao=str(int(Dimessao))
        fun = fun[0:-1]
        tex = str(fun)
        Variavel, exprecao = tex.split(";")
        Variaveis = {}
        flag = exprecao.find('suma', 0)
        exprecao = exprecao.replace('N', Dimessao)
        while flag != -1:
            pi = flag
            pf = exprecao.find('}', pi)
            somatorio = exprecao[pi:pf + 1]
            aux = exprecao[pi + 5:pf]
            a, b, c = aux.split(",")
            n = int(sympify(c))
            aux = "("
            for i in range(1, n + 1):
                if i > 1: aux = aux + " + "
                flag2 = a.find('x1', 0)
                if flag2 == -1:
                    aux = aux + a.replace(b, b + str(i))
                else:
                    aux = aux + (a.replace(b, b + str(i))).replace('x' + str(i) + '1', b + str(i + 1))
                    if i <= n: Variaveis[i] = symbols(b + str(i + 1))

                Variaveis[i - 1] = symbols(b + str(i+1))
            aux = aux + ")"
            exprecao = exprecao.replace(str(somatorio), str(aux))
            flag = exprecao.find('suma', 0)
        for i in range(0, int(Dimessao)):
            Variaveis[i] = symbols((Variavel + str(i + 1)))

        f = Funcao(variaveis_sinbolicas=Variaveis,funcao=exprecao)
        return f


class BaseFunctions:

    @staticmethod
    def FunctionIni(point=Ponto):
        value = point.v
        x1 = value[0]
        x2 = value[-1]

        y=12 * x1 ** 2.0 + 4.0 * x2 ** 2.0 - 12.0 * x1 * x2 + 2.0 * x1

        return y

    @staticmethod
    def Rosenbrock(point=Ponto):
        value = point.v
        n = len(value)
        return sum([100 * (value[i + 1] - value[i] ** 2) ** 2 + (1 - value[i]) ** 2 for i in range(n - 1)])

    @staticmethod
    def Rastrigi(point=Ponto):
        value = point.v
        n = len(value)
        pi = 3.141592653589793
        return sum([-10 * cos(2 * pi * value[i]) + value[i] ** 2 for i in range(n)]) + 10 * n

    @staticmethod
    def Zakharov(point=Ponto):
        value = point.v
        n = len(value)
        sum2 = sum1 = 0
        for i in range(n):
            sum1 += value[i] ** 2
            sum2 += 0.5 * (i + 1) * value[i]

        return sum1 + sum2 ** 2 + sum2 ** 4

    @staticmethod
    def Ackley(point=Ponto):
        value = point.v
        a = 20.0
        b = 0.2
        c = 2 * 3.141592653589793
        n = len(value)
        sum2 = sum1 = 0
        for i in range(n):
            sum1 += value[i] ** 2
            sum2 += cos(c * value[i])

        term1 = -a * exp(-b * sqrt(sum1 / n))
        term2 = -exp(sum2 / n)

        return term1 + term2 + a + exp(1)

    @staticmethod
    def Sphere(point=Ponto):
        value = point.v
        n = len(value)
        return sum([value[i] ** 2 for i in range(n)])

class Function(BaseFunctions):
    def __init__(self, name=None):
        self.name = name

    def __lshift__(self, other=Ponto):

        if self.name == 'FunctionIni': return self.FunctionIni(other)
        if self.name == 'Rosenbrock': return self.Rosenbrock(other)
        if self.name == 'Rastrigi': return self.Rastrigi(other)
        if self.name == 'Zakharov': return self.Zakharov(other)
        if self.name == 'Ackley': return self.Ackley(other)
        if self.name == 'Sphere': return self.Sphere(other)


class LogErrorModel:
    def __init__(self, nomeAlgo, artigoBase, versao,namearq):

        self.nomeAlgo = nomeAlgo
        self.artigoBase = artigoBase
        self.versao = versao
        self.namearq=namearq
        self.dataExe = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                datetime.now().hour, datetime.now().minute, datetime.now().second)
        self.directory = os.path.abspath('../Logs')
        Tools.new_path(self.directory)
        self.filename = self.directory + '/' + '_{}_logging_exec.log'.format(namearq)
        self.logger = logging.getLogger(self.filename)
        logging.basicConfig(filename=self.filename, filemode='a+', format='%(message)s',
                            level=logging.INFO)
        self.txt=''
        self.cabIter=''




    def __del__(self):
        arq = open("../test/{}.csv".format(self.namearq), 'a')
        self.text=Tools.remove_accents(self.txt).replace('\t',';').replace('.',',')
        arq.write(self.text)
        arq.close()

        arq = open("../test/{}_iter.csv".format(self.namearq), 'a')
        self.cabIter = Tools.remove_accents( self.cabIter).replace('\t',';').replace('.',',')
        arq.write( self.cabIter)
        arq.close()


    def insertTitle(self):
        self.logger.info('{}\n{}'.format('%', '#' * 200).upper())
        cabecalho = '% PONTIFÍCIA UNIVERSIDADE CATÓLICA DE GOIÁS (PUC-GO)\n' \
                    '% DEPARTAMENTO DE MATEMÁTICA E FÍSICA\n' \
                    '% Nível: Graduação [x] / Pós-Graduação\n' \
                    '% Participantes: \n' \
                    '% Aurelio    ->  Discente [x] / Orientador [ ]\n' \
                    '% Renato    ->  Discente [x] / Orientador [ ] \n' \
                    '% Eng. Civil Wanderlei Malaquias Pereira Junior    ->  Discente [ ] / Orientador [x]\n' \
                    '% Maria José Pereira Dantas    ->  Discente [ ] / Orientador [x]\n' \
                    '% Edgar Ancioto    ->  Discente [ ] / Orientador  '
        self.logger.info('{}'.format(Tools.remove_accents(cabecalho).upper()))
        self.logger.info('{}\n{}'.format('%', '#' * 76).upper())

    def resultadoCompletoDoProcessoIterativo(self):
        self.logger.info('RESULTADO COMPLETO DO PROCESSO ITERATIVO\n '
                         'ALGORITMO ESCOLHIDO{}'.format('#' * 200).upper())

        self.logger.info(
            '{}'.format(str(self.nomeAlgo) + '\n' + str(self.artigoBase) + '\n' + str(self.versao) + '\n' + str(self.dataExe)).upper())
        self.logger.info('{}\n{}'.format('%', '#' * 200).upper())

    def dadosGerais(self, dados):

        self.logger.info('DADOS GERAIS{}'.format('#' * 200).upper())
        self.txt+='DADOS GERAIS\n'
        self.txt+=Tools.remove_accents(dados.upper())
        self.logger.info('{}'.format(dados).upper())
        self.logger.info('{}\n{}'.format('%', '#' * 200).upper())

    def populacaoInicial(self, popIni, cabecalho):

        self.logger.info('POPULACAO INICIAL{}'.format('#' * 200).upper())
        self.txt+='POPUPALACAO INICIAL\n'+Tools.remove_accents(cabecalho.upper())
        self.logger.info(cabecalho)

        aux = ''
        for i in popIni:
            aux += str(i)
            print(str(i))

        aux+='\n\n'
        self.txt+=Tools.remove_accents(aux.upper())
        self.logger.info('{}'.format(aux).upper())
        self.logger.info('{}\n{}'.format('%', '#' * 200).upper())

    def iniPorceIter(self):

        self.logger.info('MARCAÇÃO DO PROCESSO ITERATIVO{}\n'.format('#' * 200).upper())

    def iteracao(self, move_iter, iter, popOrd=None, cabecalhoPopOrd=None,tipo=False):

        self.logger.info('ITERAÇÃO {}\n'.format(str(iter)))
        self.txt+=Tools.remove_accents('ITERAÇÃO {}\n'.format(str(iter)))

        if popOrd is not None:
            self.logger.info(cabecalhoPopOrd)
            self.txt +=  Tools.remove_accents(cabecalhoPopOrd.upper())

            int=1
            aux=''
            for i in popOrd:
                if tipo:
                    aux += str(i)
                else:
                    aux +=str(int)+'\t'+ str(i)
                int+=1
            self.txt += Tools.remove_accents(aux.upper())
            self.logger.info('{}'.format(aux).upper())


        self.txt+=Tools.remove_accents(move_iter.upper())
        self.logger.info(move_iter)



        aux = "#### {}".format(self.nomeAlgo).upper()
        self.logger.info('FIM DA ITERAÇÃO {} \n\n'.format(str(iter)))
        self.txt+=Tools.remove_accents('FIM DA ITERAÇÃO {}\n\n'.format(str(iter)))

def trat_list(lista):
    return str(lista).replace("[",'').replace("]",'').replace(',',';')