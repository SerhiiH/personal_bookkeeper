class Incomes:
	family = ['Serhii', 'Alona']
	
	def __init__(self):
		self.incomes = {k: 0 for k in Incomes.family}
		self._total = 0
	
	def __getitem__(self, person):
		return self.incomes[person]
		
	def __setitem__(self, person, val):
		self._total += val - self.incomes[person]
		self.incomes[person] = val
	
	def __iter__(self):
		for person in self.incomes.items():
			yield person
			
	def __repr__(self):
		string = ''
		for k,v in self.incomes.items():
			string += '\t{0:15}UAH {1:,}\n'.format(k + ':', v)
		string += '\t{0:15}UAH {1:,}\n'.format('Total:', self._total)
		return 'Incomes:\n' + string
		
	@property
	def total(self):
		return self._total
	@total.setter
	def total(self, val):
		self._total = val
	
inc = Incomes()