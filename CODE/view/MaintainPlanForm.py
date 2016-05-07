#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from controllerRoot import *

class MaintainPlanForm(BaseHandler):
    def get(self):
        self.render('maintainplan.html',)