def write(lists, filename):	
	writer = open(filename, 'w')
	for idx, item in enumerate(lists):
		print(idx, file=writer)
		print(item, file=writer)

	writer.close()

def write_nodes(list_input, list_output, filename):	
	writer = open(filename, 'w')
	for input_node, output_node in zip(list_input, list_output):
		print('Input Node:', file=writer)
		print(input_node, file=writer)
		print('Output Node:', file=writer)
		print(output_node, file=writer)

	writer.close()

def write_str(content, filename):	
	writer = open(filename, 'w')
	print(content, file=writer)
	writer.close()

def write_onnx(g, filename):
	writer = open(filename, 'w')
	list_output = []
	for node in g.get_nodes():
		# dict_node = {}
		# dict_node['op_name'] = node.name.split("/")[1] if '/' in node.name else node.name

		# output_dict = {}
		# output_dict['name'] = node.name
		# output_dict['shape'] = g.get_shape(node.output[0]) 
		# dict_node['output'] = output_dict

		# input_list = []
		# input_names = ["{}{}".format(n, g.get_shape(n)) for n in node.input]
		# for input_name in input_names:
		# 	input_node = {}
		# 	input_node['name'] = input_name.split("{")[0]
		# 	input_node['shape'] = input_name.split("[")[1].split("]")[0].replace("," , "").split()
		# 	input_list.append(input_node)
		# dict_node['inputs'] = input_list
		
		# list_output.append(dict_node)
		# print("Input Node:", file=writer)
		# print(input_names, file=writer)
		# print("Output Node:", file=writer)
		# print(node.name, file=writer)
		# print("Shape:", file=writer)
		# print(g.get_shape(node.output[0]), file=writer)
		print(node.summary, file=writer)
	# print(list_output, file=writer)
	writer.close()