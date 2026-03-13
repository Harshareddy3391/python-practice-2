val=int(input("enter num :"))

"""

for i in range(n+1):
    if(i%3 == 0 and i%5 == 0):
        print("FIZZBUZ")
    elif(i%3 == 0):
        print("fizz")
    elif(i%5 == 0):
        print("buzz")   
     
    else:

        print(i)"""



for n in range(1,val+1):
    if (n%3 == 0):
        print("FIZZ")
    elif(n%5 == 0):
        print("BUZZ")
    elif(n%5 == 0 and n%3 == 0):
        print("fizzbuzz")
    else:
        print(n)            