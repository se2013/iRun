#coding=utf-8

from dbControl import *

#admin(id,name,account,password)
class Admin(object):
    def __init__(self, *msg):
        #register:
        if len(msg) == 3:
            self.__account = msg[0]
            self.__name = msg[1]
            self.__password = msg[2]
        #login:
        elif len(msg) == 2:
            self.__account = msg[0]
            self.__password = msg[1]
            db = dbControl()
            admin = db.getAdminByAccount(self.__account)
            self.__adminid = admin[0][0]
            self.__name = admin[0][2]

    def getAccount(self):
        return self.__account

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password
        db = dbControl()
        db.updateAdminPasswordById(self.__adminid, password)
        return True

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
        db = dbControl()
        result = db.updateAdminNameById(self.__adminid, name)
        return result

    def getId(self):
        return self.__adminid

    def creatAdmin(self):
        db = dbControl()
        db.addAdmin(self.__name, self.__account, self.__password)

'''
    def setId(self, adminid):
        self.adminid = adminid
        db = dbControl()
        db.updateAdminIdById(self.__adminid)
'''
'''
    def setAccount(self, account):
        self.__account = account
        db = dbControl()
        db.updateAdminAccountById(self.__adminid, account)
'''
