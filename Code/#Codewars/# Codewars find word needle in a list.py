# Codewars find word needle in a list

list_to_filter = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

def filter_function(list_to_filter):
    if 'needle' in list_to_filter:
        x = list_to_filter.index("needle") 
        print('found the needle at position',x)
        print(x) 

    

filter_function(list_to_filter)



