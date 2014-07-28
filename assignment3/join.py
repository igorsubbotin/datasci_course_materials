import MapReduce
import sys
import os

mr = MapReduce.MapReduce()

def mapper(record):
    id = record[1]
    mr.emit_intermediate(id, record)

def reducer(key, list_of_values):
    leftName = None
    left = []
    right = []
    for v in list_of_values:
        type = v[0]
        if leftName is None:
            leftName = type
        if type == leftName:
            left.append(v)
        else:
            right.append(v)
    result = []
    for l in left:
        for r in right:
            mr.emit(l + r)

if __name__ == '__main__':
  inputdata = open(os.path.join("data", sys.argv[1]))
  mr.execute(inputdata, mapper, reducer)
