from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QWidget

def clicked():
    button=app.sender()
    text=button.text()
    if text=='=':
        symbool=textbox.text()
        try:
            res=eval(symbool.replace('÷','/').replace('×','*'))
            textbox.setText(str(res))
        except:
            textbox.setText("Error")    
    elif text=='C':
        textbox.clear()
    elif text=='⌫':
        textbox.backspace()    
    else:
        current_text=textbox.text()
        textbox.setText(current_text+text)
            

app=QApplication([])
window=QWidget()
window.resize(300,500)
window.setWindowTitle("Calculator")

MainLayout=QVBoxLayout()
gridLayout=QGridLayout()
calculator_symbols = [
    'C', '±', '%', '÷',
    '7', '8', '9', '×',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '.', '0', '=', '⌫'
]
textbox=QLineEdit()
textbox.setFixedHeight(50)
MainLayout.addWidget(textbox)

row=0
column=0
for i in calculator_symbols:
    button = QPushButton(i)
    button.setFixedSize(100,100)
    button.clicked.connect(clicked)
    button.setStyleSheet("font-size: 24px;color: white;")
    if column>3:
        column=0
        row+=1
    column+=1    
    gridLayout.addWidget(button,row,column)
    gridLayout.setSpacing(0)
    

MainLayout.addLayout(gridLayout)

window.setStyleSheet("Qwidget{background-color: #fffffc;}QPushButton{background-color: #4a4e69;}QLineEdit{color: black;font-size: 24px;}")
window.setLayout(MainLayout)
window.show()
app.exec_()