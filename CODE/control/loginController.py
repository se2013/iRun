#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from modelRoot import *
from dbControl import *
from User import *
from Admin import *

class loginController(object):
    def __init__(self, account, password):
        self.__account = account
        self.__password = password

    def __checkAccount(self):
    	db = dbControl()
        result = db.getUserByAccount(self.__account)
        if len(result) == 0:
            return False
        return True

    def __checkPassword(self):
    	db = dbControl()
        result = db.getUserByAccount(self.__account)
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

    def check(self):
        if self.__checkAccount() != True:
            print 'Account not exists!'
            return False
        if self.__checkPassword() != True:
            print 'Password is wrong!'
            return False
        return True
