#this is a recursive function

def recursive_function(parameter_1):
    if(parameter_1 > 0):
        result = parameter_1 + recursive_function(parameter_1 - 25 )
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
recursive_function(50)
