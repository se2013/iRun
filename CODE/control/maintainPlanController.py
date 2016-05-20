#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from modelRoot import *
from dbControl import *

class maintainPlanController(object):
    def __init__(self):
    	pass

    def getAllPlan(self):
    	db = dbControl()
    	result = db.getAllPlan()
    	return result

    def __deleteCollectPlanByPlanId(self, planid):
    	db = dbControl()
    	db.deleteCollectPlanByPlanId(planid)

    def __deleteJoinPlanByPlanId(self, planid):
    	db = dbControl()
    	result = db.deleteJoinPlanByPlanId(planid)

    def __deleteCreatePlanByPlanId(self, planid):
    	db = dbControl()
    	result = db.deleteCreatePlanByPlanId(planid)

    def deletePlan(self, planid):
    	self.__deleteCollectPlanByPlanId(planid)
    	self.__deleteJoinPlanByPlanId(planid)
    	self.__deleteCreatePlanByPlanId(planid)
