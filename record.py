from datetime import datetime

class Record:
	def __init__(self, type, name, amount=0, currency='UAH'):
		self.__amount = amount
		self.__type = type
		self.__name = name
		self.__modified = None
		self.__currency = currency
	def __repr__(self):
		return self.type + ' (' + self.name + '), amount: ' + self.currency + ' ' + str(self.amount)
	def __modify(self):
		self.__modified = datetime.now()
	def changeAmount(self, val):
		self.__amount += val
		self.__modify()
	def resetAmount(self):
		self.__amount = 0
		self.__modify()

	@property
	def type(self):
		return self.__type
	@property
	def amount(self):
		return self.__amount
	@property
	def name(self):
		return self.__name
	@property
	def modified(self):
		return self.__modified
	@property
	def currency(self):
		return self.__currency
