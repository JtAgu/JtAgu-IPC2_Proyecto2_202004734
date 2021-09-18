# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Listas import ListaLineas,ListaProductos,ListaDatos,ListaSimulaciones
from nodos import Pieza
import copy
import webbrowser
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.ListaLineas=ListaLineas()
        self.ListaProductos=ListaProductos()
        self.ListaProductosLinea=ListaProductos()
        self.ListaSimulaciones=ListaSimulaciones()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 524)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.archivo = QtWidgets.QPushButton(self.centralwidget)
        self.archivo.setGeometry(QtCore.QRect(30, 50, 251, 41))
        self.archivo.clicked.connect(self.LeerLineas)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.archivo.setFont(font)
        self.archivo.setObjectName("archivo")
        self.tbTerreno = QtWidgets.QTableView(self.centralwidget)
        self.tbTerreno.setGeometry(QtCore.QRect(310, 50, 461, 421))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        self.tbTerreno.setFont(font)
        self.tbTerreno.setObjectName("tbTerreno")
        self.Reporte = QtWidgets.QPushButton(self.centralwidget)
        self.Reporte.setGeometry(QtCore.QRect(170, 270, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.Reporte.setFont(font)
        self.Reporte.setObjectName("Reporte")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(40, 320, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.procesar = QtWidgets.QPushButton(self.centralwidget)
        self.procesar.setGeometry(QtCore.QRect(40, 270, 111, 41))
        self.procesar.clicked.connect(self.ProcesarSimulacion)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.procesar.setFont(font)
        self.procesar.setObjectName("procesar")
        self.cmbProducto = QtWidgets.QComboBox(self.centralwidget)
        self.cmbProducto.setGeometry(QtCore.QRect(40, 210, 241, 31))
        self.cmbProducto.setObjectName("cmbProducto")
        self.Tiempo = QtWidgets.QLabel(self.centralwidget)
        self.Tiempo.setGeometry(QtCore.QRect(150, 420, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.Tiempo.setFont(font)
        self.Tiempo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Tiempo.setTextFormat(QtCore.Qt.PlainText)
        self.Tiempo.setObjectName("Tiempo")
        self.Tiempo_2 = QtWidgets.QLabel(self.centralwidget)
        self.Tiempo_2.setGeometry(QtCore.QRect(40, 160, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.Tiempo_2.setFont(font)
        self.Tiempo_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Tiempo_2.setTextFormat(QtCore.Qt.PlainText)
        self.Tiempo_2.setObjectName("Tiempo_2")
        self.Tiempo_3 = QtWidgets.QLabel(self.centralwidget)
        self.Tiempo_3.setGeometry(QtCore.QRect(70, 390, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.Tiempo_3.setFont(font)
        self.Tiempo_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Tiempo_3.setTextFormat(QtCore.Qt.PlainText)
        self.Tiempo_3.setObjectName("Tiempo_3")
        self.Tiempo_4 = QtWidgets.QLabel(self.centralwidget)
        self.Tiempo_4.setGeometry(QtCore.QRect(470, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.Tiempo_4.setFont(font)
        self.Tiempo_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Tiempo_4.setTextFormat(QtCore.Qt.PlainText)
        self.Tiempo_4.setObjectName("Tiempo_4")
        self.archivo_articulos = QtWidgets.QPushButton(self.centralwidget)
        self.archivo_articulos.setGeometry(QtCore.QRect(30, 110, 251, 41))
        self.archivo_articulos.clicked.connect(self.LeerSimulacion)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.archivo_articulos.setFont(font)
        self.archivo_articulos.setObjectName("archivo_articulos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Intelligence"))
        self.archivo.setText(_translate("MainWindow", "ARCHIVO DE LINEAS"))
        self.Reporte.setText(_translate("MainWindow", "REPORTE"))
        self.info.setText(_translate("MainWindow", "VER INFORMACION"))
        self.procesar.setText(_translate("MainWindow", "PROCESAR"))
        self.Tiempo.setText(_translate("MainWindow", "0"))
        self.Tiempo_2.setText(_translate("MainWindow", "seleccionar producto"))
        self.Tiempo_3.setText(_translate("MainWindow", "tiempo empleado:"))
        self.Tiempo_4.setText(_translate("MainWindow", "DESCRIPCION"))
        self.archivo_articulos.setText(_translate("MainWindow", "ARCHIVO DE ARTICULOS"))

    def LeerLineas(self):
        buscar = QFileDialog.getOpenFileName()
        mytree = ET.parse(buscar[0])
        myroot = mytree.getroot()
        NLineas=myroot[0].text
        for x in range (int(NLineas)):
            Id=myroot[1][x][0].text
            numeroCom=myroot[1][x][1].text
            TiempoEnsamblaje=myroot[1][x][2].text
            self.ListaLineas.Añadir(Id,numeroCom,TiempoEnsamblaje)
        for x in myroot[2].findall('Producto'):
            Nombre=x[0].text
            Productos=x[1].text
            self.ListaProductos.Añadir(Nombre,Productos)
            c=""
            con=0
            for x in range(len(Productos)):
                if Productos[x]==" ":
                    continue
                c+=Productos[x]
                if len(c)==4:
                    self.ListaProductos.AñadirPiezas(Nombre,c[1],con,c,c[3])
                    c=""
                    con+=1
                
        self.ListaLineas.MostrarDatos()
        self.ListaProductos.MostrarDatos()
            
    def LeerSimulacion(self):
        buscar = QFileDialog.getOpenFileName()
        mytree = ET.parse(buscar[0])
        myroot = mytree.getroot()
        nombreSimulacion=myroot[0].text
        self.cmbProducto.addItem(nombreSimulacion)
        for x in myroot[1].findall('Producto'):
            nombreP=x.text
            aux=self.ListaProductos.obtener(nombreP)
            if aux.nombre==nombreP:
                self.ListaSimulaciones.Añadir(nombreSimulacion,aux)
            else:
                msg=QMessageBox()
                msg.setWindowTitle("OCURRIO UN ERROR")
                msg.setText(nombreP+" no existe en los registros")
                msg.setIcon(QMessageBox.Warning)
                x=msg.exec_()
                
    def ProcesarSimulacion(self):
        nombre=self.cmbProducto.currentText()
        #aux=self.ListaProductos.obtener()
        self.ListaSimulaciones.Procesar(nombre,self.ListaLineas.size,self.ListaLineas)
        self.ListaSimulaciones.Mostrar()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
