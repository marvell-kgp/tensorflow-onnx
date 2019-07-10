###  Instructions to extract metadata from frozen graph of tensorflow and converted ONNX graph

##### For extracting metadata of tensorflow graph 

* Run the default script with `-- metadata_dir` to convert tf graph to onnx. For example, converting a LSTM graph, command would be :

  ```bash
  python3 -m tf2onnx.convert --input model/frozen_model.pb --inputs X:0 --outputs output:0 --output ./lstm.onnx --metadata_dir visualization/output/metadata
  ```


When you run script to convert model into its onnx version, metadata is dumped automatically `metadata_dir`.

##### For extracting metadata of Tensorflow graph

* File will be by default saved in json format as `tf_data.txt`.

##### For extracting metadata of ONNX graph

* File will be by default saved in json format as `onnx_data.txt`.
### Instruction to draw a graph from the json file

#### Requirements for python 2
- `pygraphviz 1.5`
- `networkx 2.2`
- `python 2.7`
- `pdftk`
- `sudo apt install default-jre-headless libcommons-lang3-java libbcprov-java`


#### Requirements for python 3
- `pygraphviz 1.5`
- `networkx 2.3`
- `python 3.6`
- `pdftk`

###### Instructuion to install pdftk
```bash
sudo add-apt-repository ppa:malteworld/ppa
sudo apt update
sudo apt install pdftk
```

#### Run the following commands
```bash
cd codes/drawing_graphs/
python convert_graph.py
```
```
usage: convert_graph.py [-h] [--jsonfile JSONFILE] [--output_dir OUTPUT_DIR]
                        [--output_file OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  --jsonfile JSONFILE   The metadata file (default:
                        ../../output/metadata/lstm_tf.txt)
  --output_dir OUTPUT_DIR
                        The output directory (default: ../../output/graphs/)
  --output_file OUTPUT_FILE
                        The output directory (default:
                        ../../output/graphs/lstm.pdf)

```
### Instruction to get the statistics
```bash
cd codes/drawing_graphs/
python graph_properties.py
```
```
usage: graph_properties.py [-h] [--jsonfile JSONFILE]
                           [--output_file OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  --jsonfile JSONFILE   The metadata file (default:
                        ../../output/metadata/lstm_tf.txt)
  --output_file OUTPUT_FILE
                        The output directory (default:
                        ../../output/graphs/lstm.csv)
```
