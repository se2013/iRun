#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from dbControl import *

class User(object):
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
            result = db.getUserByAccount(self.__account)
            self.__userid = result[0][0]
            self.__name = result[0][2]

    def getAccount(self):
        return self.__account

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password
        db = dbControl()
        db.updateUserPasswordById(self.__userid, password)

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
        db = dbControl()
        result = db.updateUserNameById(self.__userid, name)

    def getId(self):
        return self.__userid

    def creatUser(self):
        db = dbControl()
        db.addUser(self.__account, self.__name, self.__password)

'''
    def setAccount(self, account):
        self.__account = account
        db = dbControl()
        db.updateUserAccountById(self.__userid, account)
'''

'''
    def setId(self, userid):
        self.userid = userid
        db = dbControl()
        result = db.updateUserIdById(self.__userid)
'''
