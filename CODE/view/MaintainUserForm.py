#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class MaintainUserForm(BaseHandler):
    def get(self):
        if not super(MaintainUserForm, self).is_admin():
        	return

        name = self.get_cookie('name')
        account = self.get_secure_cookie("account")

        maintainUser_controller = maintainUserController()
        all_user = maintainUser_controller.getAllUser()

        self.render('maintainuser.html', name=name, account=account, all_user=all_user)

    def post(self):
    	user_account = self.get_argument('user_account', '')
    	print user_account
    	maintainUser_controller = maintainUserController()
    	maintainUser_controller.deleteUser(user_account)
