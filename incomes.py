from items_group import ItemsGroup

class Incomes(ItemsGroup):
	def __init__(self,itemTypesList):
		ItemsGroup.__init__(self, self.__class__.__name__, itemTypesList)
		self.total = 0
	
	def __repr__(self):
		return ItemsGroup.__repr__(self) + '\n{0:13} UAH: {1:,}\n'.format('TOTAL:', self.total)		

	def changeItemAmount(self, item, amount, currency):
		ItemsGroup.changeItemAmount(self, item, amount, currency)
		if currency.casefold() == 'uah':
			self.countTotal()
		
	def countTotal(self):
		self.total = 0
		for item in self.itemsCollection.values():
			if item.getCorrespondItem() == 'wallet':
				for currency, value in item:
					if currency == 'uah':
						self.total += value

						
				
if __name__ == '__main__':
	pass