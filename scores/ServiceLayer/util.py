'''
Determine if parameter 1 is a subclass of the parameter 2 and if both of them are exception subclasses, 
if true it raises the error of the first-class, else it raises a single error
'''
def raiseParentExceptionIfApply(error : "class object of exception type",parent : "class object of exception type")->"raise first-class when match, else raise a single error":
    try:
        if issubclass(type(error), parent) : 
            raise error
    except:
        raise