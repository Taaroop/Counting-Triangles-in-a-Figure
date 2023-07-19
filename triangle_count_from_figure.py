# Counting Triangles in a Figure

import math

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
    for i in range(1, nodes+1):
        connections = str(input("Enter all the connections for Node" + " " + str(i)+ " (with space in-between): "))
        li_connections = connections.split()
        for x in range(len(li_connections)):
            li_connections[x] = int(li_connections[x])
        li_connections.insert(0, i)
        li.append(li_connections)
        
    li_run = []
    
    runs = int(input("How many different length straight-line runs are there?: "))
    for j in range(runs):
        a = int(input("Enter the run length (must be greater than or equal to 3): "))
        b = int(input("Enter the frequency of this run length: "))
        li_run.append([a, b])
    
    print("Total number of triangles in the figure:", result(li, li_run))
    
input_output()
