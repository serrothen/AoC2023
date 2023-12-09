#!/usr/bin/env python3

def fill_network(line,network):
    """Fill network with new node."""

    node_C = line.split("=")[0].strip()
    next_nodes = line.split("=")[1].strip(" ()").split(",")
    node_L = next_nodes[0]
    node_R = next_nodes[1].strip()
 
    network[node_C] = [node_L,node_R]
 
    return network


def step(node0,network,direction):
    """Take a step within the network in the given direction."""

    if (direction=="L"):
        node0 = network[node0][0]
    else:
        node0 = network[node0][1]

    return node0


#fname = "test1.txt"
#fname = "test2.txt"
fname = "input.txt"

network = dict()
destination="ZZZ"
num_steps = 0
arrived = False
with open(fname,"r") as file:

    # read path
    path = next(file).strip()
    path_len = len(path)
    path_pos = 0
    next(file).strip()
    
    # read center, left, right nodes
    line = next(file).strip()
    network = fill_network(line,network)
    
    # starting node
    node0 = [node_C for node_C in network.keys()][0]
    
    # take step
    if (node0 in network.keys()):
#        print(f"{num_steps}: {node0}: {path[num_steps%path_len]}")
        node0 = step(node0,network,path[num_steps])
        num_steps += 1
    
    # check arrival
    if (node0==destination):
        arrived = True
    
    while (not arrived):
        # read center, left, right nodes
        line = next(file).strip()
        network = fill_network(line,network)
        
        # take step
        while (node0 in network.keys()):
#            print(f"{num_steps}: {node0}: {path[num_steps%path_len]}")
            node0 = step(node0,network,path[num_steps%path_len])
            num_steps += 1
        
            # check arrival
            if (node0==destination):
                arrived = True
                break

print(num_steps)
