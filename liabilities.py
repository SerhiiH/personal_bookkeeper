from month_item import MonthItem

class Liabilities(MonthItem):
	def __init__(self, itemTypesList):
		MonthItem.__init__(self, self.__class__.__name__, itemTypesList)


if __name__ == '__main__':
	liab = Liabilities()
	liab.addItem('wallet', 'uah')
	print(liab)
	
	liab.changeItemAmount('wallet', 1000000)
	print(liab)
	
	liab.changeItemAmount('wallet', 1100000)
	print(liab)
	
	liab.addItemCurrency('wallet', 'usd')
	print(liab)
	
	liab.deleteItemCurrency('wallet', 'eur')
	print(liab)
	
	liab.deleteItemCurrency('wallet', 'usd')
	print(liab)
	
