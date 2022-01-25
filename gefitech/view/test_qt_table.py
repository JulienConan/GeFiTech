from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from test_Band import test_band

band = band_infos_from_database("Fugazi")
patch_size = 48

def info_from_database(band):
    connexion = sqlite3






class PatchView(QWidget):
    def __init__(self, band=band, patch_size=patch_size):
        super().__init__()

        self.title = "Liste sources"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.patch_size = patch_size
        self.band = band

        #self.creatingTables(self.band)
        #self.show()


    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.patch_size)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Source"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Reference"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Stand"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("PAD"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("48V"))

        while len(band.patch) < 48 :
            band.patch.append({'source' : '',
                'reference' : '',
                'stand' : '',
                'pad' : False,
                '48V' : False })

        for i in range(48):
            count = i+1
            self.tableWidget.setItem(count, 0, QTableWidgetItem(band.patch[i]['source']))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(band.patch[i]['reference']))
            self.tableWidget.setItem(count, 2 , QTableWidgetItem(band.patch[i]['stand']))

            chkBoxPad = QTableWidgetItem()
            chkBoxPad.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            if band.patch[i]['pad'] == False:
                chkBoxPad.setCheckState(QtCore.Qt.Unchecked)
            else:
                chkBoxPad.setCheckState(QtCore.Qt.Checked)
            self.tableWidget.setItem(count, 3 , chkBoxPad)

            chkBox48V = QTableWidgetItem()
            chkBox48V.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            if band.patch[i]['48V'] == False:
                chkBox48V.setCheckState(QtCore.Qt.Unchecked)
            else:
                chkBox48V.setCheckState(QtCore.Qt.Checked)
            self.tableWidget.setItem(count, 4 , chkBox48V)




        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)


        save_button = QtWidgets.QPushButton()
        save_button.setText("Save Patch")
        save_button.clicked.connect(self.save_clicked)
        self.vBoxLayout.addWidget(save_button)

        self.setLayout(self.vBoxLayout)


    def save_clicked(self):
        new_patch=[]
        for i in range(1,48):
            item = {'source' : '',
                'reference' : '',
                'stand' : '',
                'pad' : False,
                '48V' : False}
            item['source'] = self.tableWidget.item(i,0).text()
            item['reference'] = self.tableWidget.item(i,1).text()
            item['stand'] = self.tableWidget.item(i,2).text()
            if self.tableWidget.item(i,3).checkState() == 0:
                item['pad'] = False
            else:
                item['pad'] = True
            if self.tableWidget.item(i,4).checkState() == 0:
                item['48V'] = False
            else:
                item['48V'] = True

            print(self.tableWidget.item(i,4).checkState())
            new_patch.append(item)
        print(new_patch)



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = WindowE(test_band)
    sys.exit(App.exec())
