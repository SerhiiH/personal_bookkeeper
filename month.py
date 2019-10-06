from expenses import Expenses
from incomes import Incomes
from savings import Savings

class Month:
	def __init__(self, name):
		self.items = {'expenses': Expenses(), 'incomes': Incomes(), 'savings': Savings()}
		self.name = name
		
	def __repr__(self):
		return self.name.upper().center(30, ' ') + '\n' + str(self.items['incomes']) + str(self.items['expenses']) + str(self.items['savings']) 

	def __getitem__(self, key):
		return self.items[key.lower()]

		
if __name__ == '__main__':
	m = Month('October 2019')
	print(m)
