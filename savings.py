from record import Record

class Savings(Record):
	def __init__(self, amount=0, name=None, currency='UAH'):
		Record.__init__(self, amount, 'Savings', name)
		self.currency = currency
		
	@property
	def currency(self):
		return self.currency