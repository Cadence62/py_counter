# -*- coding: utf-8 -*-
__author__ = 'mengfan'

from PyQt5 import QtCore, QtGui, QtWidgets
from count_ui import Ui_MainWindow #导入类
import sys

class mydesignershow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mydesignershow,self).__init__()
        #self.ui = Ui_MainWindow()  #创建实例
        self.setupUi(self)#加载窗体  setupu是ui.py的中的函数
        self.pushButton_7.clicked.connect(self.pr1)
        self.pushButton_3.clicked.connect(self.pr1)
        self.pushButton_11.clicked.connect(self.pr1)
        self.pushButton_12.clicked.connect(self.pr1)
        self.pushButton_13.clicked.connect(self.pr1)
        self.pushButton_5.clicked.connect(self.pr1)
        self.pushButton_4.clicked.connect(self.pr1)
        self.pushButton_9.clicked.connect(self.pr1)
        self.pushButton_8.clicked.connect(self.pr1)
        self.pushButton_10.clicked.connect(self.pr1)
        self.pushButton_6.clicked.connect(self.pr1)
        self.pushButton_2.clicked.connect(self.pr1)
        self.pushButton_17.clicked.connect(self.pr1)
        self.pushButton_15.clicked.connect(self.pr1)
        self.pushButton_16.clicked.connect(self.pr1)
        self.pushButton_14.clicked.connect(self.pr1)
        self.pushButton_21.clicked.connect(self.clear)            # c
        self.pushButton.clicked.connect(self.returns)  # =



    def pr1(self):
        sender = self.sender()  #确定信号来自那个按钮
        str1 = self.lineEdit.text()
        self.value = sender.text()

        self.lineEdit.setText(str1 + self.value)

    def returns(self):
        str1 = self.lineEdit.text()
        self.lineEdit.setText(str(eval(str1)))

    def clear(self):
        self.lineEdit.setText(" ")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mydesignershow()       #创建实例
    myshow.show()                   #使用Qmainwindow 的 show 方法 Qwident
    sys.exit(app.exec_())