from record import Record

class Savings(Record):
	def __init__(self, name, amount=0, currency='UAH'):
		Record.__init__(self, 'Savings', name, amount)
