from user import MainMenu

class group:
    def __init__(self) -> None:
        print('welcome, here you can creat and manage groups')
        self.groups :dict={}
        self.main_menu=MainMenu()
        self.balance_graph : dict={}
        self.checkpoint=True

    def main(self):
        print('1.add new group')
        print('2.add expense to an existing group')
        print('3.track balances of an existing group')
        print('4.return to the main menu')

        group_choice=int(input('choose an option: '))
        if group_choice == 1:
            self.group_input()
        elif group_choice == 2:
            self.group_expense()
        elif group_choice == 3 :
            self.group_balance()
        elif group_choice == 4:
            self.main_menu.return_menu()

        

    def group_input(self):
        group_name=input('please enter the group name: ')
        if group_name in self.groups.keys():
            print('the group already exists')
            if int(input('press 1 to add new members to this group: ')) == 1:
                new_members :list=list(map(str,input('enter name of new group members(comma seperated): ').split()))
                for member in new_members:
                    self.groups[group_name].update({member:[]})
                print(f"{new_members} succesfully added to the {group_name}")
                print(self.groups[group_name])
                #consider quitting the app
                if int(input('press 1 to return to the group menu: ')) == 1:
                    self.main()

        else:
            group_no :int=int(input('please enter the number of members: '))
            members :list=list(map(str,input('enter name of group members(comma seperated): ').split()))
            group_members :dict={char :[] for char in members}
            if len(members) == group_no:
                self.groups[group_name]=group_members
                print(f"{group_name} succesfully added")
                print(self.groups[group_name])
                if int(input('press 1 to return to the group menu: ')) == 1:
                    self.main()
            else:
                print('the numbers does not match')


    def group_expense(self):
        group_name: str=input('please enter group name: ')
        if group_name not in self.groups.keys():
            print('please define your group first,enter 1 to define the group')
            if int(input()) == 1:
                self.group_input()
        
        else:
            host_n , geust_n=map(int,input('please enter number of hosts and guests(comma seperated):').split())
            amount=int(input('enter the amount of money: '))
            hosts=list(map(str,input('enter people who paid(comma seperated) :').split()))                                                                                  
            geusts=list(map(str,input('enter other people invoveld(comma seperated): ').split()))
            if len(hosts) == host_n and len(geusts) == geust_n:
                
                for char in geusts + hosts:
                    if char not in self.groups[group_name].keys():
                        print('some members are not in the group,press 1 to get back to add group')

                        if int(input()) == 1 :
                            self.group_input()
                            break
                else:
                        share : int=int(amount/(host_n+geust_n))
                        share_per_host :int = int(share/host_n)
                        for host in hosts:
                            for geust in geusts:                                   
                                self.groups[group_name][host].append((geust,-(share_per_host)))
                                self.groups[group_name][geust].append((host,(share_per_host)))
                    #self.groups[group_name].append(self.balance_graph)
                        print('new expenses succesfully added')
                        self.balance_graph={}
            else:
                print('numbers of peaple in this expense does not match')
    
        print(self.groups[group_name])
        if int(input('press 1 to return to the group menu: ')) == 1:
            self.main()

    def group_balance(self):
        pass



if __name__=='__main__':
    a=group()
    a.main()