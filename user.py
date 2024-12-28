
class user_input:
    def __init__(self):
        #self.user=input('please enter your name:')
        #print(f"welcome {self.user}")
        pass
        

class MainMenu:
    def __init__(self):
        self.user=user_input()
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

    def main(self):
        print(self.menu)
        
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

    def add_user(self):
        
        new_user=input('please enter name of new user:')
        if new_user not in self.user_list.keys():
            self.user_list[new_user]=[]
            print(f"{new_user} succesfully added")
            new_user=None
        else:
            print('the user already exists')    
        self.return_menu()
    '''
    def add_expense(self):
        host_n , geust_n=map(int,input('please enter number of hosts and guests(comma seperated):').split())
        print(type(host_n))
        print(geust_n)

        amount=input('enter the amount of money: ')
        hosts=list(map(str,input('enter people who paid(comma seperated) :').split()))
        geusts=list(map(str,input('enter other people invoveld(comma seperated): ').split()))
        share : int=int(amount)/(int(host_n)+int(geust_n))
        share_per_host :int = int(share/host_n)

        
        for host in hosts:
            if host not in self.balance_graph:
                self.balance_graph[host] =[]
        for geust in geusts:
            if geust not in self.balance_graph:
                self.balance_graph[geust] =[]
        for geust in geusts:
            for host in hosts:
                self.balance_graph[geust].append((host,share_per_host))
                self.balance_graph[host].append((geust,-(share_per_host)))
        print(self.balance_graph)

        #self.return_menu()
        '''
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
    app.main()
