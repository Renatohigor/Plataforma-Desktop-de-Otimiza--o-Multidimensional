# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_f.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Model.FunctionModel import *


class Ui_Menu_2(QtWidgets.QDialog,object):
    nome=None
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi()
        self.obj = None
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(681, 298)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 70, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.doubleSpinBox_domi_if = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_domi_if.setFont(font)
        self.doubleSpinBox_domi_if.setObjectName("doubleSpinBox_domi_if")
        self.gridLayout.addWidget(self.doubleSpinBox_domi_if, 2, 0, 1, 1)
        self.doubleSpinBox_domi_if.setMinimum(-10000)
        self.doubleSpinBox_domi_if.setValue(-1.0)

        self.doubleSpinBox_domi_sup = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_domi_sup.setMinimum(-10000)
        self.doubleSpinBox_domi_sup.setValue(1.0)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_domi_sup.setFont(font)
        self.doubleSpinBox_domi_sup.setObjectName("doubleSpinBox_domi_sup")
        self.gridLayout.addWidget(self.doubleSpinBox_domi_sup, 2, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(460, 70, 211, 111))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_num_dime_if = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_num_dime_if.setFont(font)
        self.spinBox_num_dime_if.setObjectName("spinBox_num_dime_if")
        self.spinBox_num_dime_if.setMinimum(2)
        self.spinBox_num_dime_if.setValue(2)
        self.gridLayout_2.addWidget(self.spinBox_num_dime_if, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.spinBox_num_dime_sup = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_num_dime_sup.setFont(font)
        self.spinBox_num_dime_sup.setObjectName("spinBox_num_dime_sup")
        self.gridLayout_2.addWidget(self.spinBox_num_dime_sup, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.spinBox_num_dime_sup.setMinimum(2)
        self.spinBox_num_dime_sup.setValue(2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 201, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_vari = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_vari.setFont(font)
        self.lineEdit_vari.setObjectName("lineEdit_vari")
        self.horizontalLayout.addWidget(self.lineEdit_vari)
        self.pushButton_salvar = QtWidgets.QPushButton(self)
        self.pushButton_salvar.setGeometry(QtCore.QRect(460, 200, 211, 41))
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 120, 201, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_Nome = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_Nome.setFont(font)
        self.lineEdit_Nome.setObjectName("lineEdit_Nome")
        self.horizontalLayout_3.addWidget(self.lineEdit_Nome)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 190, 441, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.lineEdit_descrio = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_descrio.setFont(font)
        self.lineEdit_descrio.setObjectName("lineEdit_descrio")
        self.horizontalLayout_4.addWidget(self.lineEdit_descrio)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 651, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_expre = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_expre.setFont(font)
        self.lineEdit_expre.setObjectName("lineEdit_expre")
        self.horizontalLayout_2.addWidget(self.lineEdit_expre)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Dominio"))
        self.label_4.setText(_translate("Dialog", "Inferior"))
        self.label_5.setText(_translate("Dialog", "Superior"))
        self.label_7.setText(_translate("Dialog", "Mínimo"))
        self.label_8.setText(_translate("Dialog", "Máximo"))
        self.label_6.setText(_translate("Dialog", "Dimensões"))
        self.label.setText(_translate("Dialog", "Variável"))
        self.pushButton_salvar.setText(_translate("Dialog", "Salvar"))
        self.label_9.setText(_translate("Dialog", "Nome"))
        self.label_10.setText(_translate("Dialog", "Descrição"))
        self.label_2.setText(_translate("Dialog", "Formula "))
        self.pushButton_salvar.clicked.connect(self.clicle_save)

    def clicle_save(self):

        try:
            dominio = [float(str(self.doubleSpinBox_domi_if.text()).replace(',', '.')),
                       float((self.doubleSpinBox_domi_sup.text()).replace(',', '.'))]
            iter_dimenssao = [int(str(self.spinBox_num_dime_if.text())), int(str(self.spinBox_num_dime_sup.text()))]

            funcao = '{};{}'.format(str(self.lineEdit_vari.text()), str(self.lineEdit_expre.text()))
            dirscricao = str(self.lineEdit_descrio.text())
            nome = str(self.lineEdit_Nome.text())
            self.nome=nome
            self.obj = Function(iter_dimenssao=iter_dimenssao, dominio=dominio, dirscricao=dirscricao, funcao=funcao,
                                nome=nome)

        except:

            self.obj = None

        self.close()

