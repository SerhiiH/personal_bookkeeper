class Record:
	def __init__(self, name, currencies):
		self.name = name
		self.amount = {currency: 0 for currency in currencies}
		
	def __repr__(self):
		return ''.join(['{0:>35}: {1:,}\n'.format(curr.upper(), val) for curr, val in self.amount.items()])
		
	def changeAmount(self, currency, amount, sign = 1):
		try:
			self.amount[currency] += amount * sign
		except KeyError:
			print('ERROR!!! Incorrect currency.')

if __name__ == '__main__':
	r = Record('rent', ['uah', 'usd', 'eur'])
	print(r)
	r.changeAmount('usd', 200)
	print(r)
	r.changeAmount('usd', 70, -1)
	print(r)
	