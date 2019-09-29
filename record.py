from datetime import datetime

class Record:
	def __init__(self, amount=0):
		self.amount = amount
		self.date = datetime.now()
	def __repr__(self):
		return self.currency + ' ' + str(self.amount) + ' ' + self.date.strftime('%d.%m.%Y %H:%M:%S')
	def updateDate(self):
		self.date = datetime.now()
	def changeRecord(self, val):
		self.amount += val
		self.updateDate(self)

