from record import Record

class Incomes(Record):
	def __init__(self, name, amount=0, currency='UAH'):
		Record.__init__(self, 'Incomes', name, amount)