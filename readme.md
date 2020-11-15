# adaptive-huff
  
## About 

The code is for experimenting adaptive huffman compression with some raw data images.  
(ie. Baboon and lena in raw,halftone and binary color)

## How to run 

### Environment  

* Visual Studio Code
* Poetry 1.0.10 or later

### Step 
1. Clone this repository to local
2. Open the root directory.
``` bash
cd adaptive_huffman_coding
```
3. Install the dependencies with Poetry.
``` bash
poetry install --no-root
```
4. Run main.py
``` bash
python3 main.py
```

### Data Structure

Use a DAG, which has 2 children and parent pointer for every node, to implement Huffman tree. The code of a node is generated when we search for it (`Tree.search()` in class `Tree` of [`tree.py`](/adaptive_huffman/tree.py)), and thus the code for every node will not be updated when exchanging or appending. Furthermore, we use an array (`self.all_nodes` in class `AdaptiveHuffman` of [`ada_huffman.py`](/adaptive_huffman/ada_huffman.py)) to keep track of each node within the tree. By doing this, we could search a node within the tree iteratively instead of recursively traversal.
 

## Experiment statistic

Baboon 
  
![Baboon](https://github.com/yppan/rusty-classic-huffman-for-img/blob/main/Data/PNG/baboon.png)

| Image(256*256)  | Entropy(bit) | Before(byte) | After(byte) -without header | Header(byte) | Compression Rate |
|-----------------|--------------|--------------|-----------------------------|--------------|------------------|
| baboon_b        | 0.96909      | 65536        | 11446                       | 4            | 82.53%           |
| baboon_halftone | 0.96136      | 65536        | 11347                       | 4            | 82.68%           |
| baboon_raw      | 7.24065      | 65536        | 59828                       | 146          | 8.71%            |

Lena 
  
![Lena](https://github.com/yppan/rusty-classic-huffman-for-img/blob/main/Data/PNG/lena.png)

| Image(256*256)  | Entropy(bit) | Before(byte) | After(byte) -without header | Header(byte) | Compression Rate |
|-----------------|--------------|--------------|-----------------------------|--------------|------------------|
| lena_b          | 0.96968      | 65536        | 11454                       | 4            | 82.52%           |
| baboon_halftone | 0.83681      | 65536        | 10380                       | 4            | 84.16%           |
| baboon_raw      | 7.59536      | 65536        | 62832                       | 214          | 4.13%            |
