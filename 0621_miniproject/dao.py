from logging import exception
import cx_Oracle
from dto import *
import bcrypt

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

# ---------------------------------------------------------------------

    def login1(self, dto):
        data = ''
        try:
            conn = cx_Oracle.connect(
                user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select owenerid, password from dogowner where ownerid=:ownerid and password=:password",
                            ownerid=dto.getOwnerid(), password=dto.getPassword())
                row = cur.fetchone()
                print("--------")
                data = '{"password":' + '"'+row[0]+'"}'
                data = row[1]

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



# if __name__ == "__main__":
#     dao = InfoDAO()
#     # dto = DogOwnerDTO('abc', 'abc@naver.com', 'juyoung', '1234', 'youngin', 8212312345)
#     # dao.login(dto)
#     dto = BookDTO(0, 'cdf' , 1, '21/03/21', '21/04/12', '21/04/13', 0, 'bonggu', 7, 'shiba', 60000)
#     dao.insertbook2(dto)

