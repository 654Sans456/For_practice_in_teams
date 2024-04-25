from PyQt5 import QtCore, QtGui, QtWidgets
from showForms import dbForm, dbFormWindow


def editRecordOnClick():
    _translate = QtCore.QCoreApplication.translate
    dbForm.label.setText(_translate("guideForm", "Изменить запись"))

    dbFormWindow.show()