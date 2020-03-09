	# <QUESTION 1>

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

	# <EXAMPLES>

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False

	# <HINT>

	# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
	input =input.lower()
	xx=len(input)
	print(xx)
	if input[(xx-1)]!='y' and input[(xx-2)]!='p':
		return False
	#else:
		#return False

endsPy('ssxxpy')