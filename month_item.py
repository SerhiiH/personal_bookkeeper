from record import Record

class MonthItem:
	def __init__(self, name):
		self.name = name
		self.itemsTypes = {}
		self.itemsSources = {}
		
	def __repr__(self):
		string = ''.join(['{0} (source: {1}):\n'.format(item.capitalize(), self.itemsSources[item].capitalize()) 
				+ str(rec) for item, rec in self.itemsTypes.items()])
		return self.name.capitalize().center(38, '-') + '\n' + string + '\n'
		
	def addItem(self, name, *currencies, source = 'wallet'):
		name = name.lower()
		currencies = [curr.lower() for curr in currencies]
		source = source.lower()
		self.itemsTypes[name] = Record(name, currencies)
		self.itemsSources[name] = source
		
	def deleteItem(self, item):
		try:
			del self.itemsTypes[item.lower()]
			del self.itemsSources[item.lower()]
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		
	def changeItemAmount(self, item, currency, amount, sign = 1):
		try:
			self.itemsTypes[item.lower()].changeAmount(currency.lower(), float(amount), sign)
		except KeyError:
			print('ERROR!!! Incorrect Item name.')
			return
		except ValueError:
			print('ERROR!!! Incorrect amount format.')
			return
	
	def getItemSource(self, item):
		return self.itemsSources[item.lower()]
		
		
if __name__ == '__main__':
	mi = MonthItem('Expenses')
	mi.addItem('Rent', 'uah')
	mi.addItem('TRAVELLING', 'uah', 'usd', 'eur', source = 'travelling')
	mi.addItem('FooD', 'uah')
	print(mi)
	
	mi.changeItemAmount('rent', 'uah', 1000)
	print(mi)
	mi.changeItemAmount('rent', 'uah', 500, -1)
	print(mi)
	mi.changeItemAmount('rent', 'usd', 500)
	print(mi)
	mi.changeItemAmount('bikes', 'uah', 500)
	print(mi)
	mi.changeItemAmount('rent', 'uah', '541-')
	print(mi)
	
	mi.deleteItem('rent')
	print(mi)
	