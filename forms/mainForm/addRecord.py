from PyQt5 import QtCore, QtGui, QtWidgets
from showForms import dbForm, dbFormWindow


def addRecordOnClick():
    _translate = QtCore.QCoreApplication.translate
    dbForm.label.setText(_translate("guideForm", "Добавить запись"))

    dbFormWindow.show()
