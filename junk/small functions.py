def mysum(*numbers, extra=0):
    ''' unpack list and add extra argument'''
    result = 0
    
    for item in numbers:
        result += item
        
    print(f'{result=}')

mysum(1,2,3)
mysum(*[1,2,3])
mysum(*[1,2,3],2) 

# word length of list, Mix max and average