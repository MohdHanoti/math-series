def fibonacci(n):
    if type(n)!=int or n<0:
        return "you have to enter positive int value"
  
    else:
        return sum_series(n)    
                 
    
def lucas(n):
    if type(n)!=int or n<0:
        return "you have to enter positive int value"
    else:
        return sum_series(n,2,1)

def sum_series(n,x=0,y=1):
     if type(n)!=int or n<0:
        return "you have to enter positive int value"
     else:
        
        for i in range(0,n):
            nth=x+y        # make the new number is sum of the previous 2
            x=y            # make the first number = the second one
            y=nth          # make the secound = the new number 
        return x    

        
