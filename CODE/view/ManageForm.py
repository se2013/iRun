#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class ManageForm(BaseHandler):
    def get(self, mode):
        # mode分为aboutme和otherplan
        # name = self.get_cookie('name')
        # account = self.get_secure_cookie("account")
        # aboutMe_controller = aboutMeController(account, '')

        # my_plan = aboutMe_controller.getCreatePlanByAboutMe()
        # collect_plan = aboutMe_controller.getCollectPlanByAboutMe()
        self.render('manage.html', name='', my_plan='', collect_plan='')
        # self.render('manage.html', name=name, my_plan=my_plan, collect_plan=collect_plan)