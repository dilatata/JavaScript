import cx_Oracle
from dto import *

#gurune/jungguru

class InfoDAO:



    def join(self, dto):
        conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
        cur = conn.cursor()
        print("-------test1")

        try: # insert into dogowner values ('lee', 'jae', 'seon', 'love', 'js', 79371280, 25);
            cur.execute("insert into dogowner values (:ownerid, :email, :ownername, :password, :address, :phoneno, :accumpoints)",\
                 ownerid=dto.getOwnerid(), email=dto.getEmail(), ownername=dto.getOwnername(), password=dto.getPassword(), address=dto.getAddress(), phoneno=dto.getPhoneno(), accumpoints=dto.getAccumpoints())
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
                cur.execute("select ownerid, password from dogowner where ownerid=:ownerid and password=:password", \
                    owenrid=dto.getOwnerid(), password=dto.getPassword()) 
                row = cur.fetchone() 
                data = '{"ownerid":"' + str(row[0]) + '", "password":' + row[1]+ '}'
                print(data)

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
    dto = DogOwnerDTO('s12un1234', 'jasun112208@nave2sar.com', 'jaes2eo21n','a4s22d', 'qw2e123', 7937212801, 45)
    # dao.join(dto)
    # dto = DogOwnerDTO('sun1234', 'a4s2d')
    # dao.login(dto)
