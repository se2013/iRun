from dbControl import *

class Plan(object):
	def __init__(self, time, place, contact_way, account, publish_time, tips):
		self.__time = time
		self.__place = place
		self.__contact_way = contact_way
		self.__account = account
		self.__publish_time = publish_time
		self.__tips = tips

	def getId(self):
		pass

	def setId(self, planid):
		pass

	def getTime(self):
		pass

	def setTime(self, time):
		pass

	def getPlace(self):
		pass

	def setPlace(self, place):
		pass

	def getcontact_way(self):
		pass

	def setcontact_way(self, contact_way):
		pass

	def getTips(self):
		pass

	def setTips(self, tips):
		pass

	def createPlan(self):
		db = dbControl()
		db.addPlan(self.__time, self.__place, self.__contact_way, self.__account, self.__publish_time, self.__tips)