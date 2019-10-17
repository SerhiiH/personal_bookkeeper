from item import Item
import functions as f

class ItemsGroup():
	def __init__(self, name, itemsTypes):
		self.name = name.casefold()
		self.itemsList = {}
		for itemType in itemsTypes:
			self.addItem(itemType)
 		
	def __repr__(self):
		string = ''.join([str(item) for item in filter(lambda x: x.correspondItem == 'wallet', self.itemsList.values())])
		string += ''.join([str(item) for item in filter(lambda x: x.correspondItem != 'wallet', self.itemsList.values())])
		return '\n' + self.name.capitalize().center(30, '-') + '\n' + string
		
	def __iter__(self):
		for item in self.itemsList.values():
			yield item

	def addItem(self, itemType):
		self.itemsList[itemType.name] = Item(itemType)
		
	def addItemCurrency(self, item, currency):
		f.execWithException(self.addItemCurrency, lambda: self.itemsList[item.casefold()].addCurrency(currency), KeyError)
		
	def deleteItem(self, item):
		f.execWithException(self.deleteItem, lambda: self.itemsList.pop(item.casefold()), KeyError)
			
	def deleteItemCurrency(self, item, currency):
		f.execWithException(self.deleteItemCurrency, lambda: self.itemsList[item.casefold()].deleteCurrency(currency), KeyError)

	def changeItemAmount(self, item, amount, currency):
		f.execWithException(self.changeItemAmount, lambda: self.itemsList[item.casefold()].changeAmount(currency, amount), KeyError)

	def getItemCorrespondItem(self, item):
		return f.execWithException(self.getItemCorrespondItem, lambda: self.itemsList[item.casefold()].correspondItem, KeyError)
		
		
if __name__ == '__main__':
	pass