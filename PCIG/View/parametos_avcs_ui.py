# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parametos_avcs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class prametro_acvs(QtWidgets.QDialog,object):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi()
        self.parametro=[]
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(387, 259)
        self.pushButton_salva = QtWidgets.QPushButton(self)
        self.pushButton_salva.setGeometry(QtCore.QRect(160, 210, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_salva.setFont(font)
        self.pushButton_salva.setObjectName("pushButton_salva")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 168))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.npop = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.npop.setFont(font)
        self.npop.setObjectName("npop")
        self.gridLayout.addWidget(self.npop, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBox_nger = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_nger.setMinimum(1)
        self.spinBox_nger.setValue(1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_nger.setFont(font)
        self.spinBox_nger.setObjectName("spinBox_nger")
        self.gridLayout.addWidget(self.spinBox_nger, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.lineEdit_gama = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_gama.setFont(font)
        self.lineEdit_gama.setObjectName("lineEdit_gama")
        self.gridLayout.addWidget(self.lineEdit_gama, 2, 1, 1, 1)
        self.lineEdit_alfa = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_alfa.setFont(font)
        self.lineEdit_alfa.setObjectName("lineEdit_alfa")
        self.gridLayout.addWidget(self.lineEdit_alfa, 1, 1, 1, 1)
        self.lineEdit_tetha = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_tetha.setFont(font)
        self.lineEdit_tetha.setObjectName("lineEdit_tetha")
        self.gridLayout.addWidget(self.lineEdit_tetha, 2, 3, 1, 1)
        self.lineEdit_beta = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_beta.setFont(font)
        self.lineEdit_beta.setObjectName("lineEdit_beta")
        self.gridLayout.addWidget(self.lineEdit_beta, 1, 3, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setValue(1)
        self.gridLayout.addWidget(self.spinBox_3, 0, 3, 1, 1)
        self.lineEdit_beta_min = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_beta_min.setFont(font)
        self.lineEdit_beta_min.setObjectName("lineEdit_beta_min")
        self.gridLayout.addWidget(self.lineEdit_beta_min, 3, 2, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton_salva.clicked.connect(self.salvar)

    def salvar(self):
        try:
            alfa = self.lineEdit_alfa.text()
            alfa = float(alfa.replace(',','.')) if alfa is not ''else None
            beta=self.lineEdit_beta.text()
            beta = float(beta.replace(',','.'))  if beta is not ''else None
            beta_min=self.lineEdit_beta_min.text()
            beta_min = float(beta_min.replace(',','.'))  if beta_min is not ''else None
            gama=self.lineEdit_gama.text()
            gama = float(gama.replace(',','.'))  if gama is not ''else None
            tetha =self.lineEdit_tetha.text()
            tetha = float(tetha.replace(',','.')) if tetha is not ''else None
            nger= int(self.spinBox_nger.text())
            npop= int(self.spinBox_3.text())

            self.parametro=[npop,nger,alfa,beta,beta_min,gama,tetha]
        except:
            self.parametro.clear()
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_salva.setText(_translate("Dialog", "Salver"))
        self.label.setText(_translate("Dialog", "NGER"))
        self.npop.setText(_translate("Dialog", "NPOP"))
        self.label_3.setText(_translate("Dialog", "Alfa"))
        self.label_4.setText(_translate("Dialog", "Gama"))
        self.label_7.setText(_translate("Dialog", "Tetha"))
        self.label_6.setText(_translate("Dialog", "Beta"))
        self.label_8.setText(_translate("Dialog", "Beta_min"))



