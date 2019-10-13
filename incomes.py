from month_item import MonthItem

class Incomes(MonthItem):
	def __init__(self,itemTypesList):
		MonthItem.__init__(self, self.__class__.__name__, itemTypesList)
		self.total = 0
	
	def __repr__(self):
		return MonthItem.__repr__(self) + '\n{0:13} UAH: {1:,}\n'.format('TOTAL:', self.total)		

	def changeItemAmount(self, item, amount, currency):
		MonthItem.changeItemAmount(self, item, amount, currency)
		if currency.casefold() == 'uah':
			self.countTotal()
		
	def countTotal(self):
		self.total = 0
		for item in self.itemTypes.values():
			if item.getCorrespondItem() == 'wallet':
				for currency, value in item:
					if currency == 'uah':
						self.total += value

						
				
if __name__ == '__main__':
	inc = Incomes()
	# inc.addItem('Serhii', 'uah', correspondItem = 'wallet')
	# inc.addItem('Alona', 'uah', correspondItem = 'wallet')
	print(inc)
	
	# inc.changeItemAmount('serhii', 1000000)
	# inc.changeItemAmount('alona', 1100000)
	# print(inc)
	
