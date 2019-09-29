class Expenses:
	expensesItems = ['Rent', 'Food', 'Travelling', 'Other']
	
	def __init__(self):
		self.expenses = {k: Record() for k in Expenses.expensesItems}
	def __getitem__(self, item):
		return self.expenses[item]
	def __iter__(self):
		for rec in self.expenses.items():
			yield rec
			
		
exp = Expenses()
