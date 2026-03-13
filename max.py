arry=[2,4,3,3,6,8]

min_val=arry[0]
max_val=arry[0]



for index,i in enumerate(arry):
    if ( i > max_val):
        max_val=i
    elif(i<min_val):
        min_val=i




print("min val : " ,min_val )
print("max val : " ,max_val )