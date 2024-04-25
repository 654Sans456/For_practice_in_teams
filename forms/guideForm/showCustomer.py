from PyQt5 import QtCore, QtGui, QtWidgets
from showForms import guideForm, guideFormWindow


def customerOnClick():
    _translate = QtCore.QCoreApplication.translate
    guideForm.label.setText(_translate("guideForm", "Клиенты"))

    guideFormWindow.show()

