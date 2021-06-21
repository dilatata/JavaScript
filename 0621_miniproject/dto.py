class DogOwnderDTO:

    def __init__(self, newownerid, newemail, newownername, newaddress, newphoneno, newpassword, newaccumpoints):
        self.ownerid = newownerid
        self.email = newemail
        self.ownername = newownername
        self.address = newaddress
        self.phoneno = newphoneno
        self.password = newpassword
        self.accumpoints = newaccumpoints

    def getOwnerid(self):
        return self.ownerid

    def getEmail(self):
        return self.email

    def getOwnername(self):
        return self.ownername

    def getPhoneno(self):
        return self.phoneno

    def getPassword(self):
        return self.password
    
    def getAccumpoints(self):
        return self.accumpoints

    def __str__(self):
        return 'Id : ' + self.ownerid + '- Email : ' + self.email + '- owner name : ' + self.ownername + '- adress : ' + self.address + '- Phoneno : ' + self.phoneno + '- password : ' + self.password + '- accumpoints : ' + self.accumpoints
    



class RoomDTO:
    def __init__(self, newroomno, newroomname, newroomtype, newroomdesc):
        self.roomno = newroomno
        self.roomname = newroomname
        self.roomtype = newroomtype
        self.roomdesc = newroomdesc

    def getRoomno(self):
        return self.roomno

    def getRoomname(self):
        return self.roomname

    def getRoomtype(self):
        return self.roomtype

    def getRoomdesc(self):
        return self.roomdesc

    def __str__(self):
        return 'room no : ' + self.roomno + '- room name : ' + self.roomname + '- room type : ' + self.roomtype + '- room desc : ' + self.roomdesc




class BookDTO:
    def __init__(self, newbookingid, newownerid, newroomno, newbookingdate, newchindate, newchoutdate, newcancel,newdogname, newdogsize, newdogbreed ,newprice):
        self.bookingid = newbookingid
        self.ownerid = newownerid
        self.roomno = newroomno
        self.bookingdate = newbookingdate
        self.checkindate = newchindate
        self.checkoutdate = newchoutdate
        self.cancellation = newcancel
        self.dogname = newdogname
        self.dogsize = newdogsize
        self.dogbreed = newdogbreed
        self.totalprice = newprice

    def getBookingid(self):
        return self.bookingid

    def getOwnerid(self):
        return self.ownerid

    def Roomno(self):
        return self.roomno

    def getBookingdate(self):
        return self.bookingdate

    def getCheckindate(self):
        return self.checkindate

    def getCheckoutdate(self):
        return self.checkoutdate    

    def getCancellation(self):
        return self.cancellation
    
    def getDogname(self):
        return self.dogname
    
    def getDogsize(self):
        return self.dogsize
    
    def getDogBreed(self):
        return self.dogbreed
        
    def getTotalprice(self):
        return self.totalprice

    def __str__(self):
        return 'booking id: ' + self.bookingid + '- room custid : ' + self.ownerid + '- room no : ' + self.roomno + '- bookingdate : ' + self.bookingdate + '- check in date: ' + self.checkindate + '- check out date : ' + self.checkoutdate + '- cancelation : ' + self.cancellation \
            + '- dog name : ' + self.dogname + '- dog size : ' + self.dogsize + '- dog breed : ' + self.dogbreed + '- Total Price : ' + self.totalprice


class DogDTO:

    def __init__(self, newdogname, newownername, newdogsize, newdogbreed):
        
        self.dogname = newdogname
        self.ownername = newownername
        self.dogsize = newdogsize
        self.dogbreed = newdogbreed

    def getDogname(self):
        return self.dogname
    
    def getOwnername(self):
        return self.ownername

    def getDogsize(self):
        return self.dogsize

    def getDogbreed(self):
        return self.dogbreed

    def __str__(self):
        return 'dog name : ' + self.dogname + '- owner name : ' + self.ownername + '- dog size : ' + self.dogsize + '- dog breed : ' + self.dogbreed


class RoomTypeDTO:
    def __init__(self, newroomtype, newlength, newwidth, newheight, newroomtypedesc):

        self.roomtype = newroomtype
        self.length = newlength
        self.width = newwidth
        self.height = newheight
        self.roomtypedesc = newroomtypedesc

    def getRoomtype(self):
        return self.roomtype

    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getRoomtypedesc(self):
        return self.roomtypedesc

    def __str__(self):
        return 'room type : ' + self.roomtype + '- length : ' + self.length + '- width : ' + self.width + '- height : ' + self.height + ' - room type desc : ' + self.roomtypedesc

