class Savings:
	items = ['pocket money', 'travelling', 'deposit', 'interests']
	currencies = ['uah', 'usd', 'eur']

	def __init__(self):
		self.savings = {item: {currency: 0 for currency in Savings.currencies} for item in Savings.items}
	
	def __getitem__(self, key):
		return self.savings[key.lower()]

	def __iter__(self):
		for type, currency in self.savings.items():
			for cur in currency:
				yield cur
		
	def __repr__(self):
		string = ''
		for k1,v1 in self.savings.items():
			string += '\n{0}\n'.format(k1.capitalize() + ':')
			for k2,v2 in v1.items():
				string += '{0:>19} {1}\n'.format(k2.upper() + ':', v2)
		return 'Savings'.center(30, '-') + string + '\n'


if __name__ == '__main__':
	sav = Savings()
	print(sav['travelling']['usd'])
	count = 0
	for s in sav: 
		print(s)
	print(sav)