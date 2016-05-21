#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from modelRoot import *
from dbControl import *

class publishController(object):
    def __init__(self, time, location, contact, create_user, publish_time, tips):
        self.__plan = Plan(time, location, contact, create_user, publish_time, tips)

    def insertPlan(self):
        self.__plan.createPlan()

