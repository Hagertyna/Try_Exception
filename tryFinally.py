#try...finally
try:
    print("I am try block")
    raise TypeError
    
except:
    print("I am except block")
finally:
    print("I am finally block")
