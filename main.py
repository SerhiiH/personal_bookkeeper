import pickle
import runtime as rt


def run():
	try: 
		with open('file_db.pkl', 'rb')as fileDB:
			runtime = pickle.load(fileDB)
			fileDB.close()
	except FileNotFoundError:
		runtime = rt.Runtime()
	finally:
		try:
			runtime.run()
		finally:
			with open('file_db.pkl', 'wb') as fileDB:
				pickle.dump(runtime, fileDB)
		

run()