class Savings:
	items = ['Pocket money', 'Travelling', 'Deposit', 'Interests']
	currencies = ['UAH', 'USD', 'EUR']

	def __init__(self):
		self.savings = {}
		for type in Savings.items:
			if type == 'Travelling':
				self.savings[type] = {'UAH': 0}
			else:
				self.savings[type] = {key: 0 for key in Savings.currencies}
	
	def __getitem__(self, key):
		return self.savings[key]

	def __iter__(self):
		for saving in self.savings.items():
			yield saving
		
	def __repr__(self):
		string = ''
		for k1,v1 in self.savings.items():
			string += '\n{0}\n'.format(k1 + ':')
			for k2,v2 in v1.items():
				string += '\t{0} {1}\n'.format(k2 + ':', v2)
		return 'Savings'.center(30, '-') + string + '\n'
