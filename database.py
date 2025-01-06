import sqlite3

class Database:
    def __init__(self) :
        self.conn = sqlite3.connect('splitwise clone.db')
        self.cur = self.conn.cursor()

    def user_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT UNIQUE,
                        pass TEXT,
                        email TEXT UNIQUE
        )""")   
        self.conn.commit()
        #self.conn.close() I don't know about this

    def friends_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS friends(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE,
                        email TEXT
        )""")
        self.conn.commit()
        #self.conn.close()


    def insert_user(self,user_name,user_password,user_email):
    
        query="INSERT INTO users(name, pass, email) VALUES (?, ?, ?)"
        self.cur.execute(query,(user_name, user_password, user_email))
        self.conn.commit()
        
        print('command executed succesfully')

    def insert_friend(self,friend_name, friend_email):
        query="INSERT INTO friends(name, email) VALUES (?, ?)"
        self.cur.execute(query,(friend_name, friend_email))
        self.conn.commit()
        
        print(f'{friend_name} executed succesfully')


    def find_user(self,user_name,user_password) -> bool:                 #this is for login
        self.cur.execute("SELECT * FROM users")
        #print(user_name)
        #print(user_password)
        users_list=self.cur.fetchall()
        print(users_list)
        if any((user_name,user_password) == u[1:3] for u in users_list ):
            print('user name found')
            return True
        else:
            print('nothing found')
            return False
    
    def show_users(self):                                                   #this just shows list of users
        self.cur.execute("SELECT * FROM users")
        users_list=self.cur.fetchall()
        print(users_list)

    def show_friends(self):
        self.cur.execute("SELECT * FROM friends ")
        friends_list=self.cur.fetchall()
        friends_names=[friend for friend in friends_list]
        return friends_names

    
    def each_user_table(self,user_name):
        self.cur.execute("PRAGMA foreign_keys = ON")
        query=f"""CREATE TABLE IF NOT EXISTS {user_name}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            other_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            currency TEXT,
            description TEXT,
            date TEXT DEFAULT CURRENT_TIMESTAMP
            )"""

        self.cur.execute(query)
        self.conn.commit()
        #self.conn.close()
    
    def each_friend_table(self,friend_name):
        
        query=f"""CREATE TABLE IF NOT EXISTS {friend_name}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            currency TEXT,
            description TEXT,
            date TEXT DEFAULT CURRENT_TIMESTAMP
            )"""
        self.cur.execute(query)
        self.conn.commit()
        #self.conn.close()

    def find_friend_id(self,friend_name):
        self.cur.execute('SELECT id FROM friends where name=?',(friend_name,))
        friend_id=self.cur.fetchone()
        #self.conn.close()
        return friend_id[0] if friend_id else None 

    def find_user_id(self, user_name):
        self.cur.execute('SELECT id FROM users where name=?',(user_name,))
        user_id=self.cur.fetchone()
        #self.conn.close()
        return user_id[0] if user_id else None 


    
    def others_insert(self,other_name,share,currency,time,desc,user_name):
        id_other=self.find_friend_id(other_name)
        id_user=self.find_user_id(user_name)
        query=f"INSERT INTO {other_name} (user_id, amount, currency,description, date) VALUES (?,?,?,?,?)"
        self.cur.execute(query,(id_user,share,currency,desc,time))
        self.conn.commit()
        #self.conn.close()


    def each_insert(self,user_name,money,currency,time,desc,friend_name):

        id_friend=self.find_friend_id(friend_name)
        query=f"INSERT INTO {user_name} (other_id, amount, currency, description, date) VALUES (?,?,?,?,?)"
        self.cur.execute(query,(id_friend,money,currency,desc,time))
        self.conn.commit()
        #self.conn.close()

    def show_expense(self,user_name):
        query=f"SELECT * FROM {user_name}"
        expense_list=self.cur.fetchall()
        return expense_list


    def groups_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS GROUPS(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         group_name TEXT UNIQUE
                         )""")
        self.conn.commit()

    def insert_group(self,group_name_input):
        self.cur.execute("INSERT INTO groups (group_name) VALUES (?)",(group_name_input,))
        self.conn.commit()
        print(f"{group_name_input} added succsefully")

    def show_groups(self):
        self.cur.execute("SELECT * FROM groups")
        groups_list1=self.cur.fetchall()
        group_list=[group[1] for group in groups_list1]
        return group_list

        

    def each_group(self,group_name_input):
        query=f"""CREATE TABLE IF NOT EXISTS {group_name_input}(
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            name TEXT UNIQUE,
            email TEXT UNIQUE
            ) """
        self.cur.execute(query)
        self.conn.commit()

    def show_group_members(self,group_name):
        query=f"SELEcT * FROM {group_name}"
        self.cur.execute(query)
        grooup_whole=self.cur.fetchall()
        group_members=[member[2] for member in grooup_whole]
        return group_members


    def insert_member(self,member_name,member_email,group_name):
        query=f"INSERT INTO {group_name}(name, email) VALUES (?, ?)"
        self.cur.execute(query,(member_name,member_email))
        self.conn.commit()
        print(f'{member_name} successfully added to {group_name}')