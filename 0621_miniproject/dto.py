class CustDTO:
    def __init__(self, newcustidm, newemail, newname, newaddress, newphoneno, newpw):
        self.custid = newcustidm
        self.email = newemail
        self.name = newname
        self.address = newaddress
        self.phoneno = newphoneno
        self.pw = newpw
    
    def getCustid(self):
        return self.custid

    def getEmail(self):
        return self.email

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhoneno(self):
        return self.phoneno

    def getPw(self):
        return self.pw