#For loop examples 

array = [1,2,3,4,5,6,7,8,9,10]

def odd_times_2(array):

    x = []
    
    for i in array:
        
        if i%(2) != 0:
            
            i = i*2
            
            x.append(i)

            print(x)


odd_times_2(array)

def count_odd(array):
    count = 0
    
    y = []
    
    for i in array:
        
        if i%2 != 0:
            
            count += 1

            y.append(count)

    z = [y[-1]]

    print(z)
    

count_odd(array)             