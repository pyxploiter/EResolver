from eresolver import resolver

print "====================> Eresolver <=========================="
print "It helps you to find the suggestions to resolve your errors"
print "==========================================================="
print "Testing..."
print "try to use statement which gives error:"
print "e.g. print 1/0\n"

# def replace():
# 	print "this is my function\n"

try:
	#xyz(test)
	print 1/0
except Exception,e:
	print "Error: "+str(e)
	print "-----------------------------------------------------"
	print "Possible Solutions:-"
	#print resolver(str(e))
	answers = resolver(str(e))
	for x in answers:
		print "-----------------------------------------------------"
		print x

# print json.dumps(response, indent=2, sort_keys=True)
