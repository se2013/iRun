#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from BaseHandler import *

class RegisterForm(BaseHandler):
    def get(self):
        self.render('register.html',)