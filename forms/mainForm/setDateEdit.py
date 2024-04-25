from showForms import mainForm
from PyQt5 import QtCore

def setDateIn():
    mainForm.dateEditIn.setDate(QtCore.QDate.currentDate())

def setDateOut():
    mainForm.dateEditOut.setDate(QtCore.QDate.currentDate())


def changeDateIn():
    print(mainForm.dateEditIn.dateTime().toString('dd.MM.yyyy'))

def changeDateOut():
    print(mainForm.dateEditOut.dateTime().toString('dd.MM.yyyy'))


