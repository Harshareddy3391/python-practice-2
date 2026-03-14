
def zero_check(func):

        def inner(a,b):
            if b == 0:
                    print("zero")
            else:
                    return func(a,b)     
        return inner



@zero_check
def division(a,b):
    print(a/b) 


division(5,2)
division(5,0)