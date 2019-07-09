import json

def write(lists, filename):	
	writer = open(filename, 'w')
	for idx, item in enumerate(lists):
		print(idx, file=writer)
		print(item, file=writer)

	writer.close()

def write_nodes(list_input, list_output, list_node, output_shapes, filename):	
	writer = open(filename, 'w')
	list_output_nodes = []
	for input_names, output_names, node_name in zip(list_input, list_output, list_node):
		dict_node = {}
		dict_node['op_name'] = node_name

		output_list = []
		for output_name in output_names:
			output_dict = {}
			output_dict['name'] = output_name
			if output_shapes[output_name] is None:
				output_dict['shape'] = 'None'
			output_dict['shape'] = output_shapes[output_name]
			output_list.append(output_dict)
		dict_node['output'] = output_list

		input_list = []
		for input_name in input_names:
			input_node = {}
			input_node['name'] = input_name
			if output_shapes[input_name] is None:
				input_node['shape'] = 'None'
			input_node['shape'] = output_shapes[input_name]
			input_list.append(input_node)
		dict_node['inputs'] = input_list
		list_output_nodes.append(dict_node)


	# for input_node, output_node in zip(list_input, list_output):
	# 	print('Input Node:', file=writer)
	# 	print(input_node, file=writer)
	# 	print('Output Node:', file=writer)
	# 	print(output_node, file=writer)
	#print('*******************   ' + str(len(list_output)) )
	outstr = str(list_output)
	outstr = outstr.replace("\'", "\"")
	parsed_json=json.loads(outstr)
	print(json.dumps(parsed_json, indent = 4,sort_keys=False), file=writer)
	#print(list_output_nodes, file=writer)
	writer.close()

def write_str(content, filename):	
	writer = open(filename, 'w')
	print(content, file=writer)
	writer.close()

def write_onnx(g, filename):
	writer = open(filename, 'w')
	list_output = []
	for node in g.get_nodes():
		dict_node = {}
		dict_node['op_name'] = node.name.split("/")[1] if '/' in node.name else node.name

		output_list = []
		for name in node.output:
			output_dict = {}
			output_dict['name'] = name
			output_dict['shape'] = g.get_shape(name) 
			output_list.append(output_dict)
		dict_node['output'] = output_list

		input_list = []
		input_names = ["{}{}".format(n, g.get_shape(n)) for n in node.input]
		for input_name in input_names:
			input_node = {}
			input_node['name'] = input_name.split("{")[0]
			input_node['shape'] = input_name.split("[")[1].split("]")[0].replace("," , "").split()
			input_list.append(input_node)
		dict_node['inputs'] = input_list
		
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
