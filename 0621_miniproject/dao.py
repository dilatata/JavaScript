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

        # insert into dogowner values ('lee', 'jae', 'seon', 'love', 'js', 79371280, 25);
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
                # print("-----test")
                # data = '{"ownerid":' + '"'+row[0]+'", "password":' + '"'+row[1]+'"}'
                # data = '{"password":' + '"'+row[0]+'"}'
                data = row[1]
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
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()

            try:  # insert into Booking values(10, 'qwe' , 2, '21/06/02', '21/06/03', '21/06/06', 1, 'coco', 6, 'bichon', 90000)
                cur.execute("insert into booking values (:bookingid, :ownerid, :roomno, :bookingdate, :chindate, :choutdate, :cancel, :dogname, :dogsize, :dogbreed, :price)",
                            bookingid=dto.getBookingid(), ownerid=dto.getOwnerid(), roomno=dto.getRoomno(), bookingdate=dto.getBookingdate(), chindate=dto.getCheckindate(), choutdate=dto.getCheckoutdate(),
                            cancel=dto.getCancellation(), dogname=dto.getDogname(), dogsize=dto.getDogsize(), dogbreed=dto.getDogBreed(), price=dto.getTotalprice())
                conn.commit()
                
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()


if __name__ == "__main__":
    dao = InfoDAO()
    # dto = DogOwnerDTO('abc', 'abc@naver.com', 'juyoung', '1234', 'youngin', 8212312345)
    # dao.pwcheck(dto)
    # dao.login(dto)
    # dao.login1(dto)
    # dao.insertjoin(dto)
    # dto = DogOwnerDTO('sun1234')
    # dao.login(dto)
    # dao.inser(dto)
    # dto = BookDTO(23, 'abc' , 6, '21/06/05', '21/06/06', '21/06/08', 0, 'gru', 9, 'mix', 80000)
    # dao.insertbook(dto)
    dto = DogDTO('gru', 'abc', 10, 'mix')
    dao.findinfo(dto)
