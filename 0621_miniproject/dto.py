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
    
    def __str__(self):
        return 'Id : ' + self.custid + '- Email : ' + self.name + '- Phone : ' + self.phone + '- password : ' + self.pw
    
    

class RoomDTO:
    def __init__(self, newroomno, newroomname, newroomtype, newroomdesc):
        self.roomno = newroomno
        self.roomname = newroomname
        self.roomtype = newroomtype
        self.roomdesc = newroomdesc

    def getRoomno(self):
        return self.newroomno

    def getRoomname(self):
        return self.newroomname

    def getRoomtype(self):
        return self.newroomtype

    def getRoomdesc(self):
        return self.newroomdesc

    def __str__(self):
        return '방 번호 : ' + self.roomno + '- 방 이름 : ' + self.roomname + '- 방 종류 : ' + self.roomtype + '- 방 설명 : ' + self.roomdesc
