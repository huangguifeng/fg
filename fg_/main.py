#conding=GBK
from Ui_main import Ui_MainWindow
import  sys
from  PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import pyqtSlot
from  PyQt5.QtGui import QIcon
import info  # 58同城信息
import zlinfo
import gjinfo
import  zhinfo
import qcinfo
import spider_58
import  spider_zl
import spdier_gj
import spider_qiancheng
import spider_chinahr
from Ui_about import  Ui_Form
from Ui_help import  Ui_Help
from Ui_company import Ui_Form as Ui_Company
from Ui_insert import Ui_insert
from Ui_delete import  Ui_delete_2
from Ui_update import Ui_update
from my_connect_sql import  Mysqlite

class MainWindows(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./logo.jpg'))
        ### 58
        self.comboBox_4.clear() # 清空items
        self.position_dict = info.position_dict
        #self.dictCity = area.dictCity
        #self.dictTown = area.dicTown
        self.City = info.City
       # self.ui_sel.pushButton_ok.hide()
        self.comboBox_4.addItem(u'请选择')
        self.comboBox.addItem(u'请选择')
        self.center() 
         #初始化职位大类
        for (keys, val) in sorted(self.position_dict.items()):
            self.comboBox.addItem(keys, QVariant(val))
         #初始化城市   
        for k, v in sorted(self.City.items()):
            self.comboBox_4.addItem(k, v)  # 键、值反转
        ### 智联
        self.comboBox_9.addItem(u'请选择')
        self.comboBox_7.addItem(u'请选择')
        for k, v in sorted(self.City.items()):
            self.comboBox_9.addItem(k, v)  # 键、值反转
       #初始化职位大类
        for (keys, val) in sorted(zlinfo.position.items()):
            self.comboBox_7.addItem(keys, QVariant(val))
         # 赶集
        self.comboBox_12.addItem(u'请选择')
        self.comboBox_11.addItem(u'请选择')
        
        for k, v in sorted(gjinfo.CITY.items()):
            self.comboBox_12.addItem(k, v)  # 键、值反转        
        for k, v in sorted(gjinfo.POSITION.items()):
            self.comboBox_11.addItem(k, v)  # 键、值反转              
        
        ####中华
        self.comboBox_15.addItem(u'请选择')
        self.comboBox_13.addItem(u'请选择')
        
        for k, v in sorted(zhinfo.CITY.items()):
            self.comboBox_15.addItem(k, v)  # 键、值反转        
        for k, v in sorted(zhinfo.POSITION.items()):
            self.comboBox_13.addItem(k, v)  # 键、值反转               
        ####前程
        self.comboBox_22.addItem(u'请选择')
        self.comboBox_20.addItem(u'请选择')
        
        for k, v in sorted(qcinfo.CITY.items()):
            self.comboBox_22.addItem(k, v)  # 键、值反转        
        for k, v in sorted(qcinfo.POSITION.items()):
            self.comboBox_20.addItem(k, v)  # 键、值反转                     
        
    def center(self):  
        '''设置窗口在屏幕居中'''
        screen = QDesktopWidget().screenGeometry()  
        size = self.geometry()  
        self.move((screen.width() - size.width()) / 2,    
        (screen.height() - size.height()) / 2 -40)  
    
    ##58
    @pyqtSlot(int)
    def on_comboBox_activated(self, index):

        # 取职位大类的键值
        key  = self.comboBox.itemText(index)
        self.comboBox_2.clear() # 清空items
     
        if key:
            self.comboBox_2.addItem('请选择')
            for k, v in sorted(self.position_dict[key].items()):
                self.comboBox_2.addItem(k, v)  # 键、值反转
    ##智联
    @pyqtSlot(int)
    def on_comboBox_7_activated(self, index):
        key  = self.comboBox_7.itemText(index)
        self.comboBox_8.clear() # 清空items
 
        if key:
            self.comboBox_8.addItem('请选择')
        for k, v in sorted(zlinfo.position[key].items()):
            if k=='id':
                continue
            self.comboBox_8.addItem(k, v)  # 键、值反转
    ## 赶集
    @pyqtSlot(int)
    def on_comboBox_11_activated(self, index):
        key  = self.comboBox_11.itemText(index)
        self.comboBox_10.clear() # 清空items
 
        if key:
            self.comboBox_10.addItem('请选择')
        for k, v in sorted(gjinfo.POSITION[key].items()):
            if k=='id':
                continue
            self.comboBox_10.addItem(k, v)  # 键、值反转
    #中华
    @pyqtSlot(int)
    def on_comboBox_13_activated(self, index):

        # 取职位大类的键值
        key  = self.comboBox_13.itemText(index)
        self.comboBox_14.clear() # 清空items
     
        if key:
            self.comboBox_14.addItem('请选择')
            for k, v in sorted(zhinfo.POSITION[key].items()):
                self.comboBox_14.addItem(k, v)  # 键、值反转
    #前程
    @pyqtSlot(int)
    def on_comboBox_20_activated(self, index):

        # 取职位大类的键值
        key  = self.comboBox_20.itemText(index)
        self.comboBox_21.clear() # 清空items
     
        if key:
            self.comboBox_21.addItem('请选择')
            for k, v in sorted(qcinfo.POSITION[key].items()):
                self.comboBox_21.addItem(k, v)  # 键、值反转      
                
    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 58
        # 取当前索引
        province_index = self.comboBox.currentIndex()
        city_index = self.comboBox_2.currentIndex()
   
        # 取当前职位名称
        position_b_type = self.comboBox.itemText(province_index)
        position_s_type = self.comboBox_2.itemText(city_index)
        city_ind= self.comboBox_4.currentIndex()
        city = self.comboBox_4.itemText(city_ind)
        peer = self.lineEdit.text()
        page  = self.spinBox.value()
        self.textEdit.setText("城市：%s    职位类型：%s-%s \n抓取页数：%s "%(city,position_b_type, position_s_type , page))
        #print(city, position_b_type,position_b_type )
        a, b= mysqlite.select_all(1)
        spider= spider_58.SpiderTc(page, peer, b)
        if city=='请选择' or position_b_type=='请选择' or position_s_type=='请选择':
            return
        rsdata, num = spider.spiderTc(city, position_b_type,  position_s_type)
        if rsdata:
            horizontalHeader = ["公司名称","职位名称","职位地址","职位所在页",'职位总数', u'职位总页数', "抓取时间"]
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setRowCount(len(rsdata))
            self.tableWidget.setHorizontalHeaderLabels(horizontalHeader)
            self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
            self.lineEdit_2.setText(str(num))
            self.lineEdit_3.setText(str(len(rsdata)))
            self.lineEdit_4.setText('%.2f%%'%(len(rsdata)/num*100))
            for i, data in enumerate(rsdata):
                for j in range(7):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(data[horizontalHeader[j]])))
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setColumnWidth(0, 200)
        else:
            self.textEdit.clear()
            self.tableWidget.clearContents ()    
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.textEdit.setText("抓取完成：\n城市：%s 职位类型：%s-%s \n前%s页:无数据"%(city,position_b_type, position_s_type , page))
        
    @pyqtSlot()
    def on_pushButton_7_clicked(self):    
        #智联
        btitle_index = self.comboBox_7.currentIndex()
        stitle_index = self.comboBox_8.currentIndex()
        # 取当前职位名称
        position_b_type = self.comboBox_7.itemText(btitle_index)
        position_s_type = self.comboBox_8.itemText(stitle_index)
        city_ind= self.comboBox_9.currentIndex()
        city = self.comboBox_9.itemText(city_ind)
        peer = self.lineEdit_9.text()
        page  = self.spinBox_3.value()
        self.textEdit_3.setText("城市：%s    职位类型：%s-%s \n抓取页数：%s %s"%(city,position_b_type, position_s_type , page, peer))
        if city=='请选择' or position_b_type=='请选择' or position_s_type=='请选择':
            return  
        a, b= mysqlite.select_all(2)  
        spider =  spider_zl.SpiderZl(b, peer=peer)
        rsdata, num = spider.run(city,position_b_type, position_s_type , page,)
        if rsdata:
            horizontalHeader = ["职位名称","公司名称","工作地点","职位所在页", "抓取时间"]
            self.tableWidget_3.setColumnCount(len(horizontalHeader))
            self.tableWidget_3.setRowCount(len(rsdata))
            self.tableWidget_3.setHorizontalHeaderLabels(horizontalHeader)
            self.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)
            self.lineEdit_10.setText(str(num))
            self.lineEdit_11.setText(str(len(rsdata)))
            self.lineEdit_12.setText('%.2f%%'%(len(rsdata)/num*100))
            for i, data in enumerate(rsdata):
                for j in range(len(horizontalHeader)):
                    self.tableWidget_3.setItem(i,j,QTableWidgetItem(str(data[horizontalHeader[j]])))
                    self.tableWidget_3.setColumnWidth(1, 250)
                    self.tableWidget_3.setColumnWidth(0, 200)     
        else:
            self.textEdit_3.clear()
            self.textEdit_3.setText("抓取完成：\n城市：%s 职位类型：%s-%s \n前%s页:无数据"%(city,position_b_type, position_s_type , page))
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()   
            self.tableWidget_3.clearContents ()     
    @pyqtSlot()
    def on_pushButton_8_clicked(self):    
        #赶集
        btitle_index = self.comboBox_11.currentIndex()
        stitle_index = self.comboBox_10.currentIndex()
        # 取当前职位名称
        position_b_type = self.comboBox_11.itemText(btitle_index)
        position_s_type = self.comboBox_10.itemText(stitle_index)
        city_ind= self.comboBox_12.currentIndex()
        city = self.comboBox_12.itemText(city_ind)
        peer = self.lineEdit_13.text()
        page  = self.spinBox_4.value()
        self.textEdit_4.setText("城市：%s    职位类型：%s-%s \n抓取页数：%s %s"%(city,position_b_type, position_s_type , page, peer))
        if city=='请选择' or position_b_type=='请选择' or position_s_type=='请选择':
            return        
        a, b= mysqlite.select_all(3)    
        spider = spdier_gj.GanJi(city,  page,position_b_type, position_s_type, peer, b)
        spider.spider()
        rsdata, num = spider.run()
        if rsdata:
            horizontalHeader = ["职位名称","公司名称","发布地址","发布时间", "职位所在页"]
            self.tableWidget_4.setColumnCount(len(horizontalHeader))
            self.tableWidget_4.setRowCount(len(rsdata))
            self.tableWidget_4.setHorizontalHeaderLabels(horizontalHeader)
            self.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)
            self.lineEdit_14.setText(str(num))
            self.lineEdit_15.setText(str(len(rsdata)))
            self.lineEdit_16.setText('%.2f%%'%(len(rsdata)/num*100))
            for i, data in enumerate(rsdata):
                for j in range(len(horizontalHeader)):
                    self.tableWidget_4.setItem(i,j,QTableWidgetItem(str(data[horizontalHeader[j]])))
                    self.tableWidget_4.setColumnWidth(1, 250)
                    self.tableWidget_4.setColumnWidth(0, 200)     
        else:
            self.textEdit_4.clear()
            self.textEdit_4.setText("抓取完成：\n城市：%s 职位类型：%s-%s \n前%s页:无数据"%(city,position_b_type, position_s_type , page))
            self.lineEdit_14.clear()
            self.lineEdit_15.clear()
            self.lineEdit_16.clear()   
            self.tableWidget_4.clearContents ()  
    @pyqtSlot()
    def on_pushButton_9_clicked(self):    
        # 中华
        btitle_index = self.comboBox_13.currentIndex()
        stitle_index = self.comboBox_14.currentIndex()
        # 取当前职位名称
        position_b_type = self.comboBox_13.itemText(btitle_index)
        position_s_type = self.comboBox_14.itemText(stitle_index)
        city_ind= self.comboBox_15.currentIndex()
        city = self.comboBox_15.itemText(city_ind)
        peer = self.lineEdit_20.text()
        page  = self.spinBox_5.value()
        self.textEdit_5.setText("城市：%s    职位类型：%s-%s \n抓取页数：%s %s"%(city,position_b_type, position_s_type , page, peer))
        if city=='请选择' or position_b_type=='请选择' or position_s_type=='请选择':
            return   
        a, b= mysqlite.select_all(4)       
        spdier = spider_chinahr.Chinahr( city, page, position_b_type, position_s_type, peer, b)
        spdier.spider()
        rsdata, num = spdier.data()
        if rsdata:
            horizontalHeader = ["职位名称","公司名称","发布地址及要求","发布时间", "职位所在页"]
            self.tableWidget_5.setColumnCount(len(horizontalHeader))
            self.tableWidget_5.setRowCount(len(rsdata))
            self.tableWidget_5.setHorizontalHeaderLabels(horizontalHeader)
            self.tableWidget_5.setEditTriggers(QTableWidget.NoEditTriggers)
            self.lineEdit_17.setText(str(num))
            self.lineEdit_18.setText(str(len(rsdata)))
            self.lineEdit_19.setText('%.2f%%'%(len(rsdata)/num*100))
            for i, data in enumerate(rsdata):
                for j in range(len(horizontalHeader)):
                    self.tableWidget_5.setItem(i,j,QTableWidgetItem(str(data[horizontalHeader[j]])))
                    self.tableWidget_5.setColumnWidth(1, 250)
                    self.tableWidget_5.setColumnWidth(0, 200)                    
                   
        else:
            self.textEdit_5.clear()
            self.textEdit_5.setText("抓取完成：\n城市：%s 职位类型：%s-%s \n前%s页:无数据"%(city,position_b_type, position_s_type , page))
            self.lineEdit_17.clear()
            self.lineEdit_18.clear()
            self.lineEdit_19.clear()   
            self.tableWidget_5.clearContents ()
    @pyqtSlot()
    def on_pushButton_12_clicked(self):    
        # 前程
        btitle_index = self.comboBox_20.currentIndex()
        stitle_index = self.comboBox_21.currentIndex()
        # 取当前职位名称
        position_b_type = self.comboBox_20.itemText(btitle_index)
        position_s_type = self.comboBox_21.itemText(stitle_index)
        city_ind= self.comboBox_22.currentIndex()
        city = self.comboBox_22.itemText(city_ind)
        peer = self.lineEdit_30.text()
        page  = self.spinBox_6.value()
        print(position_b_type, position_b_type)
        self.textEdit_6.setText("城市：%s    职位类型：%s-%s \n抓取页数：%s %s"%(city,position_b_type, position_s_type , page, peer))
        if city=='请选择' or position_b_type=='请选择' or position_s_type=='请选择':
            return   
        a, b= mysqlite.select_all(5)       
        spdier = spider_qiancheng.Qiancheng( city, page, position_b_type, position_s_type, peer, b)
        spdier.spider()
        rsdata, num = spdier.data()
        if rsdata:
            horizontalHeader = ["职位名称","公司名称","工作地点","发布时间", "职位所在页"]
            self.tableWidget_6.setColumnCount(len(horizontalHeader))
            self.tableWidget_6.setRowCount(len(rsdata))
            self.tableWidget_6.setHorizontalHeaderLabels(horizontalHeader)
            self.tableWidget_6.setEditTriggers(QTableWidget.NoEditTriggers)
            
            self.lineEdit_27.setText(str(num))
            self.lineEdit_28.setText(str(len(rsdata)))
            self.lineEdit_29.setText('%.2f%%'%(len(rsdata)/num*100))
            for i, data in enumerate(rsdata):
                for j in range(len(horizontalHeader)):
                    self.tableWidget_6.setItem(i,j,QTableWidgetItem(str(data[horizontalHeader[j]])))
                    self.tableWidget_6.setColumnWidth(1, 250)
                    self.tableWidget_6.setColumnWidth(0, 200)
              
        else:
            self.textEdit_6.clear()
            self.textEdit_6.setText("抓取完成：\n城市：%s 职位类型：%s-%s \n前%s页:无数据"%(city,position_b_type, position_s_type , page))
            self.lineEdit_27.clear()
            self.lineEdit_28.clear()
            self.lineEdit_29.clear()   
            self.tableWidget_6.clearContents ()

