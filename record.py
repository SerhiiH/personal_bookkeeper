class Record:
	def __init__(self, name, currencies = ['uah'], source = 'wallet'):
		self.name = name.lower()
		self.amount = {currency.lower(): 0 for currency in currencies}
		self.source = source.lower()
		
	def __repr__(self):
		string = ''.join(['{0:>25}: {1:,}\n'.format(curr.upper(), val) for curr, val in self.amount.items()])
		return self.name.capitalize() + '(source: {0}):\n'.format(self.source) + string
		
	def changeAmount(self, currency, amount, sign = 1):
		currency = currency.lower()
		self.amount[currency] += amount * sign

if __name__ == '__main__':
	r = Record('rent', ['uah', 'usd', 'eur'])
	print(r)
	r.changeAmount('UsDs', 200)
	print(r)
	r.changeAmount('uSd', 70, -1)
	print(r)
	