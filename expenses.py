from month_item import MonthItem

class Expenses(MonthItem):
	def __init__(self):
		MonthItem.__init__(self, self.__class__.__name__)
		self.addItem('rent', 'uah', correspondingItem = 'wallet')
		self.addItem('food', 'uah', correspondingItem = 'wallet')
		self.addItem('other', 'uah', correspondingItem = 'wallet')
		self.addItem('travelling', 'uah', 'usd', 'eur')
		self.total = 0
	
	def __repr__(self):
		return MonthItem.__repr__(self) + '\n{0:13} UAH: {1:,}\n'.format('TOTAL:', self.total)
		
	def changeItemAmount(self, item, amount, currency = 'uah', sign = 1):
		MonthItem.changeItemAmount(self, item, currency, amount)
		if currency.casefold() == 'uah':
			self.countTotal()
		
	def countTotal(self):
		self.total = 0
		for item in self.itemTypes.values():
			if item.getCorrespondingItem() == 'wallet':
				for currency, value in item:
					if currency == 'uah':
						self.total += value
					
			
				
				
if __name__ == '__main__':
	exp = Expenses()
	# exp.addItem('Rent', 'uah', correspondingItem = 'wallet')
	# exp.addItem('TRAVELLING', 'uah', 'usd', 'eur', correspondingItem = 'travelling')
	# exp.addItem('FooD', 'uah', correspondingItem = 'wallet')
	print(exp)
	
	# exp.changeItemAmount('rent', 300)
	# exp.changeItemAmount('travelling', 300, 'usd')
	# exp.changeItemAmount('travelling', 300)
	# exp.changeItemAmount('rent', 300)
	# exp.changeItemAmount('food', 300)
	# exp.changeItemAmount('food', 1300)
	# print(exp)