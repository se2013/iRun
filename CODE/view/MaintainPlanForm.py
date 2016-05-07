#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from BaseHandler import *

class MaintainPlanForm(BaseHandler):
    def get(self):
        self.render('maintainplan.html',)