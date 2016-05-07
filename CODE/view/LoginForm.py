#!/usr/bin/env python 
# -*- coding: utf-8 -*-


from controllerRoot import *

class LoginForm(BaseHandler):
    def get(self):
    	t = loginController()
    	t.test()
        self.render('login.html',)

