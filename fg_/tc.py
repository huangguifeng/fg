# coding=utf-8
from Ui_tc import Ui_MainWindow
import  sys
from  PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget
from PyQt5.QtWidgets import QDesktopWidget  
from PyQt5.QtCore import pyqtSlot

import info
import  spider_58
class combosel(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(combosel, self).__init__()
        self.ui_sel=Ui_MainWindow()
        self.ui_sel.setupUi(self)
        
        self.setWindowTitle('58职位覆盖率')
         # self.ui_sel.comboBox_province.addItem(QtGui.QIcon('../Document/images/favicon.ico'),'sd')   # 添加 qico图标
        self.ui_sel.comboBox.clear() # 清空items
        self.position_dict = info.position_dict
        #self.dictCity = area.dictCity
        #self.dictTown = area.dicTown
        self.City = info.City
       # self.ui_sel.pushButton_ok.hide()
        self.ui_sel.comboBox.addItem(u'请选择')
        self.ui_sel.comboBox_4.addItem(u'请选择')
        self.center() 
         #初始化职位大类
        for (keys, val) in sorted(self.position_dict.items()):
            self.ui_sel.comboBox.addItem(keys, QVariant(val))
            
        for k, v in sorted(self.City.items()):
            self.ui_sel.comboBox_4.addItem(k, v)  # 键、值反转
             
          
    def center(self):  
        '''设置窗口在屏幕居中'''
        screen = QDesktopWidget().screenGeometry()  
        size = self.geometry()  
        self.move((screen.width() - size.width()) / 2,    
        (screen.height() - size.height()) / 2 -40)  
    
    
    @pyqtSlot(int)
    def on_comboBox_activated(self, index):
        # 取省份名称
        # 取省份的键值
        key  = self.ui_sel.comboBox.itemText(index)
        self.ui_sel.comboBox_2.clear() # 清空items
     
        if key:
            #self.lblResult.setText('未选择！')
            self.ui_sel.comboBox_2.addItem('请选择')
            #初始化市
            for k, v in sorted(self.position_dict[key].items()):
                self.ui_sel.comboBox_2.addItem(k, v)  # 键、值反转
                
    
    @pyqtSlot(int)
    def on_comboBox_3_activated(self, index):
        self.ui_sel.pushButton.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 取当前索引
        province_index = self.ui_sel.comboBox.currentIndex()
        city_index = self.ui_sel.comboBox_2.currentIndex()
   
        # 取当前职位名称
        position_b_type = self.ui_sel.comboBox.itemText(province_index)
        position_s_type = self.ui_sel.comboBox_2.itemText(city_index)
        city_ind= self.ui_sel.comboBox_4.currentIndex()
        city = self.ui_sel.comboBox_4.itemText(city_ind)
       
        page  = self.ui_sel.spinBox.value()
        self.ui_sel.textEdit.setText("城市：%s    职位类型：%s-%s \n抓取页数：%s"%(city,position_b_type, position_s_type , page))
        spider= spider_58.SpiderTc(page)
        rsdata = spider.spiderTc(city, position_b_type,  position_s_type)
        if rsdata:
            horizontalHeader = ["公司名称","职位地址","职位名称","职位所在页",'职位总数', u'职位总页数', "抓取时间"]
            self.ui_sel.tableWidget.setColumnCount(7)
            self.ui_sel.tableWidget.setRowCount(len(rsdata))
            self.ui_sel.tableWidget.setHorizontalHeaderLabels(horizontalHeader)
            self.ui_sel.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
            for i, data in enumerate(rsdata):
                for j in range(7):
                    self.ui_sel.tableWidget.setItem(i,j,QTableWidgetItem(str(data[horizontalHeader[j]])))
        else:
            self.ui_sel.textEdit.clear()
            self.ui_sel.textEdit.setText("抓取完成：\n城市：%s 职位类型：%s-%s \n前%s页:无数据"%(city,position_b_type, position_s_type , page))



 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = combosel()
    dlg.show()
    sys.exit(app.exec_())
