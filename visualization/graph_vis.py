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
	for node in g.get_nodes():
		input_names = ["{}{}".format(n, g.get_shape(n)) for n in node.input]
		print("Input Node:", file=writer)
		print(input_names, file=writer)
		print("Output Node:", file=writer)
		print(node.name, file=writer)
		print("Shape:", file=writer)
		print(g.get_shape(node.output[0]), file=writer)
		print('\n', file=writer)
	writer.close()