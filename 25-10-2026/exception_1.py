inspection_score = 85
total_inspection = 0

print(inspection_score / total_inspection)
# ZeroDivisionError: division by zero

print(inspection_score / str(total_inspection))
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

# try :
#     print(inspection_score / total_inspection)
# except:
#     print("User trying to divide by zero.")



print("Hello")