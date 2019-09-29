class Incomes:
	family = ['Serhii', 'Alona']
	
	def __init__(self):
		self.incomes = {k: Record() for k in Incomes.persons}
	def __iter__(self):
		for person in self.incomes.items():
			yield person