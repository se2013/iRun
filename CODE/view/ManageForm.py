#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class ManageForm(BaseHandler):
    def get(self, mode):
        # mode分为aboutme和otherplan
        self.render('manage.html',)