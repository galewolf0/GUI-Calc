from PyQt5 import QtCore, QtGui, QtWidgets
import re
import sys
global firstKeyPressFlag
firstKeyPressFlag = False
global evalFlag
evalFlag = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 714)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(381, 714))
        MainWindow.setMaximumSize(QtCore.QSize(381, 714))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, -10, 401, 741))
        self.widget.setStyleSheet("background-color:rgb(40, 40, 43)")
        self.widget.setObjectName("widget")
        self.Screen = QtWidgets.QLabel(self.widget)
        self.Screen.setGeometry(QtCore.QRect(10, 30, 381, 131))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.Screen.setFont(font)
        self.Screen.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Screen.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Screen.setAutoFillBackground(False)
        self.Screen.setStyleSheet("background-color:rgb(40, 40, 43);\n"
"color:white")
        self.Screen.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Screen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Screen.setWordWrap(True)
        self.Screen.setObjectName("Screen")
        self.CButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("C"))
        self.CButton.setGeometry(QtCore.QRect(30, 200, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CButton.setFont(font)
        self.CButton.setStyleSheet("color:red")
        self.CButton.setObjectName("CButton")
        self.divideButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.checkOp("/"))
        self.divideButton.setGeometry(QtCore.QRect(120, 200, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.divideButton.setFont(font)
        self.divideButton.setStyleSheet("color:rgb(0, 255, 204)")
        self.divideButton.setObjectName("divideButton")
        self.xButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.checkOp("x"))
        self.xButton.setGeometry(QtCore.QRect(210, 200, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xButton.setFont(font)
        self.xButton.setStyleSheet("color:rgb(0, 255, 204)")
        self.xButton.setObjectName("xButton")
        self.minusButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.checkOp("-"))
        self.minusButton.setGeometry(QtCore.QRect(300, 200, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("color:rgb(0, 255, 204)")
        self.minusButton.setObjectName("minusButton")
        self.sevenButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(30, 300, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("color:white")
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(120, 300, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("color:white")
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(210, 300, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("color:white")
        self.nineButton.setObjectName("nineButton")
        self.fourButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(30, 400, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("color:white")
        self.fourButton.setObjectName("fourButton")
        self.oneButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(30, 500, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("color:white")
        self.oneButton.setObjectName("oneButton")
        self.fiveButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(120, 400, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("color:white")
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(210, 400, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("color:white")
        self.sixButton.setObjectName("sixButton")
        self.plusButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.checkOp("+"))
        self.plusButton.setGeometry(QtCore.QRect(300, 300, 71, 181))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plusButton.setFont(font)
        self.plusButton.setStyleSheet("color:rgb(0, 255, 204)")
        self.plusButton.setObjectName("plusButton")
        self.twoButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(120, 500, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("color:white")
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(210, 500, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("color:white")
        self.threeButton.setObjectName("threeButton")
        self.equalButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.eval())
        self.equalButton.setGeometry(QtCore.QRect(300, 500, 71, 181))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("color:white;\n"
"background-color:rgb(0, 255, 204)")
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(30, 600, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("color:white")
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.checkDot("."))
        self.decimalButton.setGeometry(QtCore.QRect(210, 600, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.decimalButton.setFont(font)
        self.decimalButton.setStyleSheet("color:white\n"
"")
        self.decimalButton.setObjectName("decimalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def splitByOp(self, screen):
        return re.findall(r'[\d.]+|\+|-|\*|/|\(|\)', screen)
    
    def eval(self):
        s = self.Screen.text()
        if s[-1] == "+" or s[-1] == "-" or s[-1] == "x" or s[-1] == "/":
            pass
        else:
            s = s.replace('x', '*')
            answer = str(eval(s))
            displayAnswer = answer
            if "." in answer:
                 man = answer.split(".")
                 decimal = man[-1][:3] if len(man[-1]) > 3 else man[-1]
                 displayAnswer = man[0] if int(decimal) == 0 else man[0] + "." + decimal 
            self.Screen.setText(displayAnswer)
            global evalFlag
            evalFlag = True
    
    def checkOp(self, op):
        global firstKeyPressFlag
        global evalFlag
        if not firstKeyPressFlag:
            firstKeyPressFlag = True
            self.press_it("C")
        s = self.Screen.text()
        if s == "0":
            if op == "+" or op == "x" or op == "/":
                pass
            else:
                self.press_it("-")
        elif (s[-1] == "x" or s[-1] == "/") and op == "-":
            self.press_it("-")
        elif s[-1] == "+" or s[-1] == "-" or s[-1] == "x" or s[-1] == "/":
            pass
        else:
            self.checkDot(op)

    def checkDot(self, op):
        s = self.Screen.text()
        if s[-1] == ".":
            pass
        elif op == "+" or op == "-" or op == "x" or op == "/": 
            self.press_it(op)  
        else:
            self.dot()

    def dot(self):
        global firstKeyPressFlag
        global evalFlag
        if not firstKeyPressFlag:
            firstKeyPressFlag = True
            self.press_it("C")
        s = self.Screen.text()
        screenList = self.splitByOp(s)
        if s == "0" or evalFlag == True:
            evalFlag = False
            self.Screen.setText("0.")
        elif s[-1] == "+" or s[-1] == "-" or s[-1] == "x" or s[-1] == "/":
            self.Screen.setText(f"{self.Screen.text()}0.")
        elif "." in screenList[-1]:
            pass
        else:
            self.Screen.setText(f"{s}.")
        
    
    def press_it(self, pressed):
        global firstKeyPressFlag
        global evalFlag
        if pressed == "C":
            self.Screen.setText("0")
        else:          
            if not firstKeyPressFlag:
                firstKeyPressFlag = True
                self.press_it("C")
            if (pressed == "+" or pressed == "-" or pressed == "x" or pressed == "/") and evalFlag == True:
                evalFlag = False
            elif self.Screen.text() == "0" or evalFlag == True:
                evalFlag = False
                self.Screen.setText("")
            self.Screen.setText(f"{self.Screen.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.Screen.setText(_translate("MainWindow", "0"))
        self.CButton.setText(_translate("MainWindow", "C"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.xButton.setText(_translate("MainWindow", "x"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.decimalButton.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
