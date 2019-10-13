import inspect

def execWithException(encloseScope, func, *exceptions):
	try:
		func()
	except exceptions as err:
		print('ERROR in {0}!!! Incorrect input.'.format(inspect.getmodule(encloseScope).__name__))
		
		