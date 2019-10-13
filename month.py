from expenses import Expenses
from incomes import Incomes
from liabilities import Liabilities
import functions as f
from item_type import ItemType

class Month:
	def __init__(self, name, expensesItems, incomesItems, liabilitiesItems):
		self.itemsGroups = {'expenses': Expenses(expensesItems), 'incomes': Incomes(incomesItems), 'liabilities': Liabilities(liabilitiesItems)}
		self.name = name.casefold()
		
	def __repr__(self):
		return self.name.upper().center(30, ' ') + '\n' + str(self.itemsGroups['incomes']) + str(self.itemsGroups['expenses']) + str(self.itemsGroups['liabilities']) 

	def getItemsGroup(self, itemsGroup):
		return f.execWithException(self.getItemsGroup, lambda: self.itemsGroups[itemsGroup.casefold()], KeyError)
	




		
if __name__ == '__main__':
	pass