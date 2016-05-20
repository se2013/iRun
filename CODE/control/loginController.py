#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from modelRoot import *
from dbControl import *

class loginController(object):
    def __init__(self, account, password):
        self.__account = account
        self.__password = password

    def __checkUserAccount(self):
        db = dbControl()
        result = db.getUserByAccount(self.__account)
        if len(result) == 0:
            return False
        return True

    def __checkUserPassword(self):
        db = dbControl()
        result = db.getUserByAccount(self.__account)
        if result[0][3] != self.__password:
            return False
        return True

    def __checkAdminAccount(self):
        db = dbControl()
        result = db.getAdminByAccount(self.__account)
        if len(result) == 0:
            return False
        return True

    def __checkAdminPassword(self):
        db = dbControl()
        result = db.getAdminByAccount(self.__account)
        if result[0][3] != self.__password:
            return False
        return True

    def getUserByAccount(self, account):
        db = dbControl()
        result = db.getUserByAccount(account)
        user = User(result[0][1], result[0][2], result[0][3])
        return user

    def getAdminByAccount(self, account):
        db = dbControl()
        result = db.getAdminByAccount(account)
        admin = Admin(result[0][1], result[0][2], result[0][3])
        return admin

    def login(self):
        return True

    def checkUser(self):
        tip1 = ''
        tip2 = ''
        if self.__checkUserAccount() != True:
            print 'Account not exists!'
            tip1 = '用户名不存在'
        if self.__checkUserPassword() != True:
            print 'Password is wrong!'
            tip2 = '密码错误'
        return [tip1, tip2]

    def checkAdmin(self):
        tip1 = ''
        tip2 = ''
        if self.__checkAdminAccount() != True:
            print 'Account not exists!'
            tip1 = '用户名不存在'
        if self.__checkAdminPassword() != True:
            print 'Password is wrong!'
            tip2 = '密码错误'
        return [tip1, tip2]
