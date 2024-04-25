from PyQt5 import QtCore, QtGui, QtWidgets
from showForms import dbForm, dbFormWindow


def delRecordOnClick():
    _translate = QtCore.QCoreApplication.translate
    dbForm.label.setText(_translate("guideForm", "Удалить запись"))

    dbFormWindow.show()