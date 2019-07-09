
# coding: utf-8

# In[2]:

import json
import ast
import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from networkx.readwrite import json_graph
from collections import defaultdict
import os
import argparse

def add_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--jsonfile", type=str, default='../../output/metadata/lstm_tf.txt', help="The metadata file")
    parser.add_argument("--output_dir", type=str, default='../../output/graphs/', help="The output directory")
    parser.add_argument("--output_file", type=str, default='../../output/graphs/lstm.pdf', help="The output directory")
    args = parser.parse_args()
    return args

def node_prop(G, node, shape = 'oval', style = 'invisible', fillcolor = None):
    if fillcolor!=None:
        G.nodes[node]['fillcolor'] = fillcolor
    G.nodes[node]['shape'] = shape
    G.nodes[node]['style'] = style
    return G



''' Create indexes for nodes in a Graph'''
def create_index(json_obj):
    index_dict = defaultdict(int)
    count = 0

    input_list = []
    output_list = []


    for node in json_obj:
        op_name = node["op_name"]
        #Creating a index dictionary for integer node index
        if index_dict[op_name] == 0:
            count += 1
            index_dict[op_name] = count
            
        inputs = node["inputs"]
        if len(inputs) == 0:
            input_list.append(index_dict[op_name] - 1 )
        
        outputs = node["output"]
        if len(outputs) == 0:
            output_list.append(index_dict[op_name] - 1)
            
        else:
            for output in outputs:
                name = output["name"]
                index_dict[name] = index_dict[op_name]
    return (index_dict, input_list, output_list)


def create_subgraph_list(index_dict, input_list, output_list):
    subgraph_list = []
    #print(input_list, output_list)
    G1 = nx.DiGraph()
    edge_count = 0
    for node in json_obj:
        inputs = node["inputs"]
        op_name = node["op_name"]
        G1.add_node(index_dict[op_name] - 1,label=op_name.split("/")[-1], name=op_name)
        for _input in inputs:
            name = _input["name"]
            shape = _input["shape"]
            #print("name", name, "op_name", op_name, index_dict[name], index_dict[op_name])
            G1.add_edge(index_dict[name] - 1, index_dict[op_name] -1 ,label=shape)
            edge_count += 1
        if edge_count > 100:
            edge_count = 0
            in_degree = G1.in_degree()
            out_degree = G1.out_degree()
            for u in G1.nodes():
                if in_degree[u] == 0 :
                    if u not in input_list:
                        G1 = node_prop(G1, u, fillcolor = 'pink', shape = 'octagon', style = 'filled' )
                    else:
                        G1 = node_prop(G1, u, fillcolor = 'grey', shape = 'octagon', style = 'filled' )
                if out_degree[u] == 0:
                    if u not in output_list:
                        G1 = node_prop(G1, u, fillcolor = 'pink', shape = 'octagon', style = 'filled' )
                    else:
                        G1 = node_prop(G1, u, fillcolor = 'lightblue', shape = 'octagon', style = 'filled' )
            subgraph_list.append(G1)
            G1 = nx.DiGraph()

    return subgraph_list

if __name__ == '__main__':
    
    args = add_arguments()
    '''Loads the json objects'''

    str_json = open(args.jsonfile).read()
    json_obj = ast.literal_eval(str_json)
    index_dict, input_list, output_list = create_index(json_obj)
    subgraph_list = create_subgraph_list(index_dict, input_list, output_list)

    i = 0
    files_to_be_concatenated = ''
    for G in subgraph_list:
        write_dot(G,args.output_dir+"test"+str(i)+".dot")
        os.system("dot -Tpdf " + args.output_dir+"test"+str(i)+".dot" + " -o "+args.output_dir+"graph"+str(i)+".pdf") 
        files_to_be_concatenated += " "+args.output_dir+"graph"+str(i)+".pdf"
        i += 1
    os.system("pdftk  "+ files_to_be_concatenated +" cat output " + args.output_file)
    #i+=1