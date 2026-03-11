num=[2,7,11,8]

target=16

"""
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if (num[i]+num[j] == target):
            print(i,j)

            """





for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j] == target:
            print(num[i],num[j])