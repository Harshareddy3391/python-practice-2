"""def fact(val):

    if val == 0 or val == 1:
        return 
    

    return val * fact(val-1)


print(fact(6))"""
"""

n=6

for i in range(n):

    print(i*n-1)"""




n=5

for i in range(n+1,0,-1):

    for j in range(i):
        print("*",end="")


    print()    