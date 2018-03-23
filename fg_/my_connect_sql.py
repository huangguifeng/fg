from PyQt5 import QtSql  
from PyQt5.QtSql import QSqlQuery
import time
class Mysqlite():
    
    def __init__(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')  
        self.database.setDatabaseName('./data.db')
        self.database.open()  
        self.q=QSqlQuery()
    def client(self, cid):
        #创建QsqlQuery对象，用于执行sql语句
        if cid == 1: 
            self.q.exec_("create table if not exists tc (id int unsigned auto_increment primary key not null,name varchar(50))") 
        if cid == 2: 
            self.q.exec_("create table if not exists zhilian (id int unsigned auto_increment primary key not null,name varchar(50))") 
        if cid == 3: 
            self.q.exec_("create table if not exists ganji (id int unsigned auto_increment primary key not null,name varchar(50))") 
        if cid == 4: 
            self.q.exec_("create table if not exists zhonghua (id int unsigned auto_increment primary key not null,name varchar(50))") 
        self.q.exec_("commit") 
        return self.q
    def select(self, cid, id):    
        """查询单个"""
        if cid==1:
            return self.__to_select('tc', id)
        if cid==2:
            return self.__to_select('zhilian', id)
        if cid==3:
            return self.__to_select('ganji', id)
        if cid==4:
            return self.__to_select('zhonghua', id)  
            
    def __to_select(self, db_name, id):
        self.q.exec('select * from %s where id=%s'%(db_name, id))  
        f1= self.q.record().indexOf('id') 
        f2=self.q.record().indexOf('name')
        while self.q.next(): 
            id = self.q.value(f1)  
            name = self.q.value(f2)
            return id, name
            
    def select_all(self, cid):
        """根据不同的cid 查询不同招聘网站的品牌公司
        将查询数据封装成列表，元素为字典，返回
        """
        if cid==1:
            return self.__to_list('tc')
        if cid==2:
            return self.__to_list('zhilian')
        if cid==3:
            return self.__to_list('ganji')
        if cid==4:
            return self.__to_list('zhonghua')       
            
    def __to_list(self, args):
        self.q.exec('select * from %s'%args)  
        f1= self.q.record().indexOf('id') 
        f2=self.q.record().indexOf('name')
        data = []
        data1 = []
        while self.q.next(): 
            tmp = {} 
            id = self.q.value(f1)  
            name = self.q.value(f2)
            tmp["id"] = id
            tmp["公司名称"] = name
            data1.append(name)
            data.append(tmp)
        if not data:  
            data = [{"id":"", "公司名称":""}]
        return data, data1
        
    def  insert(self, cid, name) :
        if cid==1:
            return self.__to_insert('tc', name)
        if cid==2:
            return self.__to_insert('zhilian', name)
        if cid==3:
            return self.__to_insert('ganji', name)
        if cid==4:
            return self.__to_insert('zhonghua', name) 
            
    def __to_insert(self, db_name, name):
        id = int(time.time()*1000)
        self.q.exec('insert into %s values (%s,"%s")'%( db_name,id, name))
        self.q.exec_("commit")
    
    def  delete(self, cid, name) :
        if cid==1:
            return self.__to_delete('tc', name)
        if cid==2:
            return self.__to_delete('zhilian', name)
        if cid==3:
            return self.__to_delete('ganji', name)
        if cid==4:
            return self.__to_delete('zhonghua', name) 
            
    def __to_delete(self, db_name, id):
        self.q.exec('delete from %s where id=%s'%( db_name,id))
        self.q.exec_("commit")
        
    def  update(self, cid, id, name) :
        if cid==1:
            return self.__to_update('tc', id, name)
        if cid==2:
            return self.__to_update('zhilian', id, name)
        if cid==3:
            return self.__to_update('ganji', id, name)
        if cid==4:
            return self.__to_update('zhonghua', id, name) 
            
    def __to_update(self, db_name, id, name):
        self.q.exec('update %s set name="%s" where id=%s'%(db_name, name, id))
        self.q.exec_("commit")
