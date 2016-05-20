#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from modelRoot import *
from dbControl import *
from User import *

class AboutMeController(object):
    def __init__(self, account, password):
        self.__user = User(account, password)

    def getCreatePlanByAboutMe(self):
    	db = dbControl()
        result = db.getCreatePlanByUserAccount(self.__user.getAccount())
        return result

    def getCollectPlanByAboutMe(self):
    	db = dbControl()
        result = db.getCollectPlanByUserAccount(self.__user.getAccount())
        return result

    def getJoinPlanByAboutMe(self):
    	db = dbControl()
    	result = db.getJoinPlanByUserAccount(self.__user.getAccount())
    	return result
