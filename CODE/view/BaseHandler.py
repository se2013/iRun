#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
    	return self.get_secure_cookie("account")

    def have_login(self):
    	account = self.get_secure_cookie("account")
        if not account:
            return False
        elif account == 'admin123':
            self.redirect('/maintainuser')
            return True
        else:
            self.redirect('/manage/aboutMe')
            return True

    def is_user(self):
    	# 未登录->登录页面；管理员登录->跳转到管理员页面
    	account = self.get_secure_cookie("account")
    	if not account:
    		self.redirect('/')
    		return False
    	elif account == 'admin123':
    		self.redirect('/maintainuser')
    		return False
    	else:
    		return True
