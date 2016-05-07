#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from BaseHandler import *

class MaintainUserForm(BaseHandler):
    def get(self):
        self.render('maintainuser.html',)