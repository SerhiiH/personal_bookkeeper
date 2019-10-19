import functions as f



class Item:
	def __init__(self, itemType):
		self.name = itemType.name
		self._amount = {currency: 0 for currency in itemType.currency}
		self._correspondItem = itemType.correspondItem
		
	def __repr__(self):
		return self.name.capitalize() + ':\n' + ''.join(['{0:>17}: {1:,.2f}\n'.format(curr.upper(), val) for curr, val in self._amount.items()])
		
	def __iter__(self):
		for value in self._amount.items():
			yield value 
		
	def changeAmount(self, currency, amount):
		def func():
			curr = currency.casefold()
			value = amount
			self._amount[curr] += value
		f.execWithException(self.changeAmount, func, KeyError, ValueError)
			
	@property
	def correspondItem(self):
		return self._correspondItem

	@property
	def amount(self, currency):
		return self._amount[currency.casefold()]
	
	def addCurrency(self, currency):
		self._amount[currency.casefold()] = 0
		
	def deleteCurrency(self, currency):
		f.execWithException(self.deleteCurrency, lambda: self._amount.pop(currency.casefold()), KeyError)
		
		

if __name__ == '__main__':
	pass
	