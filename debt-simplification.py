from graph import Graph

class simplification:
    def __init__(self):
        self.graph=Graph()
        #print(self.graph.graph)
        self.one_graph={}
        self.only_nodes={key:[] for key in self.graph.graph}
        self.cycle_path=[]
        self.final_dict={}

    def one_transaction(self,graphh):

        self.one_graph={key:[(neighbor, sum(w for n, w in neighbors if n == neighbor)) 
                        for neighbor in {n for n, _ in neighbors}] 
                        for key, neighbors in graphh.items()}
        return self.one_graph
        
        #print(self.one_graph)

    def just_nodes(self,special_graph:dict):
        for key in special_graph.keys():
            for neighbor, weight in special_graph[key]:
                self.only_nodes[key].append(neighbor)

    def dc_util(self,graph,parent,general_visited,rec_stack):
        if not general_visited[parent]:
            general_visited[parent]=True
            rec_stack[parent]=True
            self.cycle_path.append(parent)
            
            for chi in graph[parent]:
                if not general_visited[chi] and self.dc_util(graph,chi,general_visited,rec_stack):
                    #self.cycle_path.append(chi)
                    return True
                elif rec_stack[chi]:
                    self.cycle_path.append(chi)
                    return True
            self.cycle_path.remove(parent)
        rec_stack[parent]=False
        #self.cycle_path=[]
        return False

    def dc(self,dc_input):
        self.one_transaction(dc_input)
        self.just_nodes(self.one_graph)   #uncomment later
        general_visited={key: False for key in self.only_nodes.keys()}
        rec_stack={key: False for key in self.only_nodes.keys()}

        for child in general_visited:
            if not general_visited[child] and self.dc_util(self.only_nodes,child,general_visited,rec_stack):
                return True
        return False

    def is_cyclic(self):
        if self.dc(self.graph.graph):
            print('There is a cycle')
            print(self.cycle_path)

    def simplify_cycle(self,graphhhh:dict):
        self.cycle_free=self.one_transaction(graphhhh)
        for i in range(5):
            if self.dc(self.cycle_free):
                print(self.cycle_free)
                print(f'cycle detected {self.cycle_path}')  
                temp_weight=0
                anb2=self.cycle_path[:-1]
                print(self.cycle_path)
                for x, y in zip(anb2, anb2[1:]):
                    for neighbor, weight in self.cycle_free[x]:
                        if neighbor == y:
                            temp_weight += weight
                            self.cycle_free[x]=[(neighbor, weight) for neighbor, weight in self.cycle_free[x] if neighbor != y]

                self.cycle_free[self.cycle_path[-2]]=[(neighbor, weight + temp_weight) for neighbor, weight
                                            in self.cycle_free[self.cycle_path[-2]] if neighbor == self.cycle_path[-1]]
                
                self.cycle_path=[]
                print(self.cycle_free)
        
    def remove_zeros(self, graph:dict):
        for key in graph.keys():
            if graph[key] != []:
                self.final_dict[key]=graph[key]

    def final_simplify(self, graph:dict, soreted_array:dict, balance_dict: dict): 
        while soreted_array:
            pass
        #continue from here

            


    


s=simplification()
s.simplify_cycle(s.graph.graph)
