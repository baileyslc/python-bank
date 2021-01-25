# MinBalance runs the program and accepts input from the end user to create respective class objects and print details.
# Add a method to deposit and withdrawal transaction based on the end user input.

class Bank:
    # parameterized constructor for bank class
    def __init__(self, i, ba, br, lo):
        self.IFSC_Code = i
        self.bankname = ba
        self.branchname = br
        self.loc = lo

    def getAccountInfo(self):
        return self.IFSC_Code, self.bankname, self.branchname, self.loc

licia = Bank(1234, "Bank of Arizona", "Chandler Fashion", "Chandler, AZ 85226")

print(licia.branchname)
print(licia.getAccountInfo())