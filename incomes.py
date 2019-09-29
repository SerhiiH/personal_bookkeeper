from record import Record

class Incomes(Record):
	def __init__(self, amount=0, name=None):
		Record.__init__(self, amount, 'Incomes', name)