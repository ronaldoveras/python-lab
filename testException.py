def newTest() :
	try:
		open('logic')
	except Exception, e:
		raise Exception(e)
	finally:
		print 'The end'


try:
	newTest()
except Exception, e:
	print 'Exception handled.'
else:
	pass
finally:
	pass

