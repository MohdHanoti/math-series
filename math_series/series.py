def fibonacci(n):
    '''
    This function takes the number (positive int) as input and should output the nth value in the fibonacci series   
    '''
    if type(n)!=int or n<0:
        return "you have to enter positive int value"
  
    else:
        return sum_series(n)    
                 
    
def lucas(n):
    '''
    This function takes the number (positive int) as input and should output the nth value in the lucas series   
    '''
    if type(n)!=int or n<0:
        return "you have to enter positive int value"
    else:
        return sum_series(n,2,1)

def sum_series(n,x=0,y=1):
     '''
     This function takes the number (positive int) as input and should output the nth value in costum series
     if the user did not send a value of the first two numbers (the optional params x & y), 0 and 1 will take place and this will be fibonacci series
     if the user send any other two numbers the series will be deferent and will be costomized like if we send 2 and 1 it will be lucas series
     and a different one if we send differnt values.    
     '''
     if type(n)!=int or n<0:
        return "you have to enter positive int value"
     else:
        
        for i in range(0,n):
            nth=x+y        # make the new number is sum of the previous 2
            x=y            # make the first number = the second one
            y=nth          # make the secound = the new number 
        return x    

        
