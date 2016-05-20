#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#import re
from modelRoot import *
from dbControl import *

class registerController(object):
    def __init__(self, account, name, password):
        self.__name = name
        self.__account = account
        self.__password = password

    def __checkAccountOnly(self):
    	db = dbControl()
        result = db.getUserByAccount(self.__account)
        if len(result) == 0:
            return True
        return False

    def __checkNameOnly(self):
    	db = dbControl()
        result = db.getUserByName(self.__name)
        if len(result) == 0:
            return True
        return False

    def __insertUser(self):
        user = User(self.__account, self.__name, self.__password)
        user.creatUser()

    def getUserByName(self, name):
    	db = dbControl()
    	result = db.getUserByName(name)
    	user = User(result[0][1], result[0][2], result[0][3])
        return user

    def getUserByAccount(self, account):
    	db = dbControl()
        result = db.getUserByAccount(account)
    	user = User(result[0][1], result[0][2], result[0][3])
        return user

    def register(self):
        self.__insertUser()

    def check(self):
        '''
        #check account
        if len(self.__account) < 6 || len(self.__account) > 15:
            return 'account\'s length should be between 6 and 15'

        regex1 = re.compile(u'[a-zA-Z0-9]')
        for :
            return 'account should be consist of number or letter'

        #check password
        if len(self.__password) < 6 || len(self.__password) > 16:
            return 'password\'s length should be between 6 and 16'

        #check name
        if len(self.__name) < 1 || len(self.__name) > 8:
            return 'name\'s length should be between 1 and 8'

        regex2 = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5]')
        self.__name = unicode(self.__name, "utf8")
        for s in self.__name:
            if !regex2.match(s):
                return 'name should be consist of number, letter or Chinese'
        '''
        if self.__checkAccountOnly() != True:
            print self.__account + ' already exists!'
            return False
        if self.__checkNameOnly() != True:
            print self.__name + ' already exists!'
            return False
        return True
