from expenses import Expenses
from incomes import Incomes
from liabilities import Liabilities
import functions as f
import pickle



class Month:
	def __init__(self, name):
		def func():
			with open('database\\items_types_groups.pkl', 'rb') as fileDB:
				itemsTypesGroups = pickle.load(fileDB)
			self.itemsGroups = {}
			self.itemsGroups['expenses'] = Expenses(itemsTypesGroups['expenses'])
			self.itemsGroups['incomes'] = Incomes(itemsTypesGroups['incomes'])
			self.itemsGroups['liabilities'] = Liabilities(itemsTypesGroups['liabilities'])
			self.name = name.casefold()
					
		try:
			f.execWithException(self.__init__, func, EOFError)
		except EOFError:
			print('ERROR!!! Items types groups are not set')
			return
		
	def __repr__(self):
		return self.name.upper().center(30, ' ') + '\n' + str(self.itemsGroups['incomes']) + str(self.itemsGroups['expenses']) + str(self.itemsGroups['liabilities']) 

	def getItemsGroup(self, itemsGroup):
		return f.execWithException(self.getItemsGroup, lambda: self.itemsGroups[itemsGroup.casefold()], KeyError)
	




		
if __name__ == '__main__':
	print(Month('e'))