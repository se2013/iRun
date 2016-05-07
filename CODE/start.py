#codeing: utf-8

import tornado.ioloop
import tornado.web
import os
import re
import urllib

class BaseHandler(tornado.web.RequestHandler):
    pass

class HomePageHandler(BaseHandler):
    '''HomePage'''
    def get(self):
        infoJson = readInfo();
        info_array = reversed(infoJson['people'])
        self.render('tennis_shot.html', info_array=info_array)

    def post(self):
        infoJson = readInfo();
        nameAdd = self.get_argument('nameAdd', '')
        if nameAdd:
            infoJson = appointAddPeople(infoJson, nameAdd)
            writeInfo(infoJson)
        else:
            temp = getFormInfo(self)
            infoJson['people'].append(temp)
            infoJson['count'] += 1
            writeInfo(infoJson)


class MapHandler(BaseHandler):
    '''Map_appoint'''
    def get(self):
        self.render('appoint.html', position='')


    def post(self):
        person = self.get_argument('person', '') 
        if not person:
            self.render('appoint.html', position='')
        else:
            infoJson = readInfo();
            position = getPositionByName(person, infoJson)
            self.render('appoint.html', position=position)


class WeatherHandler(BaseHandler):
    def get(self):
        self.render('weather.html')



def getFormInfo(self):
    name = self.get_argument('name', '')
    time = self.get_argument('time', '')
    location = self.get_argument('location', '')
    NTRP = self.get_argument('NTRP', '')
    information = self.get_argument('information', '')
    appoint_people = self.get_argument('appoint_people', '')
    x = self.get_argument('x', '')
    y = self.get_argument('y', '')

    return {
            'name':str(name),
            'time':str(time),
            'location':str(location),
            'NTRP':str(NTRP),
            'information':str(information),
            'appoint_people':int(appoint_people),
            'x':str(x),
            'y':str(y),
        }

def readInfo():
    '''return information of Json'''
    info_file = open(r'static/database/database.js')
    temp = info_file.readlines()
    info_file.close()

    temp = ''.join(temp)
    temp = re.split('[\n\r]+', temp)
    temp = ''.join(temp)
    exec(temp)
    return DB

def appointAddPeople(infoJson, name):
    '''search name And add 1 to appoint_people'''
    for i in infoJson['people']:
        if i['name'] == name:
            i['appoint_people'] = i['appoint_people'] + 1
            break
    return infoJson

def writeInfo(infoJson):
    jsonString = 'DB = ' + str(infoJson)
    info_file = open(r'static/database/database.js', 'w')
    info_file.write(jsonString)
    info_file.close()

def getPositionByName(name, infoJson):
    temp = infoJson['people']
    for person in temp:
        if name == person['name']:
            return person['x'] + ';' + person['y']
    return ''

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'debug': 'True',
}

application = tornado.web.Application([
    (r'/', HomePageHandler),
    (r'/map', MapHandler),
    (r'/weather', WeatherHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
