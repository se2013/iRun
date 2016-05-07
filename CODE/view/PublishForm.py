#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from BaseHandler import *

class PublishForm(BaseHandler):
    def get(self):
        self.render('manage.html',)