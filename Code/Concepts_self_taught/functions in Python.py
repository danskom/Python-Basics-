#functions in Python

def my_function():
    print("this is a fucntion")

my_function()

def my_fucntion_2(parameter):
    print(parameter + "...")

my_fucntion_2("this is an arguement")

#paramters are at the start of an arguement
#arguements are passed the function when it's called

def my_function_3(parameter_1,parameter_2):
    print(parameter_1 + parameter_2)

my_function_3("idiot","idiot")

# * before arguements denotes that the total number of arguements is unknown
#-> arbitary argueents 

def my_function4(*parameter):
    print('this is a function' + parameter[2])

my_function4('scalar','vector',' matirix','tensor')

