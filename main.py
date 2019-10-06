from month import Month
from savings import Savings
import shelve


db = None
totalSavings = None
currentMonth = None

def start():
	openDB()
	communicate()
	closeDB()
		
def prompt(message):
	return input(message)

def processRequest(requestString):
	args = [arg.strip().lower() for arg in requestString.split(',')]
			
	try:
		if len(args) > 1:
			commands[args[0]](*args[1:])
		else:
			commands[args[0]]()
	except KeyError:
		print('ERROR!!! Incorrect command.')
		return
		
def newTotal():
	global totalSavings
	totalSavings = Savings()
		
def newMonth(*args):
	global currentMonth
	
	if not args:
		print('ERROR!!! Month name must be entered.')
		return
		
	if not currentMonth:
		currentMonth = Month(args[0])
	
	if 'current' in db.keys():
		dbCurrentMonth = db['current']
		db[dbCurrentMonth.name] = dbCurrentMonth

def inputTotal(*args):
	global totalSavings
	
	if not totalSavings:
		try:
			totalSavings = db['total']
		except KeyError:
			print('"Total Savings" record must be created before filling in.')
			return
	try:
		savingsItem = args[0]
		savingsCurrency = args[1]
		amount = float(args[2])
		totalSavings[savingsItem][savingsCurrency] = amount
	except (ValueError, IndexError, KeyError):
		print('ERROR!!! Incorrect input.')
		return
	
def inputCurrent(*args):
	global currentMonth
	global totalSavings
	
	if not currentMonth:
		try:
			currentMonth = db['current']
		except KeyError:
			print('"Current Month" record must be created before filling in.')
			return
	
	if not totalSavings:
		try:
			totalSavings = db['total']
		except KeyError:
			print('"Total Savings" record must be created before filling in.')
			return
	
	try:
		monthSection = args[0]
		sectionItem = args[1]
		
		if monthSection in ['expenses', 'incomes']:
			amount = float(args[2])
			currentMonth[monthSection][sectionItem] += amount
			if monthSection == 'expenses':
				currentMonth['savings']['pocket money']['uah'] -= amount
				totalSavings['pocket money']['uah'] -= amount
			else:
				currentMonth['savings']['pocket money']['uah'] += amount
				totalSavings['pocket money']['uah'] += amount
		else:
			targetCurrency = args[2]
			targetAmount = float(args[3])
			source = args[4]
			sourceCurrency = ''
			sourceAmount = 0
			if len(args) > 5:
				sourceCurrency = args[5]
				sourceAmount = float(args[6])
			else:
				sourceCurrency = targetCurrency
				sourceAmount = targetAmount
			currentMonth[monthSection][sectionItem][targetCurrency] += targetAmount
			totalSavings[sectionItem][targetCurrency] += targetAmount
			currentMonth[monthSection][source][sourceCurrency] -= sourceAmount
			totalSavings[source][sourceCurrency] -= sourceAmount
	except (ValueError, IndexError, KeyError):
		print('ERROR!!! Incorrect input.')
		return

def showTotal():
	if totalSavings:
		print(totalSavings)
	else:
		try:
			print(db['total'])
		except KeyError:
			print('"Total Savings" record must be created before being shown.')
	
def showCurrent():
	if currentMonth:
		print(currentMonth)
	else:
		try:
			print(db['current'])
		except KeyError:
			print('"Current Month" record must be created before being shown.')

def openDB():
	print('Starting runtime...')
	global db
	db = shelve.open('filedb')	

def closeDB():
	print('Finishing runtime...')
	if totalSavings:
		db['total'] = totalSavings
	if currentMonth:
		db['current'] = currentMonth
	db.close()	

def communicate():
	request = prompt('Enter the request ("q" - quit): ')
	while request != 'q':
		processRequest(request)
		request = prompt('Enter the record ("q" - quit): ')	

	
commands = {'new total': newTotal, 'new month': newMonth, 'input total': inputTotal, 
			'input month': inputCurrent, 'show total': showTotal, 'show month': showCurrent}

if __name__ == '__main__':
	start()
