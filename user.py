from locale import currency
from multiprocessing import Value
from optparse import Values
from os import error
import string
import tkinter as ctk
from tkinter import BooleanVar, IntVar, StringVar, Variable, ttk
from tokenize import group
import customtkinter as ctk
from PIL import Image
from database import Database
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("D:/workplace/AP/projects/splitwise/models/dark-blue.json")

from group22 import Group

class user_input:
    def __init__(self):
        #self.user=input('please enter your name:')
        #print(f"welcome {self.user}")
        pass
        

class MainMenu:
    def __init__(self):

        self.db=Database()
        self.db.user_table()
        self.db.friends_table()
        self.group=Group()

        
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

        self.name2=''

        
        
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

        self.db.show_users()



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
        print('I have been called too motherfucker')
        self.db.groups_table()

        #self.login_win.after(1000,self.login_win.destroy)
        #self.app.after(1000,self.app.destroy)
        #print(self.menu)
        #menu_label=ctk.Label(self.app, text=self.menu, font=('bold', 14), pady=20)
        #menu_label.grid(row=1, column=1)
        #while self.default_menu:

        if hasattr(self,'login_win'):
            self.login_win.destroy()
        if hasattr(self,'app'):
            self.app.destroy()
        

        self.menu_win=ctk.CTk()
        self.menu_win.title('menu title')
        self.menu_win.geometry('600x500')

        self.menu_win.columnconfigure(0, weight=1)
        self.menu_win.columnconfigure(1, weight=1)
        self.menu_win.columnconfigure(2, weight=1)
        self.menu_win.rowconfigure(0, weight=1)
        self.menu_win.rowconfigure(1, weight=1)
        self.menu_win.rowconfigure(2, weight=1)
        self.menu_win.rowconfigure(3, weight=1)
        self.menu_win.rowconfigure(4, weight=1)

        

        #welcome_text=f"welcome {self.name2}"
        welcome_label=ctk.CTkLabel(self.menu_win,text='welcome pedram',font=('Arial Rounded MT Bold',25, "bold"))
        welcome_label.grid(row=0,column=0,padx=5,pady=5)

        group_listbox=ctk.CTkTextbox(self.menu_win)
        group_listbox.grid(row=1,column=0,rowspan=2,padx=10,pady=(0,0),sticky='nw')
        group_list=self.db.show_groups()
        for index,group in enumerate(group_list,start=1):
            group_listbox.insert("end",f"{index}.{group}\n")

        friends_listbox=ctk.CTkTextbox(self.menu_win)
        friends_listbox.grid(row=3,column=0,rowspan=2,padx=10,pady=0,sticky='nw')
        friends_list=self.db.show_friends()
        for index,friend in enumerate(friends_list,start=1):
            friends_listbox.insert("end",f"{index}.{friend}\n")


        expense_listbox=ctk.CTkTextbox(self.menu_win)
        expense_listbox.grid(row=1,column=1,rowspan=4,padx=10,pady=(0,10),sticky='nw')
        expense_list=self.db.show_expense(self.name2)
        for index,expense in enumerate(expense_list,start=1):
            expense_listbox.insert("end",f"{index}.{expense}\n")


        
        add_user_button=ctk.CTkButton(self.menu_win,text='add user',command=self.add_user)
        add_user_button.grid(row=1, column=2, rowspan=1, pady=(0,10), padx=10,sticky='nw')
        creat_group_button=ctk.CTkButton(self.menu_win,text='creat group',command=self.creat_group)
        creat_group_button.grid(row=2, column=2, rowspan=1, pady=(0,10), padx=10)
        add_expense_button=ctk.CTkButton(self.menu_win,text='add expense(for user)',command=self.add_expense)
        add_expense_button.grid(row=3, column=2, rowspan=1, pady=(10,0), padx=10)
        track_balance_button=ctk.CTkButton(self.menu_win,text='track balance(for user)',command=self.track_balances)
        track_balance_button.grid(row=3, column=2, rowspan=1, pady=(0,60), padx=10)
        simplify_button=ctk.CTkButton(self.menu_win,text='simplify balances',command=self.simplify)
        simplify_button.grid(row=3, column=2, rowspan=1, pady=(0,120), padx=10)

        self.menu_win.mainloop()


    def login(self):
        self.login_win=ctk.CTkToplevel(self.app)
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
            
        enter_button=ctk.CTkButton(self.login_win,text='enter',command=self.login2)
        enter_button.grid(row=2, column=1,padx=10, pady=10)

    

    def login2(self):
        print('I have been called motherfucker')
        self.name2=self.name_text.get().strip()
        pass2=self.pass_text.get().strip()

        
        print(self.name2)
        print(pass2)

        for widget in self.login_win.grid_slaves(row=3, column=1):
            widget.destroy()
        if self.db.find_user(self.name2,pass2):
            print('we are here')
            login_suc=ctk.CTkLabel(self.login_win,text='welcomeee') #edit
            login_suc.grid(row=3, column=1)
            menu_button=ctk.CTkButton(self.login_win,text='main window',command=self.main)
            menu_button.grid(row=4,column=1,padx=5,pady=5)

            

            #self.login_check= True
        else:
            login_fail=ctk.CTkLabel(self.login_win,text='user/pass is wrong') #edit
            login_fail.grid(row=3, column=1)


    def sign_up(self):
        self.sign_win=ctk.CTkToplevel(self.app)
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

            self.db.insert_user(name2, pass2, email2)  

            self.sign_win.after(100, self.sign_win.destroy) 


        enter_button=ctk.CTkButton(self.sign_win,text='enter',command=sign2)
        enter_button.grid(row=3, column=1)

        enter_button=ctk.CTkLabel(self.sign_win,text='login now')
        enter_button.grid(row=4, column=1)

    def add_user(self):
        self.add_user_win=ctk.CTkToplevel(self.menu_win)

        new_user_text=StringVar()
        new_user_Label=ctk.CTkLabel(self.add_user_win,text='enter name of new user:')
        new_user_Label.grid(row=0,column=0,padx=5,pady=5)
        new_user_entry=ctk.CTkEntry(self.add_user_win,textvariable=new_user_text)
        new_user_entry.grid(row=0,column=1)
        
        

        friends_names=self.db.show_friends()
        
        def add2():
            new_user_text2=new_user_text.get().strip()
            print('hey')
            print(new_user_text2)
            if new_user_text2 not in self.user_list.keys() and new_user_text2 not in  friends_names: 
                self.user_list[new_user_text2]=[]

                new_email_text=StringVar()
                new_email_Label=ctk.CTkLabel(self.add_user_win,text='enter email of new user:')
                new_email_Label.grid(row=2,column=0,padx=5,pady=5)
                new_email_entry=ctk.CTkEntry(self.add_user_win,textvariable=new_email_text)
                new_email_entry.grid(row=2,column=1)
                

                def add3():
                    new_email_text2=new_email_text.get().strip()
                    self.db.insert_friend(new_user_text2,new_email_text2)
                    print(f"{new_user_text2} succesfully added")
                    new_user=None
                enter_button=ctk.CTkButton(self.add_user_win,text='enter',command=add3)
                enter_button.grid(row=3,column=1)
            else:
                print('the user already exists')
                error_message=ctk.CTkLabel(self.add_user_win,text='this friend already exists')
                error_message.grid(row=2,column=1)
            #return_button=ctk.CTkLabel(self.add_user_win,text='return to menu',command=self.main)   
            #return_button.grid(row=4,column=1) 

        check_user=ctk.CTkButton(self.add_user_win,text='check user',command=add2)
        check_user.grid(row=1,column=1,padx=5,pady=5)
        #self.return_menu()

    def add_expense(self):
        self.add_expense_win=ctk.CTkToplevel(self.menu_win)
        self.name2='pedram'             #edit later
        self.db.each_user_table(self.name2)
        


        #user_name=input('enter name of the user: ')
        #if user_name not in self.user_list.keys():
        #    print('add user first')
        #    self.return_menu()
        
        friend_text=StringVar()
        friend_label=ctk.CTkLabel(self.add_expense_win,text='name of the friend')
        friend_label.grid(row=0,column=0)
        friend_entry=ctk.CTkEntry(self.add_expense_win,textvariable=friend_text)
        friend_entry.grid(row=0,column=1)

        amount_text=IntVar()
        amount_Label=ctk.CTkLabel(self.add_expense_win,text='amount of money')
        amount_Label.grid(row=1,column=0)
        amount_entry=ctk.CTkEntry(self.add_expense_win,textvariable=amount_text)
        amount_entry.grid(row=1,column=1)
        
        date_text=StringVar()
        date_label=ctk.CTkLabel(self.add_expense_win,text='date(yyyy-mm-dd)')
        date_label.grid(row=0,column=3)
        date_entry=ctk.CTkEntry(self.add_expense_win,textvariable=date_text)
        date_entry.grid(row=0,column=4)

        desc_text=StringVar()
        desc_label=ctk.CTkLabel(self.add_expense_win,text='description')
        desc_label.grid(row=1,column=3)
        desc_entry=ctk.CTkEntry(self.add_expense_win,textvariable=desc_text)
        desc_entry.grid(row=1,column=4)
        
        currencies=['IRR','USD']
        currency_var=StringVar(value='IRR')
        currency_switch=ctk.CTkOptionMenu(self.add_expense_win,values=currencies,variable=currency_var)
        currency_switch.grid(row=2,column=1)


        paid_var=BooleanVar(value=False)
        paid_switch=ctk.CTkSwitch(self.add_expense_win,text='paid',variable=paid_var,onvalue=True, offvalue=False)
        paid_switch.grid(row=3,column=1,padx=50)

        def add_expense2():
            final_name=friend_text.get().strip()
            final_amount=amount_text.get()
            final_desc=desc_text.get().strip()
            final_date=date_text.get().strip()
            final_paid=paid_var.get()
            final_currency=currency_var.get()
            share=final_amount/2
            self.db.each_friend_table(final_name)
            if final_paid:
                self.db.others_insert(final_name,share,final_currency,final_date,final_desc,self.name2)
                self.db.each_insert(self.name2,-(share),final_currency,final_date,final_desc,final_name)
            else:
                self.db.others_insert(final_name,-(share),final_currency,final_date,final_desc,self.name2)
                self.db.each_insert(self.name2,share,final_currency,final_date,final_desc,final_name)
        enter_button=ctk.CTkButton(self.add_expense_win,text='enter',command=add_expense2)
        enter_button.grid(row=4,column=1)

            

    def simplify(self):
        print('simplify here')
        self.return_menu()

    def creat_group(self):
            self.db.groups_table()
            self.create_group_win=ctk.CTkToplevel(self.menu_win)
            
            new_group_text=StringVar()
            new_group_label=ctk.CTkLabel(self.create_group_win,text='name of the group')
            new_group_label.grid(row=0,column=0)
            new_group_entry=ctk.CTkEntry(self.create_group_win,textvariable=new_group_text)
            new_group_entry.grid(row=0,column=1)
            def create2():
                group_name=new_group_text.get().strip()
                if group_name in self.db.show_groups():
                    group_exists=ctk.CTkLabel(self.create_group_win,text='this group already exists')
                    group_exists.grid(row=2,column=1)
                else:
                    self.db.insert_group(group_name)
                    self.db.each_group(group_name)
                    group_added=ctk.CTkLabel(self.create_group_win,text=f'{group_name} successfuly added')
                    group_added.grid(row=2,column=1)
                def create3():
                        
                    new_member_name_text=StringVar()
                    new_member_name_label=ctk.CTkLabel(self.create_group_win,text='name of the new member')
                    new_member_name_label.grid(row=4,column=0)
                    new_member_name_entry=ctk.CTkEntry(self.create_group_win,textvariable=new_member_name_text)
                    new_member_name_entry.grid(row=4,column=1)

                    new_member_email_text=StringVar()
                    new_member_email_label=ctk.CTkLabel(self.create_group_win,text='email of the new member')
                    new_member_email_label.grid(row=4,column=2)
                    new_member_email_entry=ctk.CTkEntry(self.create_group_win,textvariable=new_member_email_text)
                    new_member_email_entry.grid(row=4,column=3)

                    def create4():
                        final_add_member_name=new_member_name_text.get().strip()
                        final_add_member_email=new_member_email_text.get().strip()
                        if final_add_member_name not in self.db.show_group_members(group_name):
                            self.db.insert_member(final_add_member_name,final_add_member_email,group_name)
                            cong_label=ctk.CTkLabel(self.create_group_win,text='member successfully added')
                            cong_label.grid(row=6,column=1)
                        else:
                            fail_label=ctk.CTkLabel(self.create_group_win,text='member already exists')
                            fail_label.grid(row=6,column=1)

                    add_member_button2=ctk.CTkButton(self.create_group_win,text='add entered member',command=create4)
                    add_member_button2.grid(row=5,column=1,padx=10,pady=10)
                        
                add_member_button=ctk.CTkButton(self.create_group_win,text='add member',command=create3)
                add_member_button.grid(row=3,column=1,padx=10,pady=10)

            enter_button=ctk.CTkButton(self.create_group_win,text='enter',command=create2)
            enter_button.grid(row=1,column=1,padx=10,pady=10)

    def track_balances(self):
        print('here we track balances')
        self.return_menu()

    def return_menu(self):
        return_button=int(input('enter 1 to return to menu: '))
        if return_button==1:
            #print(self.menu)
            self.default_menu=not self.default_menu
            #print(self.default_menu)
            #self.main()
        else:
            print('ey baba')  #edit this

    

if __name__ == "__main__":
    app=MainMenu()
    #app.welcome()
    app.app.mainloop()


