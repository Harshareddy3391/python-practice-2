nums = [2,7,11,15]
target = 2
"""
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])"""


for i in range(len(nums)):
    for n in range(i+1,len(nums)):
        if nums[i]+nums[n] == target :
            print(i or n)





s="hello"
  

d=s[::-1]

print(d)
    



num=int(input("enter a table :"))
n=int(input("end"))



for j in range(1,n+1,1):
        print(f"{num}*{j}={num*j}")
     