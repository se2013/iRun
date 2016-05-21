#!/usr/bin/env python 
# -*- coding: utf-8 -*-


from controllerRoot import *

class LoginForm(BaseHandler):
    def get(self, mode):
        #如果登录，则自动跳转到用户or管理员页面
        if super(LoginForm, self).have_login():
            return
        
        if not mode:
            self.render('login.html', mode='user', account_tip='', password_tip='')
        else:
            self.render('login.html', mode='admin', account_tip='', password_tip='')

    def post(self, mode):
        account = self.get_argument('account', '')
        password = self.get_argument('password', '')

        login_controller = loginController(account,password)
        if not mode:
            #user
            tip = login_controller.checkUser()
            if tip[0] and tip[1]:
                self.render('login.html',mode='user', account_tip=tip[0], password_tip=tip[1])
                return
            else:
                user = login_controller.getUserByAccount(account)
                self.set_secure_cookie("account", account)
                self.set_cookie("name", user.getName())
                print account
                self.redirect('/manage/aboutMe')
        else:
            #admin
            tip = login_controller.checkAdmin()
            if tip[0] and tip[1]:
                self.render('login.html',mode='admin', account_tip=tip[0], password_tip=tip[1])
                return
            else:
                admin = login_controller.getAdminByAccount(account)
                self.set_secure_cookie("account", account)
                self.set_cookie("name", admin.getName())
                self.redirect('/maintainuser')



    