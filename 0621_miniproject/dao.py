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




    def selectinfo(slef, ownerid):
        data = []  
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from booking where ownerid=:ownerid and cancellation=0", ownerid=ownerid) 
                rows = cur.fetchall() 
                # json 포멧으로 가공 : empno/ename/sal key - json 배열
                # 다양한 방법 : 저장하는 순서를 유지하는 구조의 dict 클래스 
                v = []   # v 변수에 python구조의 dict 구조로 저장 -> data 변수로 json 포멧으로 변환
                for row in rows:
                    # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

                    d = collections.OrderedDict()
                    d["bookingid"] = row[0]
                    d["ownerid"] = row[1]
                    d["roomno"] = row[2]
                    d["bookingdate"] = row[3].strftime('%Y-%m-%d')
                    d["checkindate"] = row[4].strftime('%Y-%m-%d')
                    d["ckeckoutdate"] = row[5].strftime('%Y-%m-%d')
                    d["cancellation"] = row[6]
                    d["dogname"] = row[7]
                    d["dogsize"] = row[8]
                    d["dogbreed"] = row[9]
                    d["totalprice"] = row[10]
                    v.append(d)   # 이미 존재하는 list의 마지막 요소로 저장(add)
                    # print(rows)

                data = json.dumps(v, sort_keys=True, default=str, ensure_ascii=False)   # json 포멧으로 자동 변환
                print(data)

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
#     # dto = DogOwnerDTO('abc', 'abc@naver.com', 'juyoung', '1234', 'youngin', 8212312345)
#     # dao.login(dto)
#     dto = BookDTO(0, 'cdf' , 1, '21/03/21', '21/04/12', '21/04/13', 0, 'bonggu', 7, 'shiba', 60000)
#     dao.insertbook2(dto)

