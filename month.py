from expenses import Expenses
from incomes import Incomes
from savings import Savings

class Month:
	def __init__(self, name):
		self.__items = {'e': Expenses(), 'i': Incomes(), 's': Savings()}
		self.__name = name
		
	def __repr__(self):
		return self.__name.upper().center(30, ' ') + '\n' + str(self.__items['i']) + str(self.__items['e']) + str(self.__items['s']) 

	def __getitem__(self, key):
		return self.__items[key.lower()]

		
if __name__ == '__main__':
	m = Month('October 2019')
