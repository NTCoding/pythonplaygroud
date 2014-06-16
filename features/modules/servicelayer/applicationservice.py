
class ApplicationService:

	def __init__(self, database):
		self.database = database

	def findAllCustomersForBusiness(self, id):
		return self.database.find(id)