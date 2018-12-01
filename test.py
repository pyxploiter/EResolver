from eresolver import resolver

print "====================> Eresolver <=========================="
print "It helps you to find the suggestions to resolve your errors"
print "==========================================================="
print "Testing..."
print "try to use module which is not defined:"
print "e.g. replace(test)\n"

# def replace():
# 	print "this is my function\n"

try:
	#xyz(test)
	print replace()
except Exception,e:
	print "Error: "+str(e)
	print "-----------------------------------------------------"
	print "Possible Solutions:-"
	print resolver(str(e))
	# answers = resolver(str(e))
	# for x in answers:
	# 	print "-----------------------------------------------------"
	# 	print x

# print json.dumps(response, indent=2, sort_keys=True)