# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\all_file\fg\insert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_insert(object):
    def setupUi(self, insert):
        insert.setObjectName("insert")
        insert.resize(415, 225)
        self.pushButton = QtWidgets.QPushButton(insert)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(insert)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(insert)
        self.label.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(insert)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 251, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(insert)
        QtCore.QMetaObject.connectSlotsByName(insert)

    def retranslateUi(self, insert):
        _translate = QtCore.QCoreApplication.translate
        insert.setWindowTitle(_translate("insert", "新增"))
        self.pushButton.setText(_translate("insert", "新增"))
        self.pushButton_2.setText(_translate("insert", "取消"))
        self.label.setText(_translate("insert", "新增品牌公司："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    insert = QtWidgets.QWidget()
    ui = Ui_insert()
    ui.setupUi(insert)
    insert.show()
    sys.exit(app.exec_())

