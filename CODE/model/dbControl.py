#coding=utf-8

import MySQLdb

class dbControl():
    def __init__(self):
        self.conn = MySQLdb.connect(
                       host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       db = 'iRun',
                       charset = 'utf8'
                       )
        
    def __del__(self):
        self.conn.close()
        
    def getAllUser(self):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM user"
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()

    def getUserById(self, userid):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM user WHERE id = %s" % (userid)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()
            
    def getUserByName(self, name):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM user WHERE name = '%s'" % (name)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()
                          
    def getUserByAccount(self, account):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM user WHERE account = '%s'" % (account)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()
   
    def getAllAdmin(self):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM admin"
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()

    def getAdminById(self, id):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM admin WHERE id = %s" % (id)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()
             
    def getAdminByAccount(self, account):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM admin WHERE account = %s" % (account)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()
            
    def getAllPlan(self):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM plan"
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()

    def getPlanById(self, id):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM plan WHERE id = %d" % (id)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()

    def getCreatePlanByUserAccount(self, account):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM plan WHERE create_user = %s" % (account)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()

    def deleteCreatePlanByUserAccount(self,account):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM plan WHERE create_user = '%s'" % (account)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def deleteCreatePlanByPlanId(self, plan_id):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM plan WHERE plan_id = %d" % (plan_id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def deleteJoinPlanByUserAccount(self, user_account):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM joinin WHERE user_account='%s'" % (user_account)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def deleteJoinPlanByPlanId(self, plan_id):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM joinin WHERE plan_id=%d" % (plan_id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def deleteCollectPlanByUserAccount(self, user_account):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM collect WHERE user_account='%s'" % (user_account)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def deleteCollectPlanByPlanId(self, plan_id):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM collect WHERE plan_id=%d" % (plan_id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def getJoinPlanByUserAccount(self, account):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT plan.id, plan.time, plan.location, plan.contact, plan.create_user, plan.publish_time, plan.tips FROM joinin,plan WHERE joinin.user_account='%s' AND joinin.plan_id=plan.id"  % (account)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()

    def cancleJoinPlan(self,user_account,plan_id):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM joinin WHERE user_account='%s' AND plan_id=%d" % (user_account,plan_id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def joinPlan(self,user_account,plan_id):
        cursor = self.conn.cursor()
        try:
            sql = "INSERT joinin VALUES('%s',%d)" % (user_account,plan_id)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close()

    def updatePlanLoc(self,plan_id,location):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE plan SET location=\'"+location+"\' WHERE id=%d" % (plan_id)
            #print sql
            #sql = "UPDATE plan SET location=%s WHERE id=%d" % (location,plan_id)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close()

    def updatePlanTips(self,plan_id,tips):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE plan SET tips=\'"+tips+"\' WHERE id=%d" % (plan_id)
            #sql = "UPDATE plan SET tips=%s WHERE id=%d" % (tips,plan_id)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close()

    def updatePlanContact(self,plan_id,contact):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE plan SET contact=\'"+contact+"\' WHERE id=%d" % (plan_id)
            #sql = "UPDATE plan SET contact=%s WHERE id=%d" % (contact,plan_id)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close() 
        
    def updatePlanTime(self,plan_id,time):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE plan SET time=\'"+time+"\' WHERE id=%d" % (plan_id)
            #sql = "UPDATE plan SET time=%s WHERE id=%d" % (time,plan_id)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close()
  
    def addUser(self,*msg):
        cursor = self.conn.cursor()
        a = msg[0]
        n = msg[1]
        p = msg[2]
        #print i,n,a,p

        try:
            sql = "INSERT user(account, name, password) VALUES("+"\'"+a+"\',\'"+n+"\',\'"+p+"\')"
            #sql = "INSERT INTO user(id,name,account,password) VALUES(%s,%s,%s,%s)" % (i,n,a,p)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close()

    def delUser(self, account):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM user WHERE account = '%s'" % (account)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()
            
    def addPlan(self,*msg):
        cursor = self.conn.cursor()
        t = msg[0]
        l = msg[1]
        c = msg[2]
        cu = msg[3]
        pt = msg[4]
        tips = msg[5]
        #print t,l,c,cu,pt,tips
        try:
            sql = "INSERT plan(time,location,contact,create_user,publish_time,tips)\
            VALUES("+"\'"+t+"\',\'"+l+"\',\'"+c+"\',\'"+cu+"\',\'"+pt+"\',\'"+tips+"\')"
            #sql = "INSERT INTO plan(time,location,contact,create_user,publish_time,tips) VALUES(%s,%s,%s,%s,%s,%s)" % (t,l,c,cu,pt,tips)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close()

    def collectPlan(self,user_account,plan_id):
        cursor = self.conn.cursor()
        try:
            sql = "INSERT collect VALUES(%s,%d)" % (user_account,plan_id)
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        finally:
            cursor.close()

    def cancleCollectPlan(self,user_account,plan_id):
        cursor = self.conn.cursor()
        try:
            sql = "DELETE FROM collect WHERE user_account=%s AND plan_id=%d" % (user_account,plan_id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()

    def getCollectPlanByUserAccount(self,user_account):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT plan.id, plan.time, plan.location, plan.contact, plan.create_user, plan.publish_time, plan.tips FROM collect,plan WHERE collect.user_account='%s' AND collect.plan_id=plan.id"  % (user_account)
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs
        finally:
            cursor.close()
            self.conn.commit()

    def getOtherPlanByUserAccount(self, account):
        cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM plan WHERE create_user != '%s'" % (account)
            cursor.execute(sql)
            rs = cursor.fetchall();
            return rs
        finally:
            cursor.close()
            
    def updateUserPasswordById(self, id, password):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE user SET password=%s WHERE id=%d" % (password, id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()            

    def updateUserNameById(self, id, name):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE user SET name='%s' WHERE id=%d" % (name, id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()  

    def updateAdminPasswordById(self, id, password):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE admin SET password=%s WHERE id=%d" % (password, id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit()            

    def updateAdminNameById(self, id, name):
        cursor = self.conn.cursor()
        try:
            sql = "UPDATE admin SET name='%s' WHERE id=%d" % (name, id)
            cursor.execute(sql)
        finally:
            cursor.close()
            self.conn.commit() 
