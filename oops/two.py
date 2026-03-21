class Bank:
    min_bal=1000

    def account_open(self):
        print("account open")

    def diposit(self):
        print("diposit")    


a1=Bank()

b=a1


#print(a1.min_bal)

a1.account_open()
print(b.min_bal)