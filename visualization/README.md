###  Instructions to extract metadata from frozen graph of tensorflow and converted ONNX graph

##### For extracting metadata of tensorflow graph 

* Run the default script to convert tf graph to onnx. For example, converting a LSTM graph, command would be :

  ```bash
  python3 -m tf2onnx.convert --input model/frozen_model.pb --inputs X:0 --outputs output:0 --output ./lstm.onnx --verbose
  ```

* Code for extracting metadata is in the following place:
  * For dimension/shape data of graph, one can change location of file in following location:
    * [write_str(output_shapes, '/home/shivansh/dl/tensorflow-onnx/visualization/lstm_nodes_dim.txt')](https://github.com/marvell-kgp/tensorflow-onnx/blob/30f77b3a07f8487caac1692683c727d0cc67d3e2/tf2onnx/tfonnx.py#L72)
  * For getting nodes and edges metadata, one can change location of file in following location:
    * [write_nodes(input_nodes_list, output_nodes_list, '/home/shivansh/dl/tensorflow-onnx/visualization/lstm_nodes.txt')](https://github.com/marvell-kgp/tensorflow-onnx/blob/30f77b3a07f8487caac1692683c727d0cc67d3e2/tf2onnx/tfonnx.py#L123)

##### For extracting metadata of ONNX graph

* Code for extracting metadata(both nodes and dimensions) in the following place:
  * [write_onnx(g, '/home/shivansh/dl/tensorflow-onnx/visualization/onnx_lstm_nodes.txt')](https://github.com/marvell-kgp/tensorflow-onnx/blob/30f77b3a07f8487caac1692683c727d0cc67d3e2/tf2onnx/tfonnx.py#L738)

