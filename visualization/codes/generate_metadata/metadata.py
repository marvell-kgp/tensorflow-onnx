import json
import sys
sys.path.append("../../../")
from tf2onnx import utils
import tensorflow as tf

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
		attr_dictionary = dict(node.node_def.attr.items())

		dict_node = {}
		dict_node['op_name'] = node.name
		# try:
		# 	dict_node['dtype'] = utils.map_tf_dtype(utils.get_tf_node_attr(node, "dtype"))
		# except:
		# 	dict_node['dtype'] = None

		output_list = []
		for node_output in node.outputs:
			output_dict = {}
			output_dict['name'] = node_output.name.split(':')[0]
			shape = utils.get_tf_tensor_shape(node_output)
			if (len(shape) > 0) and (shape[0] is None):
				shape[0] = -1
			output_dict['shape'] = shape

			if(node_output.dtype.name is not None):
				output_dict['dtype'] = node_output.dtype.name
			else:
				output_dict['dtype'] = None

			output_list.append(output_dict)
		dict_node['output'] = output_list
#

		input_list = []
		for node_input in node.inputs:
			input_dict = {}
			input_dict['name'] = node_input.name.split(':')[0]
			shape = utils.get_tf_tensor_shape(node_input)
			if (len(shape) > 0) and (shape[0] is None):
				shape[0] = -1
			input_dict['shape'] = shape

			if(node_input.dtype.name is not None):
				input_dict['dtype'] = node_input.dtype.name
			else:
				input_dict['dtype'] = None

			input_list.append(input_dict)

		dict_node['inputs'] = input_list
		dict_node['operator_name'] = node.type
		# print(attr_dictionary.keys())

		## Code for extracting attributes in graph
		if('padding' in attr_dictionary.keys()):
			padding = attr_dictionary['padding'].s
			dict_node['padding'] = padding.decode("utf-8")
		else:
			dict_node['padding'] = "None"

		if('strides' in attr_dictionary.keys()):
			strides = attr_dictionary['strides'].list.i
			strides_list = [int(a) for a in strides]
			dict_node['strides'] = strides_list
		else:
			dict_node['strides'] = "None"

		if('dilations' in attr_dictionary.keys()):
			dilations = attr_dictionary['dilations'].list.i
			dilations_list = [int(a) for a in dilations]
			dict_node['dilations'] = dilations_list
		else:
			dict_node['dilations'] = "None"
		


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
		dict_node['op_name'] = node.name
		dict_node['operator_name'] = node.type
		output_list = []
		for node_output in node.output:
			output_dict = {}
			output_dict['name'] = g.get_node_by_output_in_current_graph(node_output).name
			if(g.get_shape(node_output) is not None):
				output_dict['shape'] = g.get_shape(node_output)
			else:
				output_dict['shape'] = "None"

			output_dict['dtype'] = g.get_dtype(node_output)
			# print(g.get_dtype(node_output))
			output_list.append(output_dict)
		dict_node['output'] = output_list

		input_list = []
		for node_input in node.input:
			input_node = {}
			input_node['name'] = g.get_node_by_output_in_current_graph(node_input).name
			if(g.get_shape(node_input) is not None):
				input_node['shape'] = g.get_shape(node_input)
			else:
				input_node['shape'] = "None"

			input_node['dtype'] = g.get_dtype(node_input)

			input_list.append(input_node)
		dict_node['inputs'] = input_list

		# Attributes of onnx graphs
		attr_dictionary = node.attr
		if('strides' in attr_dictionary.keys()):
			dict_node['strides'] = list(attr_dictionary['strides'].ints)
		else:
			dict_node['strides'] = "None"

		if('dilations' in attr_dictionary.keys()):
			dict_node['dilations'] = list(attr_dictionary['dilations'].ints)
		else:
			dict_node['dilations'] = "None"

		if('padding' in attr_dictionary.keys()):
			dict_node['padding'] = attr_dictionary['padding'].s.decode("utf-8")
		else:
			dict_node['padding'] = "None"


		list_output.append(dict_node)

	# 	# print("Input Node:", file=writer)
	# 	# print(input_names, file=writer)
	# 	# print("Output Node:", file=writer)
	# 	# print(node.name, file=writer)
	# 	# print("Shape:", file=writer)
	# 	# print(g.get_shape(node.output[0]), file=writer)
	# 	# print(node.summary, file=writer)
	# #print(str(list_output))
	outstr = str(list_output)
	outstr = outstr.replace("\'", "\"")
	parsed_json=json.loads(outstr)
	print(json.dumps(parsed_json, indent = 4,sort_keys=False), file=writer)
	writer.close()
