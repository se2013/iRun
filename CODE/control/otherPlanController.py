#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from modelRoot import *
from dbControl import *

class otherPlanController(object):
    def __init__(self, account, password):
        self.__user = User(account, password)

    def getPlanByOther(self):
    	db = dbControl()
        result = db.getOtherPlanByUserAccount(self.__user.getAccount())
        return result

    def joinPlan(self, planid):
    	db = dbControl()
        db.joinPlan(self.__user.getAccount(), planid)

    def collectPlan(self, planid):
    	db = dbControl()
        result = db.collectPlan(self.__user.getAccount(), planid)
        return result
