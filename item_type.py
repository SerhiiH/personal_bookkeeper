class ItemType:
	def __init__(self, name, correspondItem, *currencies):
		self._name = name.casefold()
		self._correspondItem = correspondItem.casefold()
		self._currencies = [curr.casefold() for curr in currencies]
		
	@property
	def name(self):
		return self._name
		
	def changeName(self, name):
		self._name = name.casefold()
				
	@property
	def correspondItem(self):
		return self._correspondItem
		
	def changeCorrespondItem(self, newCorrespondItem):
		self.correspondItem = newCorrespondItem.casefold()
		
	@property
	def currency(self):
		return self._currencies
		
	def changeCurrency(self, *newCurrency):
		self.currencies = [curr.casefold() for curr in newCurrency]