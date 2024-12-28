
from tkinter.font import BOLD
from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq
import numpy as np

class Node:
    def __init__(self, id: str, distance: int):
        self.id = id
        self.distance = distance

    def __lt__(self, next):
        return self.distance < next.distance

class Graph:
    def __init__(self):
        
        self.graph={"A": [("B", 5), ("C", -2), ("D", 3), ("E", 1),("B",6),("B",8)],
                    "B": [("A", -5), ("C", 6), ("D", 1)],
                    "C": [("A", 2), ("B", -6), ("D", 4), ("E", 3)],
                    "D": [("A", -3), ("B", -1), ("C", -4), ("E", 2)],
                    "E": [("A", -1), ("C", -3), ("D", -2)]}
        '''
        self.graph={"A": [("B", 5), ("D", 3), ("E", 1)],
                    "B": [ ("C", 6), ("D", 1)],
                    "C": [("A", 2),  ("D", 4), ("E", 3)],
                    "D": [ ("E", 2)],
                    "E": []}
        '''
        self.degree_dict={}
        self.degree_neg={}
        self.g_graph=nx.DiGraph()
        self.sorted_degree={}
        self.balance_dict={}
        #final_dict={}
        '''
        self.graph = {
        "A": ["B", "C"],
        "B": ["C", "D"],
        "C": ["A", "E"],
        "D": ["F"],
        "E": ["F", "G"],
        "F": ["D", "H"],
        "G": ["E"],
        "H": ["I"],
        "I": ["J"],
        "J": ["H", "K"],
        "K": ["L"],
        "L": ["I"]}
        '''
    def degree(self):
        
        for node in self.graph:
            self.degree_dict[node]=sum(abs(weight) for neghibor, weight in self.graph[node] )
            self.degree_neg[node]=sum(weight for neghibor, weight in self.graph[node] )

        #print(self.degree_dict)
        central_node=max(list(self.degree_dict.values()))#you should print the key.continue from here
        keys=list(self.degree_dict.keys())
        values=list(self.degree_dict.values())
        ascending_soreted_index=np.argsort(values)
        soreted_index=ascending_soreted_index[::-1]

        keys2=list(self.degree_neg.keys())
        values2=list(self.degree_neg.values())
        ascending_soreted_index2=np.argsort(values2)
        soreted_index2=ascending_soreted_index2[::-1]

        self.soreted_degree={keys[i]:values[i] for i in soreted_index}
        self.soreted_degree_2={keys2[i]:values2[i] for i in soreted_index2}
        print(self.soreted_degree)
        print(self.degree_neg)
        #print(f'Node {central_node}') 

    def dijestra(self, graph, start):
        shortest_distances = {}
        distance = 0
        nodes = [Node(id=start, distance=distance)]
        while nodes:
            node = hq.heappop(nodes)
            if node.id in shortest_distances:
                continue
            shortest_distances[node.id] = node.distance
            for id, weight in graph[node.id]:
                hq.heappush(nodes, Node(id=id, distance=distance + weight))

        return shortest_distances
    
    def node_balance(self, balance_graph:dict):
        #self.graph=balance_graph            #edit later
        temp_weight=0
        for key in balance_graph.keys():
            for neighbor, weight in balance_graph[key]:
                temp_weight += weight
            self.balance_dict[key]=temp_weight
            temp_weight=0
        print(self.balance_dict)

    def remove_zeros(self,graph):
        pass




   

    def closness(self):
        pass


    def convert_graph(self):    
        
        for node, edges in self.graph.items():
            for neighbor, weight in edges:
                self.g_graph.add_edge(node, neighbor, weight=weight)
        print(self.g_graph)

        

'''
    def visualization(self):
        
        poss=nx.spring_layout(self.g_graph)
        fig, ax=plt.subplots(figsize=(6,8))
        nx.draw(self.g_graph, poss, with_labels=True, font_weight=BOLD, node_color='skyblue',ax=ax)
        nx.draw_networkx_edge_labels(self.g_graph, poss, edge_labels={(u, v): f"{d['weight']}" for 
                                      u, v, d in self.g_graph.edges(data=True)},font_size=10, label_pos=0.5,ax=ax)
        plt.show()

'''



if __name__=='__main__':
    g=Graph()
    
    #g.convert_graph()
    #g.visualization()
    g.degree()
    g.node_balance(g.graph)
    