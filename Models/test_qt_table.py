from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from band import Band
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Liste sources"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400

        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.creatingTables()
        self.show()

    def creatingTables(self):
        b = Band()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(48)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Source"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Reference"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Stand"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("PAD"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("48V"))
        

        for i in range(48):
            count = i+1
            self.tableWidget.setItem(count, 0, QTableWidgetItem(b.sources_list[i]['source']))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(b.sources_list[i]['reference']))
            self.tableWidget.setItem(count, 2 , QTableWidgetItem(b.sources_list[i]['stand']))
            
            chkBoxPad = QTableWidgetItem()
            chkBoxPad.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            if b.sources_list[i]['pad'] == False:
                chkBoxPad.setCheckState(QtCore.Qt.Unchecked) 
            else:
                chkBoxPad.setCheckState(QtCore.Qt.Checked) 
            self.tableWidget.setItem(count, 3 , chkBoxPad)
            
            chkBox48V = QTableWidgetItem()
            chkBox48V.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            if b.sources_list[i]['48V'] == False:
                chkBox48V.setCheckState(QtCore.Qt.Unchecked) 
            else:
                chkBox48V.setCheckState(QtCore.Qt.Checked) 
            self.tableWidget.setItem(count, 4 , chkBox48V)
           
           


        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())