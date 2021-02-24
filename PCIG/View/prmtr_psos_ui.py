# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prmtr_psos.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class prmtr_pso(QtWidgets.QDialog,object):

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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 348, 174))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_w_in = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_w_in.setFont(font)
        self.lineEdit_w_in.setObjectName("lineEdit_w_in")
        self.gridLayout.addWidget(self.lineEdit_w_in, 3, 1, 1, 1)
        self.lineEdit_c1_in = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_c1_in.setFont(font)
        self.lineEdit_c1_in.setObjectName("lineEdit_c1_in")
        self.gridLayout.addWidget(self.lineEdit_c1_in, 1, 1, 1, 1)
        self.lineEdit_c2_fi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_c2_fi.setFont(font)
        self.lineEdit_c2_fi.setObjectName("lineEdit_c2_fi")
        self.gridLayout.addWidget(self.lineEdit_c2_fi, 2, 3, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setValue(1)
        self.gridLayout.addWidget(self.spinBox_3, 0, 3, 1, 1)
        self.lineEdit_c1_fi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_c1_fi.setFont(font)
        self.lineEdit_c1_fi.setObjectName("lineEdit_c1_fi")
        self.gridLayout.addWidget(self.lineEdit_c1_fi, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.spinBox_nger = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_nger.setFont(font)
        self.spinBox_nger.setObjectName("spinBox_nger")
        self.spinBox_nger.setMinimum(1)
        self.spinBox_nger.setValue(1)
        self.gridLayout.addWidget(self.spinBox_nger, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_c2_in = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_c2_in.setFont(font)
        self.lineEdit_c2_in.setObjectName("lineEdit_c2_in")
        self.gridLayout.addWidget(self.lineEdit_c2_in, 2, 1, 1, 1)
        self.npop = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.npop.setFont(font)
        self.npop.setObjectName("npop")
        self.gridLayout.addWidget(self.npop, 0, 2, 1, 1)
        self.lineEdit_w_fin = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_w_fin.setFont(font)
        self.lineEdit_w_fin.setObjectName("lineEdit_w_fin")
        self.gridLayout.addWidget(self.lineEdit_w_fin, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)
        self.pushButton_salva.clicked.connect(self.salvar)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def salvar(self):
        try:
            c1_fi= self.lineEdit_c1_fi.text()
            c1_fi = float(c1_fi.replace(',', '.')) if c1_fi is not '' else None
            c1_in = self.lineEdit_c1_in.text()
            c1_in = float(c1_in.replace(',', '.')) if c1_in is not '' else None
            c2_fi = self.lineEdit_c2_fi.text()
            c2_fi = float(c2_fi.replace(',', '.')) if c2_fi is not '' else None
            c2_in = self.lineEdit_c2_in.text()
            c2_in = float(c2_in.replace(',', '.')) if c2_in is not '' else None
            w_in = self.lineEdit_w_in.text()
            w_in = float(w_in.replace(',', '.')) if w_in is not '' else None
            w_fi = self.lineEdit_w_fin.text()
            w_fi = float(w_fi.replace(',', '.')) if w_fi is not '' else None
            nger = int(self.spinBox_nger.text())
            npop = int(self.spinBox_3.text())

            self.parametro = [npop, nger, c1_in, c1_fi, c2_in, c2_fi,w_in,w_fi]
        except:
            self.parametro=None
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_salva.setText(_translate("Dialog", "Salver"))
        self.label_8.setText(_translate("Dialog", "w"))
        self.label_4.setText(_translate("Dialog", "c2"))
        self.label.setText(_translate("Dialog", "NGER"))
        self.npop.setText(_translate("Dialog", "NPOP"))
        self.label_3.setText(_translate("Dialog", "c1"))
        self.label_5.setText(_translate("Dialog", " ate"))
        self.label_6.setText(_translate("Dialog", " ate"))
        self.label_7.setText(_translate("Dialog", " ate"))



