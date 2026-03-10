#string_val="hello world"

#print(string_val.count('o''e''i''u''a'))

#print(type(string_val))


#ovl="aeiou"
"""
d=0

for i in string_val:
    if i in ovl:
      d += 1

print(d)"""





#by using function


def ovel_count(a):
   
   count=0

   st=str(a)
   for i in st:
     if i.lower() in "aioue":
            count+=1
   return print(count)
   
ovel_count("harsha")

     
     