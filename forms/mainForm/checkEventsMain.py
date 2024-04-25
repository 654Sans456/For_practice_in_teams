from showForms import mainForm


def checkEventsMain():
    from Forms.guideForm.showCustomer import customerOnClick
    from Forms.guideForm.showExecutor import executorOnClick
    from Forms.guideForm.showStatus import statusOnClick
    from Forms.mainForm.addRecord import addRecordOnClick
    from Forms.mainForm.delRecord import delRecordOnClick
    from Forms.mainForm.editRecord import editRecordOnClick

    from Forms.mainForm.setDateEdit import setDateIn, setDateOut, changeDateIn, changeDateOut
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

    mainForm.dateEditIn.dateChanged.connect(changeDateIn)
    mainForm.dateEditOut.dateChanged.connect(changeDateOut)