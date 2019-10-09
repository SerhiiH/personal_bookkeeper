from item import Item

class MonthItem():
	def __init__(self, name):
		self.name = name
		self.itemTypes = {}
 		
	def __repr__(self):
		string = ''.join([str(item) for item in filter(lambda x: x.getCorrespondingItem() == 'wallet', self.itemTypes.values())])
		string += ''.join([str(item) for item in filter(lambda x: x.getCorrespondingItem() != 'wallet', self.itemTypes.values())])
		return self.name.capitalize().center(30, '-') + '\n' + string
		
	def __iter__(self):
		for item in self.itemTypes.values():
			for value in item:
				yield value

	def addItem(self, name, *currencies, correspondingItem = ''):
		name = name.lower()
		currencies = [curr.lower() for curr in currencies]
		correspondingItem = correspondingItem.lower()
		self.itemTypes[name] = Item(name, currencies, correspondingItem)
		
	def deleteItem(self, item):
		try:
			item = item.lower()
			del self.itemTypes[item]
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		
	def changeItemAmount(self, item, currency, amount, sign = 1):
		try:
			item = item.lower()
			currency = currency.lower()
			amount = float(amount)
			self.itemTypes[item].changeAmount(currency, amount, sign)
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		except ValueError:
			print('ERROR!!! Incorrect amount format.')
			return
	
	def getItemCorrespingItem(self, item):
		try:
			return self.itemTypes[item.lower()].getCorrespondingItem()
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
	
	print(mi.getItemCorrespingItem('FOOD'))
	print(''.center(30, '*'))
	
	for it in mi:
		print(it)
	