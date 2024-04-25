from PyQt5 import QtCore, QtGui, QtWidgets
from showForms import guideForm, guideFormWindow


def statusOnClick():
    _translate = QtCore.QCoreApplication.translate
    guideForm.label.setText(_translate("guideForm", "Статусы"))

    guideFormWindow.show()