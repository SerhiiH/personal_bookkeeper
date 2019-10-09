from month_item import MonthItem

class Expenses(MonthItem):
	def __init__(self):
		MonthItem.__init__(self, self.__class__.__name__)
		self.total = 0
	
	def __repr__(self):
		return MonthItem.__repr__(self) + '{0:31} UAH: {1:,}\n'.format('TOTAL:', self.total)
		
	def changeAmount(self, item, currency, amount, sign = 1):
		MonthItem.changeItemAmount(self, item, currency, amount, sign)

		try:
			if self.itemsSources[item.lower()] == 'wallet':
				self.total += float(amount) * sign
	

if __name__ == '__main__':
	exp = Expenses()
	exp.addItem('Rent', 'uah')
	exp.addItem('TRAVELLING', 'uah', 'usd', 'eur', source = 'travelling')
	exp.addItem('FooD', 'uah')
	
	print(exp)