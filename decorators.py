def pretty_sumab(func):                                                                                     
    def inner(a,c):                                                                                         
        print(str(a) + " + " + str(c) + " is ", end="")                                                     
        return func(a,c)                                                                                    
                                                                                                            
    return inner                                                                                            
                                                                                                            
@pretty_sumab                                                                                               
def sumab(a,b):                                                                                             
    summed = a + b                                                                                          
    print(summed)                                                                                      
                                                                                                            
if __name__ == "__main__":                                                                                  
    sumab(5,3)          