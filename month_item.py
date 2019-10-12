from item import Item

class MonthItem():
	def __init__(self, name):
		self.name = name
		self.itemTypes = {}
 		
	def __repr__(self):
		string = ''.join([str(item) for item in filter(lambda x: x.getCorrespondingItem() == 'wallet', self.itemTypes.values())])
		string += ''.join([str(item) for item in filter(lambda x: x.getCorrespondingItem() != 'wallet', self.itemTypes.values())])
		return '\n' + self.name.capitalize().center(30, '-') + '\n' + string
		
	def __iter__(self):
		for item in self.itemTypes.values():
			yield item

	def addItem(self, name, *currencies, correspondingItem = ''):
		name = name.casefold()
		self.itemTypes[name] = Item(name, currencies, correspondingItem)
		
	def addItemCurrency(self, item, currency):
		try:
			self.itemTypes[item.casefold()].addCurrency(currency)
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		
	def deleteItem(self, item):
		try:
			del self.itemTypes[item.casefold()]
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
			
	def deleteItemCurrency(self, item, currency):
		try:
			self.itemTypes[item.casefold()].deleteCurrency(currency)
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		
	def changeItemAmount(self, item, amount, currency = 'uah', sign = 1):
		try:
			self.itemTypes[item.casefold()].changeAmount(currency, amount, sign)
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		except:
			print('ERROR!!! Incorrect input.')
			return
	
	def getItemCorrespondingItem(self, item):
		try:
			return self.itemTypes[item.casefold()].getCorrespondingItem()
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		
		
if __name__ == '__main__':
	mi = MonthItem('Expenses')
	mi.addItem('Rent', 'uah', correspondingItem = 'wallet')
	mi.addItem('TRAVELLING', 'uah', 'usd', 'eur', correspondingItem = 'travelling')
	mi.addItem('FooD', 'uah', correspondingItem = 'wallet')
	print(mi)
	print(''.center(30, '*'))
	
	mi.changeItemAmount('rent', 'uah', 1000)
	print(mi)
	print(''.center(30, '*'))
	
	mi.changeItemAmount('rent', 'uah', 500, -1)
	print(mi)
	print(''.center(30, '*'))
	
	mi.changeItemAmount('rent', 'usd', 500)
	print(mi)
	print(''.center(30, '*'))
	
	mi.changeItemAmount('bikes', 'uah', 500)
	print(mi)
	print(''.center(30, '*'))
	
	mi.changeItemAmount('rent', 'uah', '541-')
	print(mi)
	print(''.center(30, '*'))
	
	mi.deleteItem('rent')
	print(mi)
	print(''.center(30, '*'))
	
	print(mi.getItemCorrespondingItem('FOOD'))
	print(''.center(30, '*'))
	
	for it in mi:
		print(it)
	