class AboutWindow(QWidget, Ui_Form):
    # 关于
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        
class HelpWindow(QWidget,Ui_Help):
    # 帮助
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        
class InsertWindow(QWidget, Ui_insert):
    # 新增公司窗口
    def __init__(self, cid):
        super().__init__()
        self.setupUi(self)
        self.cid = cid
        self.pushButton_2.clicked.connect(self.close)
        
    def insert(self, cid):
        name = self.lineEdit.text() # 获取到公司名称
        if not name:
            return
        mysqlite.insert(cid, name)
        self.close()

    def close(self):
        super( ).close()
        CompanyWindow(self.cid).show() # 点取消窗口重新打开

        
class DeleteWindow(QWidget, Ui_delete_2):
    # 删除公司窗口
    def __init__(self, cid):
        super().__init__()
        self.setupUi(self)
        self.cid = cid
        self.pushButton_4.clicked.connect(self.close) 
    def delete(self, cid, id):
        #todo : 删除
        mysqlite.delete(cid, id)
        self.close()

    def close(self):
        super( ).close()
        CompanyWindow(self.cid ).show() # 点取消窗口重新打开
    
class UpdateWindow(QWidget, Ui_update):
        # 更新公司窗口
    def __init__(self, cid):
        super().__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.close)
        self.cid = cid
    def update(self,  id):
        name = self.lineEdit.text()
        if not name:
            return
        mysqlite.update(self.cid, id, name)
        self.close()
        
    def close(self):
        super( ).close()
        CompanyWindow(self.cid ).show() # 点取消窗口重新打开        
        
class CompanyWindow(QWidget,Ui_Company):
   
        def __init__(self, cid):
            super().__init__()
            self.setupUi(self)
            self.cid = cid   #标记是修改那个招聘网站
            self.insert_win = InsertWindow(cid)
            self.delete_win = DeleteWindow(cid)
            self.update_win = UpdateWindow(cid)
            mysqlite.client(self.cid)
            self.companyTable()
            
        def  companyTable(self):
            """品牌公司修改表单"""
            horizontalHeader = ["id","公司名称", '操作']
            # 获取数据
            rsdata, rsdata1 =   mysqlite.select_all(self.cid)
            # 生成表格
            self.tableWidget.setColumnCount(len(horizontalHeader))
            self.tableWidget.setRowCount(len(rsdata))
            self.tableWidget.setHorizontalHeaderLabels(horizontalHeader)
            self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
            for i, data in enumerate(rsdata):
                for j in range(len(horizontalHeader) +1):
                    if j < len(data):
                        self.tableWidget.setItem(i,j,QTableWidgetItem(str(data[horizontalHeader[j]])))
                        self.tableWidget.setColumnWidth(0, 100) 
                        self.tableWidget.setColumnWidth(1, 300)
                        self.tableWidget.setColumnWidth(2, 330)
                        
                    if  j == len(data):
                        self.tableWidget.setCellWidget(i, j,self.buttonForRow(str(data["id"])))
                        
                    
        
        def updateTable(self, id):
            if not id:
                return
            id, name = mysqlite.select(self.cid, id)
            self.update_win.lineEdit_2.setText(name)
            self.update_win.show()
            self.update_win.pushButton_3.clicked.connect(lambda:self.update_win.update(id))
            self.close()
        def deleteTable(self, id):
            if not id:
                return
            id, name = mysqlite.select(self.cid, id)
            self.delete_win.lineEdit.setText(name)
            self.delete_win.show()
            self.delete_win.pushButton_3.clicked.connect(lambda:self.delete_win.delete(self.cid, id))
            self.close()

        def insertTable(self, id):
            self.insert_win.show()
            self.insert_win.pushButton.clicked.connect(lambda:self.insert_win.insert(self.cid))
            self.close()
   
        def buttonForRow(self, id):
            """ 表格里面的按钮 """
            widget=QWidget()
          # 修改
            updateBtn = QPushButton('修改')
            updateBtn.setStyleSheet(''' text-align : center;
                                            background-color : NavajoWhite;
                                            height : 30px;
                                            border-style: outset;
                                           font : 13px  ''') 
            updateBtn.clicked.connect(lambda:self.updateTable(id))

 
         # 删除
            deleteBtn = QPushButton('删除')
            deleteBtn.setStyleSheet(''' text-align : center;
                                     background-color : LightCoral;
                                     height : 30px;
                                     border-style: outset;
                                     font : 13px; ''')
            deleteBtn.clicked.connect(lambda: self.deleteTable(id))
 
            # 新增
            insertertBtn = QPushButton('新增')
            insertertBtn.setStyleSheet(''' text-align : center;
                                            background-color : DarkSeaGreen;
                                            height : 30px;
                                            border-style: outset;
                                           font : 13px  ''') 
            insertertBtn.clicked.connect(lambda:self.insertTable(id))
 
            hLayout = QHBoxLayout()
            hLayout.addWidget(updateBtn)
            hLayout.addWidget(deleteBtn)
            hLayout.addWidget(insertertBtn)
            hLayout.setContentsMargins(5,2,5,2)
            widget.setLayout(hLayout)
            return widget
            
def show_company(id):
    cp = CompanyWindow(id)
    cp.show()

def show_58tc():
    show_company(1)
def show_zhilian():
    show_company(2)
def show_ganji():
    show_company(3)
def show_zhonghua():
    show_company(4)
def show_qiancheng():
    show_company(5)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = MainWindows()
    dlg.show()
    # 关于窗口
    mysqlite = Mysqlite()  # 创建数据库连接
    ab = AboutWindow()
    dlg.actionabout.triggered.connect(ab.show)
    # 帮助窗口
    hp = HelpWindow()
    dlg.action.triggered.connect(hp.show)
    # 增加公司窗口
    dlg.action58.triggered.connect(show_58tc)
    dlg.actiond.triggered.connect(show_zhilian)
    dlg.actionga.triggered.connect(show_ganji)
    dlg.actionz.triggered.connect(show_zhonghua)
    dlg.actionqc.triggered.connect(show_qiancheng)
  

    sys.exit(app.exec_())

