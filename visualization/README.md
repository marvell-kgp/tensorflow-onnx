###  Instructions to extract metadata from frozen graph of tensorflow and converted ONNX graph

##### For extracting metadata of tensorflow graph 

* Run the default script to convert tf graph to onnx. For example, converting a LSTM graph, command would be :

  ```bash
  python3 -m tf2onnx.convert --input model/frozen_model.pb --inputs X:0 --outputs output:0 --output ./lstm.onnx --verbose
  ```


When you run script to convert model into its onnx version, metadata is dumped automatically in following file locations.

##### For extracting metadata of Tensorflow graph

* Code for extracting metadata(both nodes and dimesions) is in the following line:
  * [write_nodes(input_nodes_list, output_nodes_list, node_name_list, output_shapes, '/home/shivansh/dl/tensorflow-onnx/visualization/output/metadata/lstm_tf.txt')](https://github.com/marvell-kgp/tensorflow-onnx/blob/dbdbeb3b2ef3a9cf085bdc5bdce0704d15991f3b/tf2onnx/tfonnx.py#L126)
* Change the name of file to be dumped in accordingly.

##### For extracting metadata of ONNX graph

* Code for extracting metadata(both nodes and dimensions) in the following line:
  * [write_onnx(g, '/home/shivansh/dl/tensorflow-onnx/visualization/output/metadata/onnx_lstm_nodes.txt')](https://github.com/marvell-kgp/tensorflow-onnx/blob/dbdbeb3b2ef3a9cf085bdc5bdce0704d15991f3b/tf2onnx/tfonnx.py#L752)
  * Change the name of file to be dumped in accordingly.

