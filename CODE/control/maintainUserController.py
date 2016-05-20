#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from modelRoot import *
from dbControl import *

class maintainUserController(object):
    def __init__(self):
    	pass

    def getAllUser(self):
    	db = dbControl()
    	result = db.getAllUser()
    	return result

    def __deleteCreatePlanByAccount(self, account):
    	db = dbControl()
    	db.deleteCreatePlanByUserAccount(account)

    def __deleteJoinPlanByAccount(self, account):
    	db = dbControl()
    	db.deleteJoinPlanByUserAccount(account)

    def __deleteCollectPlanByAccount(self, account):
    	db = dbControl()
    	db.deleteCollectPlanByUserAccount(account)

    def __deleteUserByAccount(self, account):
    	db = dbControl()
    	db.delUser(account)

    def deleteUser(self, account):
    	self.__deleteCreatePlanByAccount(account)
    	self.__deleteJoinPlanByAccount(account)
    	self.__deleteCollectPlanByAccount(account)
    	self.__deleteUserByAccount(account)
