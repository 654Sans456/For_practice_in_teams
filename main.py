# работа с базой данных
# https://russianblogs.com/article/18821207818/
# https://www.codetd.com/ru/article/6892811

# https://stackoverflow.com/questions/21013356/how-to-display-in-qtablewidget-the-data-from-sqlite
# https://www.youtube.com/watch?v=YySB6tkjZ7Y
# https://www.piknad.ru/pyQtable3.php?ysclid=lsdge4h541231181510
# https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableWidget.html
# структура запроса в поисковике: как в PyQt5 вывести базу данных в QTableWidget

from showForms import mainForm, dbForm, guideForm, app


from Forms.guideForm.showCustomer import customerOnClick
from Forms.guideForm.showExecutor import executorOnClick
from Forms.guideForm.showStatus import statusOnClick
from Forms.mainForm.addRecord import addRecordOnClick
from Forms.mainForm.delRecord import delRecordOnClick
from Forms.mainForm.editRecord import editRecordOnClick

from Forms.mainForm.setDateEdit import setDateIn, setDateOut
from Forms.mainForm.onClickCalendar import onClickCalendar

setDateIn()
setDateOut()



mainForm.customerButton.clicked.connect(customerOnClick)
mainForm.executorButton.clicked.connect(executorOnClick)
mainForm.statusButton.clicked.connect(statusOnClick)


mainForm.addButton.clicked.connect(addRecordOnClick)
mainForm.delButton.clicked.connect(delRecordOnClick)
mainForm.editButton.clicked.connect(editRecordOnClick)

mainForm.calendarWidget.clicked.connect(onClickCalendar)




app.exec()