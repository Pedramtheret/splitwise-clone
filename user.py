import tkinter as ctk
from tkinter import StringVar, ttk
import customtkinter as ctk
from PIL import Image
from database import Database
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("D:/workplace/AP/projects/splitwise/models/dark-blue.json")

class user_input:
    def __init__(self):
        #self.user=input('please enter your name:')
        #print(f"welcome {self.user}")
        pass
        

class MainMenu:
    def __init__(self):

        self.db=Database()
        self.db.user_table()
        
        self.menu="""
        welcome to splitwise
        1.add_user
        2.creat group
        3.add expense
        4.track_balance
        5.simplify debts
        6.exit
        """
        self.balance_graph : dict={}
        self.user_list :dict ={}
        self.default_menu=True

        self.login_check= False

        self.app=ctk.CTk()
        self.app.title('Pedram splitwise clone')
        self.app.geometry('900x350')

        self.app.columnconfigure(0, weight=1)
        self.app.columnconfigure(1, weight=1)
        self.app.columnconfigure(2, weight=1)
        self.app.rowconfigure(0, weight=1)
        self.app.rowconfigure(1, weight=0)
        self.app.rowconfigure(2, weight=0)

        

        self.app.after(2000,self.welcome_text)
        self.app.after(3000,self.welcome_phrase1)
        self.app.after(3500,self.welcome_phrase2)
        

        self.header_font=("Helvetica", 18, "bold")
        self.main_font=("Helvetica", 12)

        self.welcome()

        
    
    def welcome(self):
        until_image=ctk.CTkImage(dark_image=Image.open('D:/workplace/AP/projects/splitwise/models/ehud-neuhaus-Ql3ULtlplsQ-unsplash.jpg'),size=(233,350))
        until_label=ctk.CTkLabel(self.app, image=until_image, text='')
        until_label.grid(row=0, column=0, rowspan=3 ,sticky='nsw' )

        login_button=ctk.CTkButton(self.app,text='login',command=self.login)
        login_button.grid(row=0, column=2,padx=10,pady=(10,5),sticky='ne')
        sign_button=ctk.CTkButton(self.app,text='sign up',command=self.sign_up)
        sign_button.grid(row=0, column=2,padx=10,pady=(40,5), sticky='ne')

        self.db.show_all()



    def welcome_text(self):
        welcom_Label=ctk.CTkLabel(self.app, text='welcome to Track It', font=('Arial Rounded MT Bold',25, "bold") )
        welcom_Label.grid(row=0, column=1, padx=20, pady=(10,5), sticky='nw')

    def welcome_phrase1(self):
        phrase_Label=ctk.CTkLabel(self.app, text='Got cash floating around with friends?', font=('Comic Sans MS',20, "bold"))
        phrase_Label.grid(row=0, column=1, padx=20, pady=(50,5), sticky='nw')
    
    def welcome_phrase2(self):
        phrase_Label2=ctk.CTkLabel(self.app, text='we are gonna track it here', font=('Comic Sans MS',20, "bold"))
        phrase_Label2.grid(row=0, column=1, padx=20, pady=(100,5), sticky='nw')

    
    def main(self):
        #print(self.menu)
        #menu_label=ctk.Label(self.app, text=self.menu, font=('bold', 14), pady=20)
        #menu_label.grid(row=1, column=1)
        #while self.default_menu:

        self.login_win.destroy()
        self.app.destroy()
        self.menu_win=ctk.CTk()
        self.menu_win.title('Pedram splitwise clone')
        self.menu_win.geometry('500x500')

        add_user_button=ctk.CTkButton(self.app,text='add user',command=self.add_user)
        add_user_button.grid(row=0, column=0, rowspan=1, pady=40, padx=275)
        creat_group_button=ctk.CTkButton(self.app,text='creat group',command=self.creat_group)
        creat_group_button.grid(row=1, column=0, rowspan=1, pady=10, padx=275)
        add_expense_button=ctk.CTkButton(self.app,text='add expense(for user)',command=self.add_expense)
        add_expense_button.grid(row=2, column=0, rowspan=1, pady=10, padx=275)
        track_balance_button=ctk.CTkButton(self.app,text='track balance(for user)',command=self.track_balances)
        track_balance_button.grid(row=3, column=0, rowspan=1, pady=10, padx=275)
        simplify_button=ctk.CTkButton(self.app,text='simplify balances',command=self.simplify)
        simplify_button.grid(row=4, column=0, rowspan=1, pady=10, padx=275)

        '''
        while self.default_menu:
            self.user_choice=int(input('please choose number of an option:'))
            if self.user_choice == 1:
                self.add_user()
                self.default_menu=not self.default_menu       
            elif self.user_choice == 2:
                self.creat_group()
            elif self.user_choice == 3:
                self.add_expense()
                self.default_menu=not self.default_menu
            elif self.user_choice == 4 :
                self.track_balances()
            elif self.user_choice == 5 :
                self.simplify()
            elif self.user_choice == 6 :
                print('goodbye')
                break
            else:
                print('there is no such an option,try again')
        '''
    def login(self):
        self.login_win=ctk.CTk()
        self.login_win.title('Pedram splitwise clone')
        self.login_win.geometry('250x250')

        self.name_text = StringVar()
        name_label = ctk.CTkLabel(self.login_win, text='Name', font=('Arial Rounded MT Bold', 15))
        name_entry = ctk.CTkEntry(self.login_win, textvariable=self.name_text)
        '''
        name_text=StringVar()
        name_label=ctk.CTkLabel(self.login_win,text='Name',font=('Arial Rounded MT Bold',15))
        name_entry=ctk.CTkEntry(self.login_win,textvariable=name_text)
        '''
        name_label.grid(row=0,column=0,padx=10,pady=1)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pass_text=StringVar()
        pass_label=ctk.CTkLabel(self.login_win,text='password',font=('Arial Rounded MT Bold',15))
        pass_entry=ctk.CTkEntry(self.login_win,textvariable=self.pass_text)
        pass_label.grid(row=1,column=0,padx=10,pady=1)
        pass_entry.grid(row=1, column=1, padx=10, pady=10)

        def login2():

            name2=self.name_text.get().strip()
            pass2=self.pass_text.get().strip()

            print(name2)
            print(pass2)

            for widget in self.login_win.grid_slaves(row=3, column=1):
                widget.destroy()
            if self.db.find_user(name2,pass2):
                login_suc=ctk.CTkLabel(self.login_win,text='welcomeee') #edit
                login_suc.grid(row=3, column=1)
                menu_button=ctk.CTkButton(self.login_win,text='main window',command=self.main)
                menu_button.grid(row=4,column=1,padx=5,pady=5)
            else:
                login_fail=ctk.CTkLabel(self.login_win,text='user/pass is wrong') #edit
                login_fail.grid(row=3, column=1)
            
            
        enter_button=ctk.CTkButton(self.login_win,text='enter',command=login2)
        enter_button.grid(row=2, column=1,padx=10, pady=10)

        

        self.login_win.mainloop()


    def sign_up(self):
        self.sign_win=ctk.CTk()
        self.sign_win.title('pedram splitwise clone')
        self.sign_win.geometry('250x250')

        self.name_sign_text=StringVar()
        name_label=ctk.CTkLabel(self.sign_win,text='Name',font=('Arial Rounded MT Bold',15))
        name_entry=ctk.CTkEntry(self.sign_win,textvariable=self.name_sign_text)
        name_label.grid(row=0,column=0,padx=10,pady=1)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pass_sign_text=StringVar()
        pass_label=ctk.CTkLabel(self.sign_win,text='password',font=('Arial Rounded MT Bold',15))
        pass_entry=ctk.CTkEntry(self.sign_win,textvariable=self.pass_sign_text)
        pass_label.grid(row=1,column=0,padx=10,pady=10)
        pass_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_text=StringVar()
        email_label=ctk.CTkLabel(self.sign_win,text='Email',font=('Arial Rounded MT Bold',15))
        email_entry=ctk.CTkEntry(self.sign_win,textvariable=self.email_text)
        email_label.grid(row=2,column=0,padx=10,pady=10)
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        def sign2():
            name2=self.name_sign_text.get()
            email2=self.email_text.get()
            pass2=self.pass_sign_text.get()
            print(name2)
            print(email2)

            self.db.insert_user(name2, email2, pass2)  

            self.sign_win.destroy()


        enter_button=ctk.CTkButton(self.sign_win,text='enter',command=sign2)
        enter_button.grid(row=3, column=1)

        enter_button=ctk.CTkLabel(self.sign_win,text='login now')
        enter_button.grid(row=4, column=1)

        self.sign_win.mainloop()

        


    def add_user(self):
        
        new_user=input('please enter name of new user:')
        if new_user not in self.user_list.keys():
            self.user_list[new_user]=[]
            print(f"{new_user} succesfully added")
            new_user=None
        else:
            print('the user already exists')    
        self.return_menu()

    def add_expense(self):
        user_name=input('enter name of the user: ')
        if user_name not in self.user_list.keys():
            print('add user first')
            self.return_menu()
        else:
            #continue from hereee
            amount=int(input('how much money? '))   #edit sentence
            payer=int(input(('enter 0 if you should pay,else enter 1: ')))
            other=input('enter name of the othe one: ') #rename
            # I feel this part can be written very better
            if payer == 0:
                self.user_list[user_name].append((other,(amount/2)))
                if other in self.user_list:
                    self.user_list[other].append((user_name,-(amount/2)))
            if payer==1:
                self.user_list[user_name].append((other,-(amount/2)))
                if other in self.user_list:
                    self.user_list[other].append((user_name,(amount/2)))
            print(self.user_list)
            


    def simplify(self):
        print('simplify here')
        self.return_menu()

    def creat_group(self):
        print('here we creat group')
        self.return_menu()   

    def track_balances(self):
        print('here we track balances')
        self.return_menu()

    def return_menu(self):
        return_button=int(input('enter 1 to return to menu: '))
        if return_button==1:
            #print(self.menu)
            self.default_menu=not self.default_menu
            #print(self.default_menu)
            self.main()
        else:
            print('ey baba')  #edit this

    

if __name__ == "__main__":
    app=MainMenu()
    #app.welcome()
    app.app.mainloop()