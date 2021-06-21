import cx_Oracle
from dto import *

#gurune/jungguru

class InfoDAO:
    def join(self, DogOwnderDTO):
        conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
        cur = conn.cursor()

        try: #insert into Customer values (newcustid, newemail, newname, newaddress, newphoneno, newpw)
            cur.execcute("insert into DogOwner values (:ownerid, :email, :ownername, :password, :address, :phoneno, :accumpoints)",\
                ownerid=DogOwnderDTO.getOwnerid(), email=DogOwnderDTO.getEmail(), ownername=DogOwnderDTO.getOwnername(),  pw=DogOwnderDTO.getPassword(), address=DogOwnderDTO.getAddress(), phoneno=DogOwnderDTO.getPhoneno(), accpoint=DogOwnderDTO.getAccumpoints())
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def login(self, DogOwnderDTO):
        data = ''
        try:
            conn = cx_Oracle.connect(user="gurune", password="jungguru", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select ownerid, password from DogOwner where id=:v and pw=:p", \
                    v=DogOwnderDTO.getOwnerid(), p=DogOwnderDTO.getPassword()) 
                row = cur.fetchone() 
                data = '{"ownerid":"' + str(row[0]) + '", "password":' + row[1]+ '}'

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data
    


# if __name__ == "__main__":
    # dao = InfoDA0()
