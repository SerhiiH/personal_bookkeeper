class Record:
	def __init__(self, name, currencies):
		self.name = name
		self.amount = {currency.lower(): 0 for currency in currencies}
		
	def __repr__(self):
		string = ''.join(['{0:>25}: {1:,}\n'.format(curr.upper(), val) for curr, val in self.amount.items()])
		return self.name.capitalize() + ':\n' + string
		
	def changeAmount(self, currency, amount, sign = 1):
		currency = currency.lower()
		self.amount[currency] += amount * sign

if __name__ == '__main__':
	r = Record('rent', ['uah', 'usd', 'eur'])
	print(r)
	r.changeAmount('UsD', 200)
	print(r)
	r.changeAmount('uSd', 70, -1)
	print(r)
	