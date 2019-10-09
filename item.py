class Item:
	def __init__(self, name, currencies, correspondingItem):
		self.name = name
		self.amount = {currency: 0 for currency in currencies}
		self.correspondingItem = correspondingItem
		
	def __repr__(self):
		return self.name.capitalize() + ':\n' + ''.join(['{0:>17}: {1:,}\n'.format(curr.upper(), val) for curr, val in self.amount.items()])
		
	def __iter__(self):
		for value in self.amount.items():
			yield value 
		
	def changeAmount(self, currency, amount, sign = 1):
		try:
			self.amount[currency] += amount * sign
		except KeyError:
			print('ERROR!!! Incorrect currency.')
			
	def getCorrespondingItem(self):
		return self.correspondingItem

if __name__ == '__main__':
	r = Item('rent', ['uah', 'usd', 'eur'], correspondingItem = 'wallet')
	print(r)
	r.changeAmount('usd', 200)
	print(r)
	r.changeAmount('usd', 70, -1)
	print(r)
	