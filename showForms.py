from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

MainForm, Window = uic.loadUiType("Forms/mainForm/mainForm.ui")
DbForm, DbFormWindow = uic.loadUiType("Forms/dbForm/dbForm.ui")
GuideForm, GuideFormWindow = uic.loadUiType("Forms/guideForm/guideForm.ui")

app = QApplication([])

mainWindow = Window()
dbFormWindow = DbFormWindow()
guideFormWindow = GuideFormWindow()

mainForm = MainForm()
dbForm = DbForm()
guideForm = GuideForm()

mainForm.setupUi(mainWindow)
dbForm.setupUi(dbFormWindow)
guideForm.setupUi(guideFormWindow)

mainWindow.show()