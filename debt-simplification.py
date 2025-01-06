from graph import Graph
import numpy as np

class simplification:
    def __init__(self):
        self.graph=Graph()
        #print(self.graph.graph)
        self.one_graph={}
        self.only_nodes={key:[] for key in self.graph.graph}
        self.cycle_path=[]
        self.final_dict={}

        self.cyle_flag=False


    def one_transaction(self,graphh):
        
        one_graph={key:[(neighbor, sum(w for n, w in neighbors if n == neighbor)) 
                        for neighbor in {n for n, _ in neighbors}] 
                        for key, neighbors in graphh.items()}
        return one_graph
        
        #print(self.one_graph)

    def just_nodes(self,special_graph:dict):
        only_nodes={key:[] for key in special_graph}
        for key in special_graph.keys():
            for neighbor, weight in special_graph[key]:
                only_nodes[key].append(neighbor)
        return only_nodes

    def dc_util(self,graph,parent,general_visited,rec_stack,util_path):

        general_visited[parent]=True
        rec_stack[parent]=True
        util_path.append(parent)
        
        for chi in graph[parent]:
            if not general_visited[chi] and self.dc_util(graph,chi,general_visited,rec_stack,util_path):
                #self.cycle_path.append(chi)
                return True
            elif rec_stack[chi]:
                util_path.append(chi)
                return True
        util_path.pop()
        rec_stack[parent]=False
        #self.cycle_path=[]
        return False

    def dc(self,dc_input):
        
        #self.one_graph=self.one_transaction(dc_input)
        #self.just_nodes(self.one_graph)   #uncomment later
        one_graph=self.one_transaction(dc_input)
        only_nodes=self.just_nodes(one_graph)
        general_visited={key: False for key in only_nodes.keys()}
        rec_stack={key: False for key in only_nodes.keys()}

        dc_path=[] #I changed here

        for child in general_visited:
            if not general_visited[child] and self.dc_util(only_nodes,child,general_visited,rec_stack,dc_path):
                cycle_start = dc_path[-1]
                cycle=[]
                for idx in range(len(dc_path)-2, -1, -1):
                    cycle.append(dc_path[idx+1])
                    if dc_path[idx] == cycle_start:
                        cycle.append(cycle_start)
                        break
                cycle_path = cycle[::-1]

                if len(cycle_path)>2:
                    self.cycle_flag=True
                    return cycle_path
                
    def is_cyclic(self):
        if self.dc(self.graph.graph):
            print('There is a cycle')
            print(self.cycle_path)

    def simplify_cycle(self,graphhhh:dict):
        cycle_free2=self.one_transaction(graphhhh)
        print("initail:",cycle_free2)
        iteration=0
        max_iteration=2
        while iteration < max_iteration:
            cycle=self.dc(cycle_free2)
            print(cycle)
            if cycle:
                print(f"iteration{iteration}: cycle detected:{cycle}")
                
                if len(cycle)<3:
                    print("invalid cycle")  
                    break
                temp_weight=0
                
                
                #for x, y in zip(anb2, anb2[1:]):
                for i in range(len(cycle)-2):          #check here
                    x=cycle[i]
                    y=cycle[i+1]
                    for neighbor, weight in cycle_free2[x]:
                        if neighbor == y:
                            #print(temp_weight)
                            temp_weight += weight
                            print('yes')
                            break
                    else:
                        print('I tried')
                        break
                                                   
                    cycle_free2[x]=[(neighbor, weight) for neighbor, weight in cycle_free2[x] if neighbor != y]
                #cycle_free2[self.cycle_path[-2]]=[(neighbor, weight + temp_weight) for neighbor, weight
                #                            in cycle_free2[self.cycle_path[-2]] if neighbor == self.cycle_path[-1]]
                updated=False
                last_from=cycle[-2]
                last_to=cycle[-1]
                print(cycle_free2)
                for idx, (n,w) in enumerate(cycle_free2[last_from]):
                    print(n)
                    print("blah blah",last_to)
                    if n==last_to:
                        #print(temp_weight)
                        cycle_free2[last_from][idx] = (n, w + temp_weight)
                        #print('yes')
                        updated=True
                        break
                    

                self.cycle_flag=False
                print("updated graph after simplification:",cycle_free2)
                iteration += 1
            else:
                print("no more iteration founded")    
                break
                
        if iteration == max_iteration:
            print("we reached the max iteration,maybe there would be some cycles left")
            
        
    def remove_zeros(self, graph:dict):
        final_dict={}
        for key in graph.keys():
            if graph[key] != []:
                final_dict[key]=graph[key]
        return final_dict

    def final_simplify(self, graphh:dict, sorted_array:dict, balance_dict: dict): 
        positive_dict={}
        negative_dict={}
        print(balance_dict)
        for node in balance_dict:
            if balance_dict[node]>0:
                positive_dict[node]=balance_dict[node]
            else:
                negative_dict[node]=balance_dict[node]
        negative_dict2=[n * -1 for n in list(negative_dict.values())]
        

        pos_cusum=np.cumsum(list(positive_dict.values()))
        neg_cumsum=np.cumsum(negative_dict2)
        
        final_graph={node:[] for node in graphh}

        for node in sorted_array:
            if positive_dict.get(node,0) >0:
                to_settle= positive_dict[node]

                for settler, balance in list(negative_dict.items()):
                    if balance ==0:
                        continue

                    transaction=min( -balance,to_settle)
                    final_graph[node].append((settler,transaction))

                    positive_dict[node] -= transaction
                    negative_dict[settler] += transaction

                    if to_settle ==0:
                        break
            
            elif negative_dict.get(node ,0) <0:
                to_settle = - negative_dict[node]

                for settler, balance in list(positive_dict.items()):
                    if balance ==0:
                        continue

                    transaction=min( balance,to_settle)
                    final_graph[node].append((settler,transaction))

                    negative_dict[node] += transaction
                    positive_dict[settler] -= transaction

                # Stop if the node's balance is settled
                if negative_dict[node] == 0:
                    break

        return final_graph



            


    


s=simplification()
ss=s.final_simplify(s.graph.graph,s.graph.combined(s.graph.graph),s.graph.node_balance(s.graph.graph))

