import json
import sys
sys.path.append("../../../")
from tf2onnx import utils

def write(lists, filename):	
	writer = open(filename, 'w+')
	for idx, item in enumerate(lists):
		print(idx, file=writer)
		print(item, file=writer)

	writer.close()

def write_nodes(ops, filename):
	writer = open(filename, 'w+')
	list_output_nodes = []

	for node in ops:
		dict_node = {}
		dict_node['op_name'] = node.name.split(":")[0] if '/' in node.name else node.name

		output_list = []
		for node_output in node.outputs:
			output_dict = {}
			output_dict['name'] = node_output.name
			shape = utils.get_tf_tensor_shape(node_output)
			if (len(shape) > 0) and (shape[0] is None):
				shape[0] = -1
			output_dict['shape'] = shape
			output_list.append(output_dict)
		dict_node['output'] = output_list
# 

		input_list = []
		for node_input in node.inputs:
			input_dict = {}
			input_dict['name'] = node_input.name
			shape = utils.get_tf_tensor_shape(node_input)
			if (len(shape) > 0) and (shape[0] is None):
				shape[0] = -1
			input_dict['shape'] = shape
			input_list.append(input_dict)
		dict_node['inputs'] = input_list

		

		list_output_nodes.append(dict_node)

	outstr = str(list_output_nodes)
	outstr = outstr.replace("\'", "\"")
	parsed_json=json.loads(outstr)
	print(json.dumps(parsed_json, indent = 4,sort_keys=False), file=writer)
	# print(list_output_nodes, file=writer)
	writer.close()

def write_str(content, filename):	
	writer = open(filename, 'w')
	print(content, file=writer)
	writer.close()

def write_onnx(g, filename):
	writer = open(filename, 'w+')
	list_output = []
	for node in g.get_nodes():
		dict_node = {}
		dict_node['op_name'] = node.name.split(":")[0] if '/' in node.name else node.name

		output_list = []
		for output_name in node.output:
			output_dict = {}
			output_dict['name'] = output_name.split("[")[0]
			output_dict['shape'] = g.get_shape(output_name) 
			output_list.append(output_dict)
		dict_node['output'] = output_list

		input_list = []
		input_names = ["{}{}".format(n, g.get_shape(n)) for n in node.input]
		for input_name in input_names:
			input_node = {}
			input_node['name'] = input_name.split("[")[0]
			input_node['shape'] = input_name.split("[")[1].split("]")[0].replace("," , "").split()
			input_list.append(input_node)
		dict_node['inputs'] = input_list


		print(node.attr)

		list_output.append(dict_node)
                
		# print("Input Node:", file=writer)
		# print(input_names, file=writer)
		# print("Output Node:", file=writer)
		# print(node.name, file=writer)
		# print("Shape:", file=writer)
		# print(g.get_shape(node.output[0]), file=writer)
		# print(node.summary, file=writer)
	#print(str(list_output))	
	outstr = str(list_output)
	outstr = outstr.replace("\'", "\"")
	parsed_json=json.loads(outstr)
	print(json.dumps(parsed_json, indent = 4,sort_keys=False), file=writer)
	writer.close()
