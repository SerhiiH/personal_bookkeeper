from expenses import Expenses
from incomes import Incomes
from liabilities import Liabilities

class Month:
	def __init__(self, name, expensesItems, incomesItems, liabilitiesItems):
		self.monthItems = {'expenses': Expenses(expensesItems), 'incomes': Incomes(incomesItems), 'liabilities': Liabilities(liabilitiesItems)}
		self.name = name.casefold()
		
	def __repr__(self):
		return self.name.upper().center(30, ' ') + '\n' + str(self.monthItems['incomes']) + str(self.monthItems['expenses']) + str(self.monthItems['liabilities']) 

	def getItemsGroup(self, monthItem):
		try:
			return self.monthItems[monthItem.casefold()]
		except KeyError:
			print('ERROR in month.py!!! Incorrect Month item name.')
			return
	




		
if __name__ == '__main__':
	m = Month('October 2019')
	print(m)
