from item import Item
import functions as f

class ItemsGroup():
	def __init__(self, name, itemTypesList):
		self.name = name
		self.itemsCollection = {}
		for itemType in itemTypesList:
			self.addItem(itemType)
 		
	def __repr__(self):
		string = ''.join([str(item) for item in filter(lambda x: x.getCorrespondItem() == 'wallet', self.itemsCollection.values())])
		string += ''.join([str(item) for item in filter(lambda x: x.getCorrespondItem() != 'wallet', self.itemsCollection.values())])
		return '\n' + self.name.capitalize().center(30, '-') + '\n' + string
		
	def __iter__(self):
		for item in self.itemsCollection.values():
			yield item

	def addItem(self, itemType):
		self.itemsCollection[itemType.name] = Item(itemType.name, itemType.currency, itemType.correspondItem)
		
	def addItemCurrency(self, item, currency):
		f.execWithException(self.addItemCurrency, lambda: self.itemsCollection[item.casefold()].addCurrency(currency), KeyError)
		
	def deleteItem(self, item):
		f.execWithException(self.deleteItem, lambda: self.itemsCollection.pop(item.casefold()), KeyError)
			
	def deleteItemCurrency(self, item, currency):
		f.execWithException(self.deleteItemCurrency, lambda: self.itemsCollection[item.casefold()].deleteCurrency(currency), KeyError)

	def changeItemAmount(self, item, amount, currency):
		f.execWithException(self.changeItemAmount, lambda: self.itemsCollection[item.casefold()].changeAmount(currency, amount), KeyError)

	def getItemCorrespondItem(self, item):
		return f.execWithException(self.getItemCorrespondItem, lambda: self.itemsCollection[item.casefold()].getCorrespondItem(), KeyError)
		
		
if __name__ == '__main__':
	pass