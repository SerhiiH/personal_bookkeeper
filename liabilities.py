from items_group import ItemsGroup

class Liabilities(ItemsGroup):
	def __init__(self, itemsTypes):
		ItemsGroup.__init__(self, self.__class__.__name__, itemsTypes)


if __name__ == '__main__':
	pass