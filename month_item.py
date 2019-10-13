from item import Item
import functions as f

class MonthItem():
	def __init__(self, name, itemTypesList):
		self.name = name
		self.itemTypes = {}
		for itemType in itemTypesList:
			self.addItem(itemType)
 		
	def __repr__(self):
		string = ''.join([str(item) for item in filter(lambda x: x.getCorrespondItem() == 'wallet', self.itemTypes.values())])
		string += ''.join([str(item) for item in filter(lambda x: x.getCorrespondItem() != 'wallet', self.itemTypes.values())])
		return '\n' + self.name.capitalize().center(30, '-') + '\n' + string
		
	def __iter__(self):
		for item in self.itemTypes.values():
			yield item

	def addItem(self, itemType):
		self.itemTypes[itemType.name] = Item(itemType.name, itemType.currency, itemType.correspondItem)
		
	def addItemCurrency(self, item, currency):
		f.execWithException(self.addItemCurrency, lambda: self.itemTypes[item.casefold()].addCurrency(currency), KeyError)
		
	def deleteItem(self, item):
		f.execWithException(self.deleteItem, lambda: self.itemTypes.pop(item.casefold()), KeyError)
			
	def deleteItemCurrency(self, item, currency):
		f.execWithException(self.deleteItemCurrency, lambda: self.itemTypes[item.casefold()].deleteCurrency(currency), KeyError)

	def changeItemAmount(self, item, amount, currency):
		f.execWithException(self.changeItemAmount, lambda: self.itemTypes[item.casefold()].changeAmount(currency, amount), KeyError)

	def getItemCorrespondItem(self, item):
		f.execWithException(self.getItemCorrespondItem, lambda: self.itemTypes[item.casefold()].getCorrespondItem(), KeyError)
		
		
if __name__ == '__main__':
	mi = MonthItem('Expenses')
	mi.addItem('Rent', 'uah', correspondItem = 'wallet')
	mi.addItem('TRAVELLING', 'uah', 'usd', 'eur', correspondItem = 'travelling')
	mi.addItem('FooD', 'uah', correspondItem = 'wallet')
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
	
	print(mi.getItemCorrespondItem('FOOD'))
	print(''.center(30, '*'))
	
	for it in mi:
		print(it)
	