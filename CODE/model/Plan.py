#coding=utf-8

class Plan(object):
	def __init__(self, Id, Time, Place, Contact_Way, User_Id, Publish_Time, Tips):
		self.id = Id
		self.time = Time
		self.place = Place
		self.contact_way = Contact_Way
		self.user_id = User_Id
		self.publish_time = Publish_Time
		self.tips = Tips

	def getId(self):
		return self.id

	def setId(self, Id):
		self.id = Id

	def getTime(self):
		return self.time

	def setTime(self, Time):
		self.time = Time

	def getPlace(self):
		return self.place

	def setPlace(self, Place):
		self.place = Place

	def getcontact_way(self):
		return self.contact_way

	def setcontact_way(self, Contact_Way):
		self.contact_way = Contact_Way

	def getTips(self):
		return self.tips

	def setTips(self, Tips):
		self.tips = Tips

	@staticmethod
	def creatPlan(Id, Time, Place, Contact_Way, User_Id, Publish_Time, Tips):
		return Plan(Id, Time, Place, Contact_Way, User_Id, Publish_Time, Tips)
		
