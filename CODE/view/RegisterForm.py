#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class RegisterForm(BaseHandler):
    def get(self):
        self.render('register.html',)