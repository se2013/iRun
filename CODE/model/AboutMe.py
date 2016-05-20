#coding=utf-8

class AboutMe(object):
	def __init__(self, Id, User_Id, Plan_Id):
		self.id = Id
		self.user_id = User_Id
		self.plan_id = Plan_Id

	def getId(self):
		return self.id

	def setId(self,Id):
		self.id = Id
						
	def getUserId(self):
		return self.user_id

	def setUserId(self,User_Id):
		self.user_id = User_Id
			
	def getPlanId(self):
		return plan_id
		
	def setPlanId(self,Plan_Id):
		self.plan_id = Plan_Id
	
	@staticmethod
	def creatAboutMe(Id, User_Id, Plan_Id):
		return AboutMe(Id, User_Id, Plan_Id)
