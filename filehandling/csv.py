import csv

d = open("MOCK_DATA.csv", 'r')
a = csv.reader(d)
print(type(a))

for i in a:
    print(i)

d.close()