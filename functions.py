def execWithException(encloseScopeName, func, *exceptions):
	try:
		func()
	except exceptions as err:
		print('ERROR in {0}!!! Incorrect input.'.format(encloseScopeName))
		
		