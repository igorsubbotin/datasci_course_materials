import MapReduce
import sys
import os
from sets import Set

mr = MapReduce.MapReduce()

def mapper(record):
    name1 = record[0]
    name2 = record[1]
    mr.emit_intermediate(name1, name2)
    mr.emit_intermediate(name2, name1)

def reducer(name, list_of_values):
    result = {}
    for v in list_of_values:
        key = (name, v)
        if key not in result:
            result[key] = 0
        result[key] += 1
    for key in result:
        if result[key] == 1:
            mr.emit(key)

if __name__ == '__main__':
  inputdata = open(os.path.join("data", sys.argv[1]))
  mr.execute(inputdata, mapper, reducer)
