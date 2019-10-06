class Expenses:
	items = ['rent', 'food', 'travelling', 'other']
	
	def __init__(self):
		self.expenses = {k: 0 for k in Expenses.items}
		self._total = 0
	
	def __getitem__(self, key):
		return self.expenses[key.lower()]
		
	def __setitem__(self, key, val):
		key = key.lower()
		self._total += val - self.expenses[key]
		self.expenses[key] = val
	
	def __iter__(self):
		for item in self.expenses.items():
			yield item
			
	def __repr__(self):
		string = ''
		for k,v in self.expenses.items():
			string += '{0:15}UAH {1:,}\n'.format(k.capitalize() + ':', v) 
		string += '{0:15}UAH {1:,}\n'.format('Total:', self._total)
		return 'Expenses:'.center(30, '-') + '\n' + string + '\n'
		
	@property
	def total(self):
		return self._total
	@total.setter
	def total(self, val):
		self._total = val
