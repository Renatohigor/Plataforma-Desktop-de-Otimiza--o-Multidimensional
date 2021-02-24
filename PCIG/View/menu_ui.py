# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_iniciar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.Otmiz import *
from View.menu_f_ui import *
from View.paremetro_md_ui import *
from View.parametos_avcs_ui import *
from View.prmtr_psos_ui import *
from Model.GraficFunctionModel import *

class Ui_MainWindow(QtWidgets.QMainWindow,object):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.pametros_P=None
        self.n_problema =None
        self.f_l=None
        self.dim=None

        self.setupUi()
    def setupUi(self):
        self.list_functon=FunctiinControler()
        self.list_metodos=MetodoControler()
        self.setObjectName("MainWindow")
        self.resize(529, 434)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 491, 59))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 80, 101, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.ADD_ND_spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ADD_ND_spinBox.setFont(font)
        self.ADD_ND_spinBox.setObjectName("ADD_ND_spinBox")
        self.verticalLayout_3.addWidget(self.ADD_ND_spinBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 381, 81))
        self.ADD_ND_spinBox.setMinimum(2)
        self.ADD_ND_spinBox.setValue(2)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.List_FUN_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.List_FUN_comboBox.setFont(font)
        self.List_FUN_comboBox.setObjectName("List_FUN_comboBox")
        self.verticalLayout_2.addWidget(self.List_FUN_comboBox)
        self.ADD_FU_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ADD_FU_pushButton.setObjectName("ADD_FU_pushButton")
        self.verticalLayout_2.addWidget(self.ADD_FU_pushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 180, 481, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.list_Algo_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.list_Algo_comboBox.setObjectName("list_Algo_comboBox")
        self.gridLayout.addWidget(self.list_Algo_comboBox, 1, 0, 1, 2)
        self.parametros_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.parametros_pushButton.setObjectName("parametros_pushButton")
        self.gridLayout.addWidget(self.parametros_pushButton, 2, 0, 1, 2)
        self.Rodar_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Rodar_pushButton.setFont(font)
        self.Rodar_pushButton.setObjectName("Rodar_pushButton")
        self.gridLayout.addWidget(self.Rodar_pushButton, 3, 1, 1, 1)
        # self.limpar_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(75)
        # self.limpar_pushButton.setFont(font)
        # self.limpar_pushButton.setObjectName("limpar_pushButton")
        # self.gridLayout.addWidget(self.limpar_pushButton, 3, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "lista de funções de benchmarking"))
        self.label.setText(_translate("MainWindow", "Dimensão"))
        self.ADD_FU_pushButton.setText(_translate("MainWindow", "+"))
        self.label_3.setText(_translate("MainWindow", "Lista de Algoritmo"))
        self.parametros_pushButton.setText(_translate("MainWindow", "Parâmetro"))
        self.Rodar_pushButton.setText(_translate("MainWindow", "Executar"))
        # self.limpar_pushButton.setText(_translate("MainWindow", "Limpar "))


        self.print_list_box_funcao()
        self.print_list_box_metodo()

        self.ADD_FU_pushButton.clicked.connect(self.cliker_add)
        self.parametros_pushButton.clicked.connect(self.setparemetro)
        self.Rodar_pushButton.clicked.connect(self.rodar)
    def print_list_box_funcao(self):
        _translate = QtCore.QCoreApplication.translate
        j = 0
        self.List_FUN_comboBox.clear()
        for i in self.list_functon.listar_fu():
            self.List_FUN_comboBox.addItem('')
            self.List_FUN_comboBox.setItemText(j, _translate("MainWindow", str(i)))
            j += 1
    def print_list_box_metodo(self):
        _translate = QtCore.QCoreApplication.translate
        j = 0
        self.list_Algo_comboBox.clear()
        for i in self.list_metodos.list_metodo:
            self.list_Algo_comboBox.addItem('')
            self.list_Algo_comboBox.setItemText(j, _translate("MainWindow", str(i)))
            j += 1
    def cliker_add(self):
        self.window = Ui_Menu_2()
        self.hide()
        try:
            self.window.exec_()
        except:
            pass
        self.show()
        if self.window.obj is not None:
            self.list_functon.list_functon.append(self.window.obj)
            self.print_list_box_funcao()
    def setparemetro(self):
        funcao_id=self.List_FUN_comboBox.currentIndex()
        dim= int(self.ADD_ND_spinBox.text())
        f, d = self.list_functon.list_functon[funcao_id].get_funcao(dim)
        problema_n=self.list_Algo_comboBox.currentIndex()
        self.f_l=f
        self.n_problema=problema_n
        self.dim=d
        if problema_n < 4:

            self.window = prametro_acvs()
            if problema_n <2 :
                self.window.lineEdit_beta_min.setVisible(False)
                self.window.label_8.setVisible(False)
            self.hide()
            try:
                self.window.exec_()
            except:
                pass
            if self.window.parametro is not None:
                npop, nger, alfa, beta, beta_min, gama, tetha = self.window.parametro
                if problema_n==0 or problema_n==1:
                   self.pametros_P=[f,d,npop,beta,alfa,nger,gama,tetha]
                else:
                    self.pametros_P = [f, d, npop, beta,beta_min, alfa, nger, gama, tetha]
            self.show()

        elif problema_n ==4:

            self.window = prmtr_pso()
            self.window.label_3.setVisible(False)
            self.window.label_4.setVisible(False)
            self.window.label_5.setVisible(False)
            self.window.label_6.setVisible(False)
            self.window.label_7.setVisible(False)
            self.window.label_8.setVisible(False)

            self.window.lineEdit_c1_fi.setVisible(False)
            self.window.lineEdit_c1_in.setVisible(False)
            self.window.lineEdit_c2_in.setVisible(False)
            self.window.lineEdit_c2_fi.setVisible(False)
            self.window.lineEdit_w_in.setVisible(False)
            self.window.lineEdit_w_fin.setVisible(False)
            self.hide()
            try:
                self.window.exec_()
            except:
                pass

            if self.window.parametro is not None:
                npop, nger, c1_in, c1_fi, c2_in, c2_fi, w_in, w_fi = self.window.parametro
                v=Ponto()
                v.set(dim,0)
                self.pametros_P = [npop,f,d,nger,v]
                self.show()

        elif problema_n ==5:
            self.window = prmtr_pso()
            # self.window.label_3.setVisible(False)
            # self.window.label_4.setVisible(False)
            self.window.label_5.setVisible(False)
            self.window.label_6.setVisible(False)
            self.window.label_7.setVisible(False)
            # self.window.label_8.setVisible(False)


            self.window.lineEdit_c1_fi.setVisible(False)
            # self.window.lineEdit_c1_in.setVisible(False)
            # self.window.lineEdit_c2_in.setVisible(False)
            self.window.lineEdit_c2_fi.setVisible(False)
            # self.window.lineEdit_w_in.setVisible(False)
            self.window.lineEdit_w_fin.setVisible(False)


            self.hide()
            try:
                self.window.exec_()
            except:
                pass
            if self.window.parametro is not None:
                npop, nger, c1_in, c1_fi, c2_in, c2_fi, w_in, w_fi= self.window.parametro
                v = Ponto()
                v.set(dim, 0)
                self.pametros_P = [npop, f, d, nger, v,w_in,c1_in,c2_in]
            self.show()

        elif problema_n ==6:
            #[npop, nger, c1_in, c1_fi, c2_in, c2_fi, w_in, w_fi]
            self.window = prmtr_pso()
            self.hide()
            try:
                self.window.exec_()
            except:
                pass
            if self.window.parametro is not None:
                npop, nger, c1_in, c1_fi, c2_in, c2_fi, w_in, w_fi = self.window.parametro
                v = Ponto()
                v.set(dim, 0)
                self.pametros_P = [npop, f, d, nger, v, w_in,w_fi, c1_in,c1_fi ,c2_in,c2_fi]

            self.show()

        elif problema_n > 6:

            self.window = parametros_determini_Dialog(self.list_metodos.list_moz)
            self.hide()
            try:
                self.window.exec_()
            except:
                pass

            if self.window.parametro is not None:
                ponto_inicial, nger, pre, mdoz = self.window.parametro
                p_in = Ponto()
                p_in.set(dim, ponto_inicial)
                self.pametros_P = [f,p_in,pre, mdoz, nger,[d[0].v,d[-1].v]]
            self.show()
    def rodar(self):
        if self.pametros_P is not None:
            print(self.pametros_P)
            a=self.list_metodos.exec(self.n_problema,self.pametros_P)
            p = [i[0] for i in a]
            r=[i[-1] for i in a]
            error(r,"..\Final{}_{}".format('Erro',hex(id(self))))
            if len(p[0])==2:
                plot3d_functio(self.f_l,self.dim)
                level2d(self.f_l, self.dim, p, r)




