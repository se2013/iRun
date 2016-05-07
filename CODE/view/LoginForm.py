#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from BaseHandler import *

class LoginForm(BaseHandler):
    def get(self):
        self.render('login.html',)

