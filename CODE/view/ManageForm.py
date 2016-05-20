#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class ManageForm(BaseHandler):
    def get(self, mode):
        # mode分为aboutme和otherplan
        if not super(ManageForm, self).is_user():
            return

        name = self.get_cookie('name')
        account = self.get_secure_cookie("account")
        
        if mode == 'aboutMe':
            aboutMe_controller = aboutMeController(account, '')

            my_plan = aboutMe_controller.getCreatePlanByAboutMe()
            collect_plan = aboutMe_controller.getCollectPlanByAboutMe()

            self.render('manage.html', mode=mode, name=name, account=account, my_plan=my_plan, collect_plan=collect_plan, other_plan='')
        else:
            otherPlan_controller = otherPlanController(account, '')

            other_plan = otherPlan_controller.getPlanByOther()
            self.render('manage.html', mode=mode, name=name, account=account, my_plan='', collect_plan='', other_plan=other_plan)

    def post(self, mode):
        account = self.get_argument('account', '')
        plan_id = self.get_argument('plan_id', '')

        otherPlan_controller = otherPlanController(account, '')
        otherPlan_controller.collectPlan(int(plan_id))
        

