arry = [22, 42, 6, 7]




min_val=arry[0]
max_val=arry[0]



for i in arry:
    if i>max_val:
        max_val=i
    if i<min_val:
        min_val=i


print(f"min : {min_val}  max : {max_val}")            