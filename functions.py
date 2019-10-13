def execWithException(encloseScopeName, func, *exceptions):
	try:
		func()
	except excpetions as err:
		print('ERROR in {0}!!! Incorrect input.'.format(encloseScopeName))
		
		