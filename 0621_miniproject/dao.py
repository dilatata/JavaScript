from logging import exception
import cx_Oracle
from dto import *

#gurune/jungguru

class InfoDAO:



    def insertjoin(self, dto):
        conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
        cur = conn.cursor()
        print("-------test1")

        try: # insert into dogowner values ('lee', 'jae', 'seon', 'love', 'js', 79371280, 25);
            cur.execute("insert into dogowner values (:ownerid, :email, :ownername, :password, :address, :phoneno)",\
                ownerid=dto.getOwnerid(), email=dto.getEmail(), ownername=dto.getOwnername(), password=dto.getPassword(), address=dto.getAddress(), phoneno=dto.getPhoneno())
            print("--------test")
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()






    def login(self, dto):
        data = ''
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select ownerid, password from dogowner") 
                row = cur.fetchone()
                # print(row)
                # print("-----test")
                # data = '{"ownerid":' + '"'+row[0]+'", "password":' + '"'+row[1]+'"}'
                # data = '{"ownerid":' + '"'+row[0]+'"}'
                # data = '{"password":' + '"'+row[1]+'"}'
                data = row[0]
                # print(data)


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
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select password from dogowner") 
                row = cur.fetchone()
                # print("-----test")
                # data = '{"ownerid":' + '"'+row[0]+'", "password":' + '"'+row[1]+'"}'
                # data = '{"password":' + '"'+row[0]+'"}'
                data = row[0]
                # print(data)


            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data



def insertbook(self, dto):
        conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
        cur = conn.cursor()
        print("-------test1")

        try:    # insert into booking valuew (:bookingid, :oenwerid, roomno, bookingdate, checkindate, checkoutdate, cancellation, dogname, dogsize, dogbreed, totalprice)
            cur.execute("insert into booking values (:bookingid, :ownerid, :roomno, bookingdate, checkindate, checkoutdate, cancellation, dogname, dogsize, dogbreed)", \
                bookingid=dto.getBookingid(), ownerid=dto.getOwnerid(), roomno=dto.getRoomno(), bookingdate=dto.getBookingdate(), checkindate=dto.getCheckindate(), checkoutdate=dto.getCheckoutdate(), cancellation=dto.getCancellation(), dogname=dto.getDogname(), dogsize=dto.getDogsize(), dogbreed=dto.getDogbreed(), totlaprice=dto.getTotalprice())
            print("--------test")
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()





if __name__ == "__main__":

    dao = InfoDAO()
    # dto = DogOwnerDTO('tester', 'jasun1208@naver.com', '이재선','k15687', '관악구', 10793721280)
    # dao.login(dto)
    # dao.login1(dto)
    # dao.insertjoin(dto)
    # dto = DogOwnerDTO('sun1234')
    # dao.login(dto)