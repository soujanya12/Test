import traceback
try:
	a=1/0
except Exception as e:
	print(e)
	#tb = traceback.format_exc()
	#print(tb)
	#traceback.print_exc()

"""exception message"""
#division by zero

"""traceback.print_exc() output"""
# Traceback (most recent call last):
#   File "C:/Users/Sgangula2/Desktop/Test/message_log.py", line 3, in <module>
#     a=1/0
# ZeroDivisionError: division by zero

"""traceback.format_exc() output"""
#Traceback (most recent call last):
# File "C:/Users/Sgangula2/Desktop/Test/message_log.py", line 3, in <module>
#    a=1/0
#ZeroDivisionError: division by zero

