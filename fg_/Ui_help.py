# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\fg\help.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(631, 412)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Help)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 631, 411))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Help)
        self.pushButton.setGeometry(QtCore.QRect(410, 320, 71, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "帮助"))
        self.plainTextEdit.setPlainText(_translate("Help", "\n"
"\n"
"数据说明：\n"
"    抓取职位：指定页数所有职位总数\n"
"\n"
"    符合条件：属于本公司品牌下的职位\n"
"\n"
"    职位占比：符合条件职位数除以抓取职位的数量，即本公司职位占指定页数总职位数的占比\n"
"\n"
"同行数据：如果需要抓取同行的数据，只需要填写同行的公司名称，如果同行公司名称留空，那么就是抓取本公司的覆盖率。\n"
"\n"
"如果抓取页数比较多，网速比较慢的情况下，抓取完数据比较慢，请稍微等待下，不要频繁点击开始。\n"
"\n"
"城市只包含了本公司所推广的城市！"))
        self.pushButton.setText(_translate("Help", "ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Help = QtWidgets.QWidget()
    ui = Ui_Help()
    ui.setupUi(Help)
    Help.show()
    sys.exit(app.exec_())

