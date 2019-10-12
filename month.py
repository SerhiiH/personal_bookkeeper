from expenses import Expenses
from incomes import Incomes
from liabilities import Liabilities

class Month:
	def __init__(self, name):
		self.monthItems = {'expenses': Expenses(), 'incomes': Incomes(), 'liabilities': Liabilities()}
		self.name = name.casefold()
		
	def __repr__(self):
		return self.name.upper().center(30, ' ') + '\n' + str(self.items['incomes']) + str(self.items['expenses']) + str(self.items['liabilities']) 

	def getMonthItem(self, monthItem):
		try:
			return self.monthItems[monthItem.casefold()]
		except KeyError:
			print('ERROR!!! Incorrect Month item name.')
			return
	




		
if __name__ == '__main__':
	m = Month('October 2019')
	print(m)
