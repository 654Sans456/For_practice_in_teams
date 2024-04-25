from showForms import mainForm

def onClickCalendar():
    print(mainForm.calendarWidget.selectedDate().toString('dd.MM.yyyy'))