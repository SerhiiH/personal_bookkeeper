from record import Record

class MonthItem:
	def __init__(self, name):
		self.name = name
		self.items = {}
		self.itemsSources = {}
		
	def __repr__(self):
		string = ''.join([str(rec) for rec in self.items.values()])
		return self.name.capitalize().center(30, '-') + '\n' + string + '\n'
		
	def addItem(self, name, currencies = ['uah'], source = 'wallet'):
		name = name.lower()
		self.items[name] = Record(name, currencies)
		self.itemsSources[name] = source.lower()
		
		
		
		
if __name__ == '__main__':
	mi = MonthItem('Expenses')
	mi.addItem('Rent', ['uah'])
	mi.addItem('TRAVELLING', ['uah', 'usd', 'eur'])
	mi.addItem('FooD', ['uah',])
	print(mi)