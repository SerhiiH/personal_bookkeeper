class Incomes:
	family = ['serhii', 'alona']
	
	def __init__(self):
		self.incomes = {k: 0 for k in Incomes.family}
		self._total = 0
	
	def __getitem__(self, key):
		return self.incomes[person.key()]
		
	def __setitem__(self, key, val):
		key = key.lower()
		self._total += val - self.incomes[key]
		self.incomes[key] = val
	
	def __iter__(self):
		for person in self.incomes.items():
			yield person
			
	def __repr__(self):
		string = ''
		for k,v in self.incomes.items():
			string += '{0:15}UAH {1:,}\n'.format(k.capitalize() + ':', v)
		string += '{0:15}UAH {1:,}\n'.format('Total:', self._total)
		return 'Incomes:'.center(30, '-') + '\n' + string + '\n'
		
	@property
	def total(self):
		return self._total
	@total.setter
	def total(self, val):
		self._total = val
