# ascii pattern recreation challenge

all the following ascii grid patterns are visual artworks within rectangular grid canvases, and therefore  MUST BE viewed with a monospaced font. This allows for the patterns, and the transformations from inputs to outputs, to be understood

Rules govern the transformation of the input patterns into the output patterns. Your task is to understand these rules so that you can create a new output from a given challenge input.

## Pattern examples

## Training Inputs

### Input 1
```ascii
+-------+
| X   X |
|XX   XX|
|       |
|XX   XX|
| X   X |
+-------+
```

### Input 2
```ascii
+-------+
|##   ##|
|      #|
|       |
| #   # |
|#     #|
+-------+
```

### Input 3
```ascii
+-------+
|%%   % |
|     %%|
|       |
|       |
|%     %|
+-------+
```

### Input 4
```ascii
+-------+
|%     %|
|       |
|       |
|       |
|%    %%|
+-------+
```

### Input 5
```ascii
+-------+
| @   @ |
|@     @|
|       |
|       |
|      @|
+-------+
```

## Training Outputs

### Output 1
```ascii
+---+
| X |
|XXX|
| X |
+---+
```

### Output 2
```ascii
+---+
|###|
| ##|
|# #|
+---+
```

### Output 3
```ascii
+---+
|%% |
| %%|
|% %|
+---+
```

### Output 4
```ascii
+---+
|% %|
|   |
|%%%|
+---+
```

### Output 5
```ascii
+---+
| @ |
|@ @|
|  @|
+---+
```

## Challenge

### Input
```ascii
+-------+
|     **|
|*      |
|       |
|       |
| *    *|
+-------+
```


Produce a single code block with the language indicated as ascii as your response. Then reflect on that code block. Reason aloud. Consider how both how it does, and does not reflect the examples you were given. Think about the images holistically, and try to come up with a rule or rules for the transformation that applies to all of the training examples. Then make a final attempt, again produce a single code block with the language indicated as ascii as your response.
