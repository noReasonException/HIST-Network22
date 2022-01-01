import MySQLdb


class DefineVolunteer():
	database_server="localhost"
	database_username="tester"
	database_password="12312312345"
	database_name="greece"
	def __init__(self,user_username,user_password,user_email,user_ip,user_port,IsOnline,req):
		MainConnectionObject = MySQLdb.connect(self.database_server,self.database_username,self.database_password,self.database_name)
		MainCursor = MainConnectionObject.cursor()

