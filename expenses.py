from record import Record

class Expenses(Record):
	def __init__(self, name, amount=0, currency='UAH'):
		Record.__init__(self, 'Expenses', name, amount)