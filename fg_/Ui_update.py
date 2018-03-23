# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\all_file\fg\update.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update(object):
    def setupUi(self, update):
        update.setObjectName("update")
        update.resize(415, 228)
        self.pushButton_4 = QtWidgets.QPushButton(update)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 180, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(update)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(update)
        self.label.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(update)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(update)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(update)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 251, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(update)
        QtCore.QMetaObject.connectSlotsByName(update)

    def retranslateUi(self, update):
        _translate = QtCore.QCoreApplication.translate
        update.setWindowTitle(_translate("update", "更新"))
        self.pushButton_4.setText(_translate("update", "取消"))
        self.pushButton_3.setText(_translate("update", "更新"))
        self.label.setText(_translate("update", "新品牌公司："))
        self.label_2.setText(_translate("update", "原品牌公司："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update = QtWidgets.QWidget()
    ui = Ui_update()
    ui.setupUi(update)
    update.show()
    sys.exit(app.exec_())

