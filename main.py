from month import Month




def communicate():
	global action
	action = input('Say what to do ("q" - quit): ')
	
commands = {'new_total': newTotal, 'new_month': newMonth, 
			'input_total': inputTotal, 'input_current': inputCurrent, 
			'show_total': showTotal, 'show_current': showCurrent, 'q': quit}

if __name__ == '__main__':
	communicate()
	print(action)