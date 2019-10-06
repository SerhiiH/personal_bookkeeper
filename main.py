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
	
	if len(args) < 3:
		print('Not full input')
		return
		
	savingsItem = args[0]
	savingsCurrency = args[1]
	savingsAmount = args[2]
	
	try:
		savingsAmount = float(savingsAmount)
	except ValueError:
		print('ERROR!!! Incorrect amount format.')
		return
		
	if not savingsItem in Savings.items:
		print('ERROR!!! Incorrect Savings item.')
		return
		
	if not savingsCurrency in Savings.currencies:
		print('ERROR!!! Incorrect currency.')
		return
		
	totalSavings[savingsItem][savingsCurrency] = savingsAmount
	
def inputCurrent(*args):
	global currentMonth
	global totalSavings
	
	if not currentMonth:
		try:
			currentMonth = db['current']
		except KeyError:
			print('"Current Month" record must be created before filling in.')
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
	global db
	db = shelve.open('filedb')	

def closeDB():
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
			'input current': inputCurrent, 'show total': showTotal, 'show current': showCurrent}

if __name__ == '__main__':
	start()
