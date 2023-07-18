# Counting Triangles in a Figure

import math

li = [[1, 2, 3, 4],
      [2, 1, 3, 4],
      [3, 1, 2, 4],
      [4, 1, 2, 3]
      ]



def count(li):
    count = 0
    for i in range(len(li)):
        li_connections = li[i]
        current_node = li_connections[0]
        
        for j in range(1, len(li_connections)):
            connection = li_connections[j]
            li_2_connections = li[connection-1]
            
            for k in range(1, len(li_2_connections)):
                connection_2 = li_2_connections[k]
                if connection_2 in li_connections and connection_2 != current_node:
                    count += 1
    return count//6

def result(li, li_run):
    count_triangles = count(li)
    subtract = 0
    for sub_li in li_run:
        n = sub_li[0]
        multiply = sub_li[1]
        subtract += multiply*math.comb(n, 3)
        
    return count_triangles-subtract

def input_output():
    nodes = int(input("How many nodes are there in total?: "))
    li = []
    # nodes are numbered 1, 2, 3, ...
    for i in range(nodes):
        current_node = int(input("Enter the current node number: "))
        connections = str(input("Enter all the connections (space inbetween): "))
        li_connections = connections.split()
        for x in range(len(li_connections)):
            li_connections[x] = int(li_connections[x])
        li_connections.insert(0, current_node)
        li.append(li_connections)
        
    li_run = []
    
    runs = int(input("How many different length straight-line runs are there?: "))
    for j in range(runs):
        a = int(input("Enter the run length: "))
        b = int(input("Enter the frequency of this run length: "))
        li_run.append([a, b])
    
    print(result(li, li_run))
    
input_output()
