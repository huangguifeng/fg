# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\all_file\fg\delete.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_delete_2(object):
    def setupUi(self, delete_2):
        delete_2.setObjectName("delete_2")
        delete_2.resize(416, 225)
        self.pushButton_4 = QtWidgets.QPushButton(delete_2)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 150, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(delete_2)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(delete_2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(delete_2)
        self.label.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label.setObjectName("label")

        self.retranslateUi(delete_2)
        QtCore.QMetaObject.connectSlotsByName(delete_2)

    def retranslateUi(self, delete_2):
        _translate = QtCore.QCoreApplication.translate
        delete_2.setWindowTitle(_translate("delete_2", "删除"))
        self.pushButton_4.setText(_translate("delete_2", "取消"))
        self.pushButton_3.setText(_translate("delete_2", "删除"))
        self.label.setText(_translate("delete_2", "删除品牌公司："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_2 = QtWidgets.QWidget()
    ui = Ui_delete_2()
    ui.setupUi(delete_2)
    delete_2.show()
    sys.exit(app.exec_())

