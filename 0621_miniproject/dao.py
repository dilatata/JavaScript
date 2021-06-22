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

    # def selectone(self, ownerid):

    #     data = ''
    #     try:
    #         conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
    #         cur = conn.cursor()

    #         try:
    #             cur.execute("select * from dogowner where ownerid :=ownerid", ownerid=ownerid)
    #             row = cur.fetchone()
    #             data = '{"email":"' + row[1] + '", "ownername":"' + row[2] + '", "password":"' + row[3] + '", "address":"' + row[4] + '", "phoneno":' + str(row[5])+'}'

    #         except Exception as e:
    #             print(e)

    #     except Exception as e:
    #         print(e)

    #     finally:
    #         cur.close()
    #         conn.close()

    #     return data






    def login(self, dto):
        data = ''
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()
            print("-----test")
            try:
                cur.execute("select ownerid, password from dogowner where ownerid=:ownerid and password=:password", \
                    ownerid=dto.getOwnerid(), password=dto.getPassword()) 
                print('-----2-----')
                row = cur.fetchone()
                # print(row)
                data = '{"ownerid":' + '"'+row[0]+'"}'
                data2 = '{"password":' + '"'+row[1]+'"}'
                print(data)
                print(data2)


            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data
    


if __name__ == "__main__":

    dao = InfoDAO()
    dto = DogOwnerDTO('s12un1234', 'jasun112208@nave2sar.com', 'jaes','a4s22d', 'qw2e123', 10793721280)
    dao.login(dto)
    # dao.insertjoin(dto)
    # dto = DogOwnerDTO('sun1234')
    # dao.login(dto)
