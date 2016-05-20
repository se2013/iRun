#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class PublishForm(BaseHandler):
    def get(self):
    	pass

    def post(self):
        time = self.get_argument('time', '')
        place = self.get_argument('place', '')
        contact_way = self.get_argument('contact_way', '')
        tips = self.get_argument('tips', '')

        self.get_secure_cookie("account")


