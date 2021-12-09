import hashlib
import json
import networkx as nx
import matplotlib.pyplot as plt

#Create Nodes that are build just like in Blockchain, each node is encrypted and their hashes remind the previous nodes

data = { 
    'name': "Genesis",
    'Age': "2021-12-08",
    'index': 0,
}

def hashes(data):
    stringfy = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(stringfy).hexdigest()


result = hashes(data)

#######################################################

data1 = { 
    'previousHash': result,
    'index': 1,
}

def hashes1(data1):
    stringfy = json.dumps(data1, sort_keys=True).encode()
    return hashlib.sha256(stringfy).hexdigest()


result1 = hashes1(data1)

########################################################

data2 = { 
    'previousHash': result1,
    'index': 2,
}

def hashes2(data2):
    stringfy = json.dumps(data2, sort_keys=True).encode()
    return hashlib.sha256(stringfy).hexdigest()


result2 = hashes2(data2)

##############################################################

data3 = { 
    'previousHash': result2,
    'index': 3,
}

def hashes3(data3):
    stringfy = json.dumps(data3, sort_keys=True).encode()
    return hashlib.sha256(stringfy).hexdigest()


result3 = hashes3(data3)

#################################################################

data4 = { 
    'previousHash': result3,
    'index': 4,
}

def hashes4(data4):
    stringfy = json.dumps(data4, sort_keys=True).encode()
    return hashlib.sha256(stringfy).hexdigest()


result4 = hashes4(data4)

#Building the Graph with all the nodes

graph = nx.DiGraph()
graph.add_node(result)

graph.add_edges_from([(result1, result), (result2, result), (result3, result), (result4, result)])

#Plot the graph

plt.figure(figsize=(10, 10))

options = {
    'node_color': 'green',
    'node_size': 500,
    'width': 2,
}

nx.draw_shell(graph, with_labels=True, **options)


