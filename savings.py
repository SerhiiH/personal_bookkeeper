class Savings:
	types = ['Pocket money', 'Travelling', 'Deposit', 'Interests']
	currencies = ['UAH', 'USD', 'EUR']

	def __init__(self):
		self.savings = {}
		for type in Savings.types:
			if type == 'Travelling':
				self.savings[type] = Record()
			else:
				self.savings[type] = {key: Record(currency = key) for key in Savings.currencies}
		
		
	def __getitem__(self, key):
		return self.savings[key]
	def createSaving(self, type, amount, currency, exchangeRate=1):
		self.savings[type] = Record(amount, currency)
		if currency != 'UAH':
			
		
