#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import sys
import re
import urllib

sys.path.append(os.path.join(sys.path[0], 'view'))
sys.path.append(os.path.join(sys.path[0], 'control'))
sys.path.append(os.path.join(sys.path[0], 'model'))

from LoginForm import *
from RegisterForm import *
from ManageForm import *
from PublishForm import *
from MaintainUserForm import *
from MaintainPlanForm import *

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('account')
        self.redirect('/')

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "login_url": "/",
    'debug': 'True',
}

application = tornado.web.Application([
    (r'/(admin)?', LoginForm),
    (r'/register', RegisterForm),
    (r'/manage/(aboutMe|otherPlan)', ManageForm),
    (r'/publish', PublishForm),
    (r'/maintainuser', MaintainUserForm),
    (r'/maintainplan', MaintainPlanForm),
    (r'/logout', LogoutHandler),
], **settings)

if __name__ == "__main__":
    print sys.path[0]
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

