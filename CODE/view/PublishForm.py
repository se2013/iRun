#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from controllerRoot import *

class PublishForm(BaseHandler):
    def get(self):
        # 未登录->登录页面；管理员登录->跳转到管理员页面
        if not super(ManageForm, self).is_user():
            return

    def post(self):
        meet_time = self.get_argument('time', '')
        place = self.get_argument('place', '')
        contact_way = self.get_argument('contact_way', '')
        tips = self.get_argument('tips', '')
        account = self.get_secure_cookie("account")

        publish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


        publish_controller = publishController(meet_time, place, contact_way, account, publish_time, tips)
        publish_controller.insertPlan()
        self.redirect('/manage/aboutMe')

