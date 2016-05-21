#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
    	return self.get_secure_cookie("account")

    def have_login(self):
    	account = self.get_secure_cookie("account")
    	mode = self.get_secure_cookie("mode")
        if not account and not mode:
            return False
        elif mode == 'admin':
            self.redirect('/maintainuser')
            return True
        else:
            self.redirect('/manage/aboutMe')
            return True

    def is_user(self):
    	# 未登录->登录页面；管理员登录->跳转到管理员页面
    	account = self.get_secure_cookie("account")
    	mode = self.get_secure_cookie("mode")
    	if not account and not mode:
    		self.redirect('/')
    		return False
    	elif mode == 'admin':
    		self.redirect('/maintainuser')
    		return False
    	else:
    		return True

    def is_admin(self):
    	# 未登录->登录页面；管理员登录->跳转到管理员页面
    	account = self.get_secure_cookie("account")
    	mode = self.get_secure_cookie("mode")
    	print '8' * 30
    	print account
    	print mode
    	if not account:
    		self.redirect('/')
    		return False
    	elif mode != 'admin':
    		self.redirect('/manage/aboutMe')
    		print '8' * 30
    		return False
    	else:
    		return True

    def get(self):
    	self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
