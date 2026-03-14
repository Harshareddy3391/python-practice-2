"""
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
division(5,0)"""


"""

def div(a,b):
   print( a/b )

   return div

    



div(4,2)"""


"""

def second(fun):


    def inner():
        print("good mornig")
        fun()
        print("byee!!")
        
    return inner    


@second
def first():
    
    print("hii harsha")



first()     

 """


def sec(fun):
    def inner():

        fun()
        print("good morning")
        
    return inner




@sec
def first():


    print("hi mama")



#first()    

sec(first)



 