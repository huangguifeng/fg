# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\all_file\fg_\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 811, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 200, 331, 71))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 54, 12))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 721, 111))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 60, 161, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(510, 60, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(280, 40, 54, 12))
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.comboBox_4.setMaxVisibleItems(14)
        self.comboBox_4.setObjectName("comboBox_4")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(320, 10, 51, 31))
        self.spinBox.setObjectName("spinBox")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 280, 781, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(420, 20, 71, 20))
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 190, 381, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(160, 20, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(250, 20, 54, 12))
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 40, 41, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 40, 41, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 40, 41, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(500, 10, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 280, 781, 271))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_3.setGeometry(QtCore.QRect(320, 10, 51, 31))
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(420, 20, 71, 20))
        self.label_20.setObjectName("label_20")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(500, 10, 231, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(10, 180, 54, 12))
        self.label_21.setObjectName("label_21")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 60, 721, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_7.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_8.setGeometry(QtCore.QRect(280, 60, 161, 31))
        self.comboBox_8.setObjectName("comboBox_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 60, 101, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(280, 40, 54, 12))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(260, 20, 54, 12))
        self.label_24.setObjectName("label_24")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_9.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.comboBox_9.setMaxVisibleItems(14)
        self.comboBox_9.setObjectName("comboBox_9")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 200, 331, 71))
        self.textEdit_3.setObjectName("textEdit_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(350, 190, 381, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_25 = QtWidgets.QLabel(self.groupBox_6)
        self.label_25.setGeometry(QtCore.QRect(160, 20, 54, 12))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_6)
        self.label_26.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_6)
        self.label_27.setGeometry(QtCore.QRect(250, 20, 54, 12))
        self.label_27.setObjectName("label_27")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_10.setGeometry(QtCore.QRect(70, 40, 41, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_11.setGeometry(QtCore.QRect(160, 40, 41, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_12.setGeometry(QtCore.QRect(250, 40, 41, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 280, 781, 271))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_4.setGeometry(QtCore.QRect(320, 10, 51, 31))
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(420, 20, 71, 20))
        self.label_29.setObjectName("label_29")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(500, 10, 231, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(10, 180, 54, 12))
        self.label_30.setObjectName("label_30")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 60, 721, 111))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 60, 101, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_10.setGeometry(QtCore.QRect(280, 60, 161, 31))
        self.comboBox_10.setObjectName("comboBox_10")
        self.label_31 = QtWidgets.QLabel(self.groupBox_7)
        self.label_31.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label_31.setObjectName("label_31")
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_11.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.comboBox_11.setObjectName("comboBox_11")
        self.label_32 = QtWidgets.QLabel(self.groupBox_7)
        self.label_32.setGeometry(QtCore.QRect(280, 40, 54, 12))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        self.label_33.setGeometry(QtCore.QRect(260, 20, 54, 12))
        self.label_33.setObjectName("label_33")
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_12.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.comboBox_12.setMaxVisibleItems(14)
        self.comboBox_12.setObjectName("comboBox_12")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 200, 331, 71))
        self.textEdit_4.setObjectName("textEdit_4")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(350, 190, 381, 81))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_34 = QtWidgets.QLabel(self.groupBox_8)
        self.label_34.setGeometry(QtCore.QRect(160, 20, 54, 12))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.groupBox_8)
        self.label_35.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox_8)
        self.label_36.setGeometry(QtCore.QRect(250, 20, 54, 12))
        self.label_36.setObjectName("label_36")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_14.setGeometry(QtCore.QRect(70, 40, 41, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_15.setGeometry(QtCore.QRect(160, 40, 41, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_16.setGeometry(QtCore.QRect(250, 40, 41, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setGeometry(QtCore.QRect(350, 190, 381, 81))
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_37 = QtWidgets.QLabel(self.groupBox_9)
        self.label_37.setGeometry(QtCore.QRect(160, 20, 54, 12))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_9)
        self.label_38.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_9)
        self.label_39.setGeometry(QtCore.QRect(250, 20, 54, 12))
        self.label_39.setObjectName("label_39")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_17.setGeometry(QtCore.QRect(70, 40, 41, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_18.setGeometry(QtCore.QRect(160, 40, 41, 31))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_19.setGeometry(QtCore.QRect(250, 40, 41, 31))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_40 = QtWidgets.QLabel(self.tab_4)
        self.label_40.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_40.setObjectName("label_40")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 280, 781, 271))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_20.setGeometry(QtCore.QRect(500, 10, 231, 31))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.spinBox_5 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_5.setGeometry(QtCore.QRect(320, 10, 51, 31))
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_41 = QtWidgets.QLabel(self.tab_4)
        self.label_41.setGeometry(QtCore.QRect(420, 20, 71, 20))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.tab_4)
        self.label_42.setGeometry(QtCore.QRect(260, 20, 54, 12))
        self.label_42.setObjectName("label_42")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 60, 721, 111))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_43 = QtWidgets.QLabel(self.groupBox_10)
        self.label_43.setGeometry(QtCore.QRect(280, 40, 54, 12))
        self.label_43.setObjectName("label_43")
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_13.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.comboBox_13.setObjectName("comboBox_13")
        self.label_44 = QtWidgets.QLabel(self.groupBox_10)
        self.label_44.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label_44.setObjectName("label_44")
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_14.setGeometry(QtCore.QRect(280, 60, 161, 31))
        self.comboBox_14.setObjectName("comboBox_14")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_9.setGeometry(QtCore.QRect(510, 60, 101, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 200, 331, 71))
        self.textEdit_5.setObjectName("textEdit_5")
        self.comboBox_15 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_15.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.comboBox_15.setMaxVisibleItems(14)
        self.comboBox_15.setObjectName("comboBox_15")
        self.label_45 = QtWidgets.QLabel(self.tab_4)
        self.label_45.setGeometry(QtCore.QRect(10, 180, 54, 12))
        self.label_45.setObjectName("label_45")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_46 = QtWidgets.QLabel(self.tab_5)
        self.label_46.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.tab_5)
        self.label_47.setGeometry(QtCore.QRect(10, 180, 54, 12))
        self.label_47.setObjectName("label_47")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_11.setGeometry(QtCore.QRect(350, 190, 381, 81))
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_58 = QtWidgets.QLabel(self.groupBox_11)
        self.label_58.setGeometry(QtCore.QRect(160, 20, 54, 12))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.groupBox_11)
        self.label_59.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.groupBox_11)
        self.label_60.setGeometry(QtCore.QRect(250, 20, 54, 12))
        self.label_60.setObjectName("label_60")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_27.setGeometry(QtCore.QRect(70, 40, 41, 31))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_28.setGeometry(QtCore.QRect(160, 40, 41, 31))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_29.setGeometry(QtCore.QRect(250, 40, 41, 31))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 60, 721, 111))
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_61 = QtWidgets.QLabel(self.groupBox_12)
        self.label_61.setGeometry(QtCore.QRect(280, 40, 54, 12))
        self.label_61.setObjectName("label_61")
        self.comboBox_20 = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_20.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.comboBox_20.setObjectName("comboBox_20")
        self.label_62 = QtWidgets.QLabel(self.groupBox_12)
        self.label_62.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label_62.setObjectName("label_62")
        self.comboBox_21 = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_21.setGeometry(QtCore.QRect(280, 60, 161, 31))
        self.comboBox_21.setObjectName("comboBox_21")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_12.setGeometry(QtCore.QRect(510, 60, 101, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_63 = QtWidgets.QLabel(self.tab_5)
        self.label_63.setGeometry(QtCore.QRect(420, 20, 71, 20))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.tab_5)
        self.label_64.setGeometry(QtCore.QRect(260, 20, 54, 12))
        self.label_64.setObjectName("label_64")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 200, 331, 71))
        self.textEdit_6.setObjectName("textEdit_6")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_30.setGeometry(QtCore.QRect(500, 10, 231, 31))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.spinBox_6 = QtWidgets.QSpinBox(self.tab_5)
        self.spinBox_6.setGeometry(QtCore.QRect(320, 10, 51, 31))
        self.spinBox_6.setObjectName("spinBox_6")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_6.setGeometry(QtCore.QRect(10, 280, 781, 271))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.comboBox_22 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_22.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.comboBox_22.setMaxVisibleItems(14)
        self.comboBox_22.setObjectName("comboBox_22")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.action58 = QtWidgets.QAction(MainWindow)
        self.action58.setObjectName("action58")
        self.actiond = QtWidgets.QAction(MainWindow)
        self.actiond.setObjectName("actiond")
        self.actionga = QtWidgets.QAction(MainWindow)
        self.actionga.setObjectName("actionga")
        self.actionz = QtWidgets.QAction(MainWindow)
        self.actionz.setObjectName("actionz")
        self.actionqc = QtWidgets.QAction(MainWindow)
        self.actionqc.setObjectName("actionqc")
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.actionabout)
        self.menu_3.addAction(self.action58)
        self.menu_3.addAction(self.actiond)
        self.menu_3.addAction(self.actionga)
        self.menu_3.addAction(self.actionz)
        self.menu_3.addAction(self.actionqc)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "招聘网职位覆盖率"))
        self.label.setText(_translate("MainWindow", "地市："))
        self.label_2.setText(_translate("MainWindow", "抓取页数："))
        self.groupBox.setTitle(_translate("MainWindow", "职位类型"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.label_3.setText(_translate("MainWindow", "职位大类："))
        self.label_4.setText(_translate("MainWindow", "职位小类："))
        self.label_5.setText(_translate("MainWindow", "状态："))
        self.label_6.setText(_translate("MainWindow", "同行公司名："))
        self.groupBox_2.setTitle(_translate("MainWindow", "数据"))
        self.label_10.setText(_translate("MainWindow", "符合条件"))
        self.label_11.setText(_translate("MainWindow", "抓取职位"))
        self.label_9.setText(_translate("MainWindow", "职位占比"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "58同城"))
        self.label_19.setText(_translate("MainWindow", "地市："))
        self.label_20.setText(_translate("MainWindow", "同行公司名："))
        self.label_21.setText(_translate("MainWindow", "状态："))
        self.groupBox_5.setTitle(_translate("MainWindow", "职位类型"))
        self.pushButton_7.setText(_translate("MainWindow", "开始"))
        self.label_22.setText(_translate("MainWindow", "职位大类："))
        self.label_23.setText(_translate("MainWindow", "职位小类："))
        self.label_24.setText(_translate("MainWindow", "抓取页数："))
        self.groupBox_6.setTitle(_translate("MainWindow", "数据"))
        self.label_25.setText(_translate("MainWindow", "符合条件"))
        self.label_26.setText(_translate("MainWindow", "抓取职位"))
        self.label_27.setText(_translate("MainWindow", "职位占比"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "智联招聘"))
        self.label_28.setText(_translate("MainWindow", "地市："))
        self.label_29.setText(_translate("MainWindow", "同行公司名："))
        self.label_30.setText(_translate("MainWindow", "状态："))
        self.groupBox_7.setTitle(_translate("MainWindow", "职位类型"))
        self.pushButton_8.setText(_translate("MainWindow", "开始"))
        self.label_31.setText(_translate("MainWindow", "职位大类："))
        self.label_32.setText(_translate("MainWindow", "职位小类："))
        self.label_33.setText(_translate("MainWindow", "抓取页数："))
        self.groupBox_8.setTitle(_translate("MainWindow", "数据"))
        self.label_34.setText(_translate("MainWindow", "符合条件"))
        self.label_35.setText(_translate("MainWindow", "抓取职位"))
        self.label_36.setText(_translate("MainWindow", "职位占比"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "赶集网"))
        self.groupBox_9.setTitle(_translate("MainWindow", "数据"))
        self.label_37.setText(_translate("MainWindow", "符合条件"))
        self.label_38.setText(_translate("MainWindow", "抓取职位"))
        self.label_39.setText(_translate("MainWindow", "职位占比"))
        self.label_40.setText(_translate("MainWindow", "地市："))
        self.label_41.setText(_translate("MainWindow", "同行公司名："))
        self.label_42.setText(_translate("MainWindow", "抓取页数："))
        self.groupBox_10.setTitle(_translate("MainWindow", "职位类型"))
        self.label_43.setText(_translate("MainWindow", "职位小类："))
        self.label_44.setText(_translate("MainWindow", "职位大类："))
        self.pushButton_9.setText(_translate("MainWindow", "开始"))
        self.label_45.setText(_translate("MainWindow", "状态："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "中华英才"))
        self.label_46.setText(_translate("MainWindow", "地市："))
        self.label_47.setText(_translate("MainWindow", "状态："))
        self.groupBox_11.setTitle(_translate("MainWindow", "数据"))
        self.label_58.setText(_translate("MainWindow", "符合条件"))
        self.label_59.setText(_translate("MainWindow", "抓取职位"))
        self.label_60.setText(_translate("MainWindow", "职位占比"))
        self.groupBox_12.setTitle(_translate("MainWindow", "职位类型"))
        self.label_61.setText(_translate("MainWindow", "职位小类："))
        self.label_62.setText(_translate("MainWindow", "职位大类："))
        self.pushButton_12.setText(_translate("MainWindow", "开始"))
        self.label_63.setText(_translate("MainWindow", "同行公司名："))
        self.label_64.setText(_translate("MainWindow", "抓取页数："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "前程无忧"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.menu_3.setTitle(_translate("MainWindow", "添加公司品牌"))
        self.action.setText(_translate("MainWindow", "帮助"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.action58.setText(_translate("MainWindow", "58同城"))
        self.actiond.setText(_translate("MainWindow", "智联"))
        self.actionga.setText(_translate("MainWindow", "赶集"))
        self.actionz.setText(_translate("MainWindow", "中华英才"))
        self.actionqc.setText(_translate("MainWindow", "前程无忧"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

