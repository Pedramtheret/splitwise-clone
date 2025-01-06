from turtle import pos
import networkx as nx
import heapq as hq
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


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
                    "C": [("A", 2),  ("D", 4)],
                    "D": [ ("E", 2)],
                    "E": [("C",7)]}
        '''
        '''       
        self.graph={
        "a": [("b", 8), ("c", 3), ("d", 6)],
        "b": [("a", 8), ("e", 5)],
        "c": [("a", 3), ("d", 2)],
        "d": [("a", 6), ("c", 2), ("e", 5), ("g", 3)],
        "e": [("b", 5), ("d", 5), ("f", 5)],
        "f": [("e", 5), ("g", 3), ("h", 6)],
        "g": [("d", 3), ("f", 3), ("h", 4)],
        "h": [("g", 4), ("f", 6)],
}
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
    def degree(self,graph2):
        degree_dict={}
        degree_neg={}
        for node in graph2:
            degree_dict[node]=sum(abs(weight) for neghibor, weight in graph2[node] )
            degree_neg[node]=sum(weight for neghibor, weight in graph2[node] )

        #print(self.degree_dict)
        
        keys=list(degree_dict.keys())
        values=list(degree_dict.values())
        ascending_soreted_index=np.argsort(values)
        soreted_index=ascending_soreted_index[::-1]

        keys2=list(degree_neg.keys())
        values2=list(degree_neg.values())
        ascending_soreted_index2=np.argsort(values2)
        soreted_index2=ascending_soreted_index2[::-1]

        sorted_degree={keys[i]:values[i] for i in soreted_index}
        sorted_degree_2={keys2[i]:values2[i] for i in soreted_index2}

        return sorted_degree
        
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
                hq.heappush(nodes, Node(id=id, distance=node.distance + weight))

        return shortest_distances
    
    def node_balance(self, balance_graph:dict):
        #self.graph=balance_graph            #edit later
        balance_dict={}
        positive_dict={}
        negative_dict={}
        temp_weight=0
        for key in balance_graph.keys():
            for neighbor, weight in balance_graph[key]:
                temp_weight += weight
            balance_dict[key]=temp_weight
            temp_weight=0
        for node in balance_dict:
            if balance_dict[node]>0:
                positive_dict[node]=balance_dict[node]
            else:
                negative_dict[node]=balance_dict[node]
        return balance_dict
    def remove_zeros(self,graph):
        for node in graph:
            graph[node]=[(neighbor, weight) for neighbor, weight in graph[node] if weight != 0]
        return graph
    
    def closness(self,graph):
        shortest_sum=0
        close_graph={}
        for node in graph:
            shortest_list=self.dijestra(graph, node)
            close_graph[node]=(1/sum(shortest_list.values()))

        return close_graph

    def convert_graph(self):    
        
        for node, edges in self.graph.items():
            for neighbor, weight in edges:
                self.g_graph.add_edge(node, neighbor, weight=weight)
        print(self.g_graph)

    def combined(self,graph):
        degree_centrality=self.degree(graph)
        closeness_centrality=self.closness(graph)

    
        degree_values = list(degree_centrality.values())
        closeness_values = list(closeness_centrality.values())

        # Normalize each centrality individually
        degree_scaler = MinMaxScaler()
        closeness_scaler = MinMaxScaler()

        normalized_degree = degree_scaler.fit_transform(np.array(degree_values).reshape(-1, 1))
        normalized_degree2=normalized_degree.astype(float)
        normalized_closeness = closeness_scaler.fit_transform(np.array(closeness_values).reshape(-1, 1))
        normalized_closeness2=normalized_closeness.astype(float)

        # Combine the normalized values
        combined = {}
        for i, node in enumerate(degree_centrality.keys()):
            combined[node] = (
                0.5 * normalized_degree2[i][0] +  # Weight for degree centrality
                0.5 * normalized_closeness2[i][0]  # Weight for closeness centrality
            )
        combined2={}
        for node in combined:
            combined2[node]=combined[node].tolist()

        keys=list(combined2.keys())
        values=list(combined2.values())
        ascending_soreted_index=np.argsort(values)
        soreted_index=ascending_soreted_index[::-1]

        sorted_combined={keys[i]:values[i] for i in soreted_index}

        return sorted_combined



        


    def visualization(self):
        
        poss=nx.spring_layout(self.g_graph)
        fig, ax=plt.subplots(figsize=(6,8))
        nx.draw(self.g_graph, poss, with_labels=True,  node_color='skyblue',ax=ax)
        nx.draw_networkx_edge_labels(self.g_graph, poss, edge_labels={(u, v): f"{d['weight']}" for 
                                      u, v, d in self.g_graph.edges(data=True)},font_size=10, label_pos=0.5,ax=ax)
        plt.show()





if __name__=='__main__':
    g=Graph()
    
    #g.convert_graph()
    g.visualization()
    #g.degree(g.graph)
    #g.node_balance(g.graph)

    #print(g.combined(g.graph))
    