
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
    parser.add_argument("--output_file", type=str, default='../../output/graphs/lstm.csv', help="The output directory")
    args = parser.parse_args()
    return args



''' Calculate the types of nodes in the Graph'''
def type_of_operation(json_obj):
    op_type_index = defaultdict(int)
    for node in json_obj:
        op_name = node["op_name"]
        op_name_key = op_name.split("/")[-1].split("_")[0]
        op_type_index[op_name_key] += 1
    return op_type_index




if __name__ == '__main__':
    
    args = add_arguments()
    '''Loads the json objects'''

    str_json = open(args.jsonfile).read()
    json_obj = ast.literal_eval(str_json)
    
    type_dict = type_of_operation(json_obj)
    with open(args.output_file, "w") as f_w:
        for _type in type_dict.keys():
            f_w.write(_type+","+str(type_dict[_type])+"\n")
