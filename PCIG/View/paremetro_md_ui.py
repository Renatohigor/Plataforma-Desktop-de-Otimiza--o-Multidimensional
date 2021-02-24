# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paremetro_md.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class parametros_determini_Dialog(QtWidgets.QDialog,object):
    list_oz=None
    def __init__(self,list_oz):
        QtWidgets.QDialog.__init__(self)
        self.list_oz =list_oz
        self.setupUi()


    def setupUi(self):
        self.setObjectName("Dialog1")
        self.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontalLayoutWidget.setFont(font)
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
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(-10000)
        self.doubleSpinBox.setValue(1.0)
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 120, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setValue(1)
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 170, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def print_list_box_oz(self):
        _translate = QtCore.QCoreApplication.translate
        j = 0
        print(self.list_oz)
        self.comboBox.clear()
        for i in self.list_oz:
            self.comboBox.addItem('')
            self.comboBox.setItemText(j, _translate("MainWindow", str(i)))
            j += 1

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ponto inicial"))
        self.label_3.setText(_translate("Dialog", "precisão"))
        self.label_4.setText(_translate("Dialog", "iteração maxima"))
        self.label_5.setText(_translate("Dialog", "Método de  ordem zero"))
        self.pushButton.setText(_translate("Dialog", "Salver"))
        self.print_list_box_oz()
        self.pushButton.clicked.connect(self.salvar)


    def salvar(self):
        try:
            pre = self.lineEdit_3.text()
            pre = float(pre.replace(',', '.'))
            mdoz = self.comboBox.currentText()
            ponto_inicial = float(self.doubleSpinBox.text().replace(',', '.'))
            nger = int(self.spinBox.text())
            self.parametro = [ponto_inicial, nger, pre,mdoz]
        except:
            self.parametro.clear()

        self.close()

# import sys
# app = QtWidgets.QApplication(sys.argv)
# a=['a','b','c','d']
# ui = parametros_determini_Dialog(a)
# ui.show()
# sys.exit(app.exec_())
