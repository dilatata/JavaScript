from logging import exception
import cx_Oracle
from dto import *
import bcrypt
import datetime
import json
import collections

# gurune/jungguru


class InfoDAO:

    def insertjoin(self, dto):
        conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
        cur = conn.cursor()
        print("-------test1")

        try:
            cur.execute("insert into dogowner values (:ownerid, :email, :ownername, :password, :address, :phoneno)",
                        ownerid=dto.getOwnerid(), email=dto.getEmail(), ownername=dto.getOwnername(), password=dto.getPassword(), address=dto.getAddress(), phoneno=dto.getPhoneno())
            print("--------test")
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def login(self, ownerid, password):
        data = ''
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select ownername from dogowner where ownerid=:ownerid and password=:password", ownerid=ownerid, password=password) 
                row = cur.fetchone()

                data = '{"ownername":"' + row[0] + '"}'

                return row
                
            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data






    def insertbook(self, dto):
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()

            try:  
                cur.execute("insert into booking (Bookingid, ownerid, roomno, bookingdate, checkindate, checkoutdate, Cancellation, dogname, dogsize, dogbreed, totalprice)\
                     select Booking_seq.nextval,  :ownerid, :roomno, :bookingdate, :checkindate, :checkoutdate, :Cancellation, :dogname, :dogsize, :dogbreed, :totalprice from dual\
                          where not EXISTS (select * from booking where roomno=:roomno and :checkindate between checkindate and checkoutdate or :checkoutdate between checkindate and checkoutdate)",\
                            ownerid=dto.getOwnerid(), roomno=dto.getRoomno(), bookingdate=dto.getBookingdate(), checkindate=dto.getCheckindate(), checkoutdate=dto.getCheckoutdate(), cancellation=dto.getCancellation(), dogname=dto.getDogname(), dogsize=dto.getDogsize(), dogbreed=dto.getDogBreed(), totalprice=dto.getTotalprice())
                conn.commit()
                #ORA-01400: cannot insert NULL into ("GURUNE"."BOOKING"."CHECKINDATE")
            
                
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()



    def selectinfo(slef, ownerid):
        data = []  
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select rownum, bookingid, ownerid, roomno, bookingdate, checkindate, checkoutdate, cancellation, dogname, dogsize, dogbreed, totalprice from \
                    (select * from booking where ownerid=:ownerid and cancellation=0 order by checkindate asc)", ownerid=ownerid)

                rows = cur.fetchall() 
                v = []
                for row in rows:

                    d = collections.OrderedDict()
                    d["rownum"] = row[0]
                    d["bookingid"] = row[1]
                    d["ownerid"] = row[2]
                    d["roomno"] = row[3]
                    d["bookingdate"] = row[4].strftime('%Y-%m-%d')
                    d["checkindate"] = row[5].strftime('%Y-%m-%d')
                    d["ckeckoutdate"] = row[6].strftime('%Y-%m-%d')
                    d["cancellation"] = row[7]
                    d["dogname"] = row[8]
                    d["dogsize"] = row[9]
                    d["dogbreed"] = row[10]
                    d["totalprice"] = row[11]
                    v.append(d)

                data = json.dumps(v, sort_keys=True, default=str, ensure_ascii=False)

            except Exception as e:
                print(e) 
        except Exception as e:
            print(e) 
        finally:
            cur.close() 
            conn.close()

        return data

    def selectroom(slef):
        data = []  
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select rownum, roomno, roomtype, RoomName, RoomPrice, RoomDesc from room")

                rows = cur.fetchall() 
                v = []
                for row in rows:

                    d = collections.OrderedDict()
                    d["rownum"] = row[0]
                    d["roomno"] = row[1]
                    d["roomtype"] = row[2]
                    d["RoomName"] = row[3]
                    d["RoomPrice"] = row[4]
                    d["RoomDesc"] = row[5]
                    v.append(d)

                data = json.dumps(v, sort_keys=True, default=str, ensure_ascii=False)

            except Exception as e:
                print(e) 
        except Exception as e:
            print(e) 
        finally:
            cur.close() 
            conn.close()

        return data



# if __name__ == "__main__":
#     dao = InfoDAO()
#     dao.login("abc","1234")
    # dto = DogOwnerDTO('abc', 'abc@naver.com', 'juyoung', '1234', 'youngin', 8212312345)
    # dao.login(dto)
#     dto = BookDTO(0, 'cdf' , 1, '21/03/21', '21/04/12', '21/04/13', 0, 'bonggu', 7, 'shiba', 60000)
#     dao.insertbook2(dto)
    # dao.selectinfo("qwe")
    # dao.selectroom()