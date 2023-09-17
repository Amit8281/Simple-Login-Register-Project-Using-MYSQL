import mysql.connector

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost',user='root',password = '',database = 'my-database')
            self.mycursor = self.conn.cursor()
        except:
            print('some error occured could not connect to database')

        else:
            print('connected to database')

    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
        
    def search(self,email,password):
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))

        data = self.mycursor.fetchall()

        return data




