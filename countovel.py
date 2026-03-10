string_val="hello world"

#print(string_val.count('o''e''i''u''a'))

#print(type(string_val))


ovl="aeiou"

d=0

for i in string_val:
    if i in ovl:
      d += 1

print(d)
     