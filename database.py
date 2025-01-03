import sqlite3

class Database:
    def __init__(self) :
        self.conn = sqlite3.connect('splitwise clone.db')
        self.cur = self.conn.cursor()

    def user_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                        name TEXT,
                        email TEXT,
                        pass TEXT
        )""")   
        self.conn.commit()
        #self.conn.close() I don't know about this

    def insert_user(self,user_name,user_email,user_password):
    
        query="INSERT INTO users(name, email, pass) VALUES (?, ?, ?)"
        self.cur.execute(query,(user_name, user_email, user_password))
        self.conn.commit()
        query=None
        print('command executed succesfully')

    def find_user(self,user_name,user_password) -> bool:
        self.cur.execute("SELECT * FROM users")
        #print(user_name)
        #print(user_password)
        users_list=self.cur.fetchall()
        print(users_list)
        if any((user_name,user_password) == u[:2] for u in users_list ):
            print('user name found')
            return True
        else:
            return False
    
    def show_all(self):
        self.cur.execute("SELECT * from users")
        users_list=self.cur.fetchall()
        print(users_list)




