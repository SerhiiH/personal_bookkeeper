from record_class import Record

class Expenses(Record):
	def __init__(self, amount=0, type=''):
		Record.__init__(self, amount, 'Expenses', type)

exp = Expenses(100, 'Trip')