from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from showForms import dbForm, dbFormWindow


def delRecordOnClick():
    # _translate = QtCore.QCoreApplication.translate
    # dbForm.label.setText(_translate("guideForm", "Удалить запись"))

    # dbFormWindow.show()

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText('Вы уверерены в удалении записи?')
    msg.setWindowTitle('Вопрос')
    okButton = msg.addButton('Да', QMessageBox.ButtonRole.YesRole)
    noButton = msg.addButton('Нет', QMessageBox.ButtonRole.NoRole)

    msg.exec_()

    if msg.clickedButton() == okButton:
        print('Да')

    if msg.clickedButton() == noButton:
        print('Нет')