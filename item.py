import functions as f


class Item:
	def __init__(self, name, currencies, correspondItem):
		name = name
		currencies = currencies
		correspondItem = correspondItem
		
		self.name = name
		self.amount = {currency: 0 for currency in currencies}
		self.correspondItem = correspondItem
		
	def __repr__(self):
		return self.name.capitalize() + ':\n' + ''.join(['{0:>17}: {1:,}\n'.format(curr.upper(), val) for curr, val in self.amount.items()])
		
	def __iter__(self):
		for value in self.amount.items():
			yield value 
		
	def changeAmount(self, currency, amount):
		def func():
			curr = currency.casefold()
			value = float(amount)
			self.amount[curr] += value
		f.execWithException(self.changeAmount, func, KeyError, ValueError)
			
	def getCorrespondItem(self):
		return self.correspondItem

	def getAmount(self, currency):
		return self.amount[currency.casefold()]
	
	def addCurrency(self, currency):
		self.amount[currency.casefold()] = 0
		
	def deleteCurrency(self, currency):
		f.execWithException(self.deleteCurrency, lambda: self.amount.pop(currency.casefold()), KeyError)
		
		

if __name__ == '__main__':
	r = Item('rent', ['uah', 'usd', 'eur'], correspondItem = 'wallet')
	print(r)
	r.changeAmount('usd', 200)
	print(r)
	r.changeAmount('usd', '3e')
	print(r)
	