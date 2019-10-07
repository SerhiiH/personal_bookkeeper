class Expenses:
	items = ['rent', 'food', 'other', 'travelling']
	currencies = ['uah', 'usd', 'eur']
	
	def __init__(self):
		self.expenses = {k: {'uah': 0} for k in Expenses.items}
		self.expenses['travelling'] = {currency: 0 for currency in Expenses.currencies}
		self._total = 0
	
	def __getitem__(self, key):
		return self.expenses[key.lower()]
		
	def __setitem__(self, key, val):
		key = key.lower()
		tmpAmount = self.expenses[key]
		self.expenses[key] = val
		if key != 'travelling':
			self._total += val - tmpAmount
	
	def __iter__(self):
		for item in self.expenses.items():
			yield item
			
	def __repr__(self):
		string = ''
		for k1,v1 in self.expenses.items():
			string += '\n{0}\n'.format(k1.capitalize() + ':')
			for k2,v2 in v1.items():
				string += '{0:>19} {1:,}\n'.format(k2.upper() + ':', v2)
		string += '\n{0:15}UAH {1:,}\n'.format('Total:', self._total)
		return 'Expenses:'.center(30, '-') + string + '\n'
		
	@property
	def total(self):
		return self._total
	@total.setter
	def total(self, val):
		self._total = val

if __name__ == '__main__':
	exp = Expenses()
	print(exp)