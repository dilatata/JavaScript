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
        return 'Id : ' + self.custid + '- Email : ' + self.email + '- name: ' + self.name + - '- address' + self.address + '- Phone : ' + self.phoneno + '- password : ' + self.pw
    
    

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
        return 'room no: ' + self.roomno + '- room name : ' + self.roomname + '- room type : ' + self.roomtype + '- room desc : ' + self.roomdesc





        
class BookDTO:
    def __init__(self, newbookingid, newcustid, newroomno, newbdate, newchindate, newchoutdate, newcancel, newprice):
        self.bookingid = newbookingid
        self.custid = newcustid
        self.roomno = newroomno
        self.bdate = newbdate
        self.chindate = newchindate
        self.choutdate = newchoutdate
        self.cancel = newcancel
        self.price = newprice

    def getBookingid(self):
        return self.bookingid

    def getCustid(self):
        return self.custid

    def Roomno(self):
        return self.roomno

    def getBdate(self):
        return self.bdate

    def getChindate(self):
        return self.chindate

    def getChoutdate(self):
        return self.choutdate

    def getCancle(self):
        return self.cancel
    
    def getPrice(self):
        return self.price

    def __str__(self):
        return 'booking id: ' + self.bookingid + '- room custid : ' + self.custid + '- room no : ' + self.roomno + '- bookingdate : ' + self.bdate + '- check in date: ' + self.chindate + '- check out date : ' + self.choutdate + '- cancelation : ' + self.cancel + '- Total Price : ' + self.cancel


    