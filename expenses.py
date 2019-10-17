from items_group import ItemsGroup

class Expenses(ItemsGroup):
	def __init__(self, itemsTypes):
		ItemsGroup.__init__(self, self.__class__.__name__, itemsTypes)
		self.total = 0
	
	def __repr__(self):
		return ItemsGroup.__repr__(self) + '\n{0:13} UAH: {1:,.2}\n'.format('TOTAL:', self.total)
		
	def changeItemAmount(self, item, amount, currency):
		ItemsGroup.changeItemAmount(self, item, amount, currency)
		if currency.casefold() == 'uah':
			self.countTotal()
		
	def countTotal(self):
		self.total = 0
		for item in self.itemsList.values():
			if item.correspondItem == 'wallet':
				for currency, value in item:
					if currency == 'uah':
						self.total += value
					
			
				
				
if __name__ == '__main__':
	pass