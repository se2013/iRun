#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class PublishForm(BaseHandler):
    def get(self):
        self.render('manage.html',)