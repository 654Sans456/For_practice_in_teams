from PyQt5 import QtCore, QtGui, QtWidgets
from showForms import guideForm, guideFormWindow
#from Forms.guideForm.guideForm import *

def customerOnClick():
    _translate = QtCore.QCoreApplication.translate
    guideForm.label.setText(_translate("guideForm", "Клиенты"))
    
    #rowPosition = Ui_guideDialog.tableWidget.rowCount()
    
    #Ui_guideDialog.tableWidget.insertRow(rowPosition)
    #Ui_guideDialog.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem("text1"))

    guideFormWindow.show()

