from month import Month
from liabilities import Liabilities
from item_type import ItemType
import functions as f
import pickle
from functools import reduce
from datetime import datetime


class Runtime:
	def __init__(self):
		self.defaultItemsTypesGroups = {
			'expenses':  [ItemType('Rent', 'Wallet', 'UAH'), ItemType('Food', 'Wallet', 'UAH'), ItemType('Pocket money', 'Wallet', 'UAH'), 
				ItemType('Travelling', 'Travelling', 'UAH')], 
			'incomes': [ItemType('Serhii', 'Wallet', 'UAH'), ItemType('Alona', 'Wallet', 'UAH')],
			'liabilities': [ItemType('Wallet', '', 'UAH', 'USD', 'EUR'), ItemType('Travelling', '', 'UAH', 'USD', 'EUR'), ItemType('Deposit', '', 'UAH', 'USD', 'EUR')]
		}
		self.currentMonth = None
		self.totalLiab = None
		self.monthHistory = None
		self.commands = {'new total': self.newTotal, 'new month': self.newMonth, 'input total': self.inputTotal, 
			'input month': self.inputCurrent, 'show total': self.showTotal, 'show month': self.showCurrent,
			'add item': self.addItem}

	def run(self):
		self.initialize()
		try:
			self.communicate()
		finally:
			self.finish()
	
	def initialize(self):
		self.initBasicItemsTypesGroups()
		self.initTotalLiabs()
		self.initCurrentMonth()
		self.initMonthHistory()

	def initBasicItemsTypesGroups(self):
		try:
			with open('database/items_types_groups.pkl', 'rb') as fileDB:
				tmpBasicItemsTypes = pickle.load(fileDB)
		except EOFError:
			with open('database/items_types_groups.pkl', 'wb') as fileDB:
				pickle.dump(self.defaultItemsTypesGroups, fileDB)
				
	def initTotalLiabs(self):
		try:
			with open('database/total.pkl', 'rb') as fileDB:
				self.totalLiab = pickle.load(fileDB)
		except EOFError:
			try:
				self.totalLiab = Liabilities(self.getItemsTypesGroup('liabilities'))
			except EOFError:
				print('ERROR!!! Items types groups are not set')
				return
			
	def initCurrentMonth(self):
		try:
			with open('database/current_month.pkl', 'rb') as fileDB:
				self.currentMonth = pickle.load(fileDB)
		except EOFError:
			print('Current month isn not set')

	def initMonthHistory(self):
		try:
			with open('database/month_history.pkl', 'rb') as fileDB:
				self.monthHistory = pickle.load(fileDB)
		except EOFError:
			self.monthHistory = {}
			
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
			f.execWithException(self.processRequest, func, KeyError, TypeError)
		except (KeyError, TypeError):
			return
		
	def newTotal(self):
		self.totalLiab = Liabilities(self.getItemsTypesGroup('liabilities'))

	def newMonth(self, *args):
		if not args:
			print('ERROR in runtime.py!!! Month name must be entered.')
			return
			
		if len(args) > 1:
			print('ERROR in runtime.py!!! Too many agruments')
			return
			
		if self.currentMonth:
			self.monthHistory[self.currentMonth.name] = self.currentMonth
		
		self.currentMonth = Month(args[0])

	def inputTotal(self, *args):
		def func():
			item = args[0]
			amount = Runtime.reduceAmount(args[1])
			if len(args) == 2:
				currency = 'uah'
			else:
				currency = args[2]
				
			self.totalLiab.changeItemAmount(item, amount, currency)
			
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
			amount = Runtime.reduceAmount(args[2])
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
				self.totalLiab.changeItemAmount(itemCorrespondItem, amount, currency)
			
			if itemsGroupName.casefold() == 'liabilities':
				self.totalLiab.changeItemAmount(itemName, amount, currency)
			
			if len(args) == 3:
				self.logTransaction(*args, currency)
			else:
			self.logTransaction(*args)
			
		try:
			f.execWithException(self.inputCurrent, func, ValueError, IndexError, KeyError)
		except (ValueError, IndexError, KeyError):
			return

	def showTotal(self):
		if self.totalLiab:
			print(self.totalLiab)
		else:
			print('"Total Savings" record must be created before being shown.')
	
	def showCurrent(self):
		if self.currentMonth:
			print(self.currentMonth)
		else:
			print('"Current Month" record must be created before being shown.')

	def getItemsTypesGroup(self, itemsTypesGroupName):
		try:
			with open('database/items_types_groups.pkl', 'rb') as fileDB:
				itemsTypesGroups = pickle.load(fileDB)
		except EOFError:
			print('ERROR!!! Items types groups are not set')
		else:
			return itemsTypesGroups[itemsTypesGroupName.casefold()]

	def addItem(self):
		pass

	def finish(self):
		with open('database/total.pkl', 'wb') as fileDB:
			pickle.dump(self.totalLiab, fileDB)
		with open('database/current_month.pkl', 'wb') as fileDB:
			pickle.dump(self.currentMonth, fileDB)
		with open('database/month_history.pkl', 'wb') as fileDB:
			pickle.dump(self.monthHistory, fileDB)

	@staticmethod
	def reduceAmount(amountString):
		return reduce(lambda x,y: x + y, map(lambda x: float(x), amountString.split()), 0)

	def logTransaction(self, *args):
		with open('database/transactions.txt', 'a') as file:
			file.write('{0:18} | {1:18} | '.format(datetime.today().strftime('%Y %B "%d"'), self.currentMonth.name.capitalize()))
			for arg in args:
				file.write('{0:15} | '.format(arg))
			file.write('\n')

if __name__ == '__main__':
	r = Runtime()
	r.run()