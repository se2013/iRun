#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from controllerRoot import *

class MaintainPlanForm(BaseHandler):
    def get(self):
        if not super(MaintainPlanForm, self).is_admin():
        	return

        name = self.get_cookie('name')
        account = self.get_secure_cookie("account")

        maintainPlan_controller = maintainPlanController()
        all_plan = sorted(maintainPlan_controller.getAllPlan())
        all_plan.reverse()
        self.render('maintainplan.html', name=name, account=account, all_plan=all_plan)

    def post(self):
    	plan_id = self.get_argument('plan_id', '')
    	print plan_id
    	maintainPlan_controller = maintainPlanController()
    	maintainPlan_controller.deletePlan(int(plan_id))

