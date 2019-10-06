from expenses import Expenses
from incomes import Incomes
from savings import Savings

class Month:
	def __init__(self, name):
		self.items = {'e': Expenses(), 'i': Incomes(), 's': Savings()}
		self.name = name
		
	def __repr__(self):
		return self.name.upper().center(30, ' ') + '\n' + str(self.items['i']) + str(self.items['e']) + str(self.items['s']) 

	def __getitem__(self, key):
		return self.items[key.lower()]

		
if __name__ == '__main__':
	m = Month('October 2019')
