from month import Month
from liabilities import Liabilities
from item_type import ItemType
import functions as f

class Runtime:
	def __init__(self):
		self.itemsTypesCollection = {
			'expenses':  {
			'rent': ItemType('Rent', 'Wallet', 'UAH'), 
			'food': ItemType('Food', 'Wallet', 'UAH'), 
			'pocket money': ItemType('Pocket money', 'Wallet', 'UAH'),
			'travelling': ItemType('Travelling', 'Travelling', 'UAH')
			}, 
			'incomes': {
			'serhii': ItemType('Serhii', 'Wallet', 'UAH'),
			'alona': ItemType('Alona', 'Wallet', 'UAH')
			},
			'liabilities': {
			'wallet': ItemType('Wallet', '', 'UAH', 'USD', 'EUR'),
			'travelling': ItemType('Travelling', '', 'UAH', 'USD', 'EUR'),
			'deposit': ItemType('Deposit', '', 'UAH', 'USD', 'EUR')
			}
		}
		self.currentMonth = None
		self.totalLiabilities = None
		self.monthHistory = {}
		self.commands = {'new total': self.newTotal, 'new month': self.newMonth, 'input total': self.inputTotal, 
			'input month': self.inputCurrent, 'show total': self.showTotal, 'show month': self.showCurrent}

	def run(self):
		self.prepare()
		self.communicate()
	
	def prepare(self):
		if not self.totalLiabilities:
			self.totalLiabilities = Liabilities(self.getItemsTypesGroup('liabilities').values())

	def communicate(self):
		request = input('Enter the request ("q" - quit): ')
		while request != 'q':
			self.processRequest(request)
			request = input('Enter the record ("q" - quit): ')	
	
	def processRequest(self, requestString):
		args = [arg.strip().casefold() for arg in requestString.split(',')]
		
		def func():
			if len(args) > 1:
				self.commands[args[0]](*args[1:])
			else:
				self.commands[args[0]]()
			
		try:
			f.execWithException(self.processRequest, func, KeyError)
		except KeyError:
			return
		
	def newTotal(self):
		self.totalLiabilities = Liabilities(self.getItemsTypesGroup('liabilities').values())
		
	def newMonth(self, *args):
		if not args:
			print('ERROR in runtime.py!!! Month name must be entered.')
			return
			
		if self.currentMonth:
			self.monthHistory.append(self.currentMonth) 
		
		self.currentMonth = Month(args[0], self.getItemsTypesGroup('expenses').values(), self.getItemsTypesGroup('incomes').values(), 
			self.getItemsTypesGroup('liabilities').values())

	def inputTotal(self, *args):
		def func():
			item = args[0]
			amount = args[1]
			if len(args) == 2:
				currency = 'uah'
			else:
				currency = args[2]
				
			self.totalLiabilities.changeItemAmount(item, amount, currency)
			
		try:
			f.execWithException(self.inputTotal, func, ValueError, KeyError, IndexError)
		except (ValueError, KeyError, IndexError):
			return
		
	def inputCurrent(self, *args):
		if not self.currentMonth:
			print('"Current Month" record must be created before filling in.')
			return
		
		def func():
			itemsGroupName = args[0]
			itemName = args[1]
			amount = float(args[2])
			if len(args) == 3:
				currency = 'uah'
			else:
				currency = args[3]
			
			itemsGroup = self.currentMonth.getItemsGroup(itemsGroupName)
			itemsGroup.changeItemAmount(itemName, amount, currency)
			itemCorrespondItem = itemsGroup.getItemCorrespondItem(itemName)
			
			if itemCorrespondItem and itemsGroupName.casefold() != 'liabilities':
				if itemsGroupName.casefold() == 'expenses':
					amount *= -1
				itemsGroupLiab = self.currentMonth.getItemsGroup('liabilities')
				itemsGroupLiab.changeItemAmount(itemCorrespondItem, amount, currency)
				self.totalLiabilities.changeItemAmount(itemCorrespondItem, amount, currency)
			
			if itemsGroupName.casefold() == 'liabilities':
				self.totalLiabilities.changeItemAmount(itemName, amount, currency)
		
		try:
			f.execWithException(self.inputCurrent, func, ValueError, IndexError, KeyError)
		except (ValueError, IndexError, KeyError):
			return

	def showTotal(self):
		if self.totalLiabilities:
			print(self.totalLiabilities)
		else:
			print('"Total Savings" record must be created before being shown.')
	
	def showCurrent(self):
		if self.currentMonth:
			print(self.currentMonth)
		else:
			print('"Current Month" record must be created before being shown.')

	def getItemsTypesGroup(self, itemsTypesGroup):
		return self.itemsTypesCollection[itemsTypesGroup.casefold()]

		



if __name__ == '__main__':
	r = Runtime()
	r.run()