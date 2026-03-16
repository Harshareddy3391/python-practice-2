#constructor is a special method which is called automatically at the time of object creation

class student:
    def __int__(self):
        print("constructor is called")


s=student()
s.__int__()



class con: 
    def namee(self,name,lname):
        self.name =name
        self.lname =lname

        print(self.name,self.lname)


s=con()
s.namee("haes","affs")
s.namee("var","thota")
 
