#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class RegisterForm(BaseHandler):
    def get(self):
        if super(RegisterForm, self).have_login():
            return
        self.render('register.html',account_tip='', name_tip='', success='')

    def post(self):
    	account = self.get_argument('account', '')
    	password = self.get_argument('password', '')
    	name = self.get_argument('name', '')

    	register_controller = registerController(account, password, name)
    	tip = register_controller.check()
    	print tip
    	if tip[0] and tip[1]:
    		self.render('register.html',account_tip=tip[0], name_tip=tip[1], success='')
    		return
    	else:
    		register_controller.register()
    		self.render('register.html',account_tip='', name_tip='', success='success')


