class Item:
	def __init__(self, name, currencies, correspondingItem):
		name = name.casefold()
		currencies = [curr.casefold() for curr in currencies]
		correspondingItem = correspondingItem.casefold()
		
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
			currency = currency.casefold()
			amount = float(amount)
			self.amount[currency] += amount * sign
		except KeyError:
			print('ERROR!!! Incorrect Currency name.')
			return
		except ValueError:
			print('ERROR!!! Incorrect amount format.')
			return
		except:
			print('ERROR!!! Incorrect input.')
			return		
			
	def getCorrespondingItem(self):
		return self.correspondingItem

	def getAmount(self, currency):
		return self.amount[currency.casefold()]
	
	def addCurrency(self, currency):
		self.amount[currency.casefold()] = 0
		
	def deleteCurrency(self, currency):
		try:
			del self.amount[currency.casefold()]
		except KeyError:
			print('ERROR!!! Incorrect Currency name.')
			return
		
		

if __name__ == '__main__':
	r = Item('rent', ['uah', 'usd', 'eur'], correspondingItem = 'wallet')
	print(r)
	r.changeAmount('usd', 200)
	print(r)
	r.changeAmount('usd', 70, -1)
	print(r)
	