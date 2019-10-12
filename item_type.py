class ItemType:
	def __init__(self, name, correspondingItem, *currencies):
		self.name = name.casefold()
		correspondingItem = correspondingItem.casefold()
		currencies = [curr.casefold() for curr in currencies]
		
	def getName(self):
		return self.name
		
	def getCorrespondingItem(self):
		return self.correspondingItem
		
	def getCurrencies(self):
		return self.currencies