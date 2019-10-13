import inspect

def execWithException(encloseScope, func, *exceptions):
	try:
		func()
	except exceptions as err:
		print('ERROR: method - \'{0}\', module - \'{1}\'!'.format(encloseScope.__name__, inspect.getmodule(encloseScope).__name__))
		
		