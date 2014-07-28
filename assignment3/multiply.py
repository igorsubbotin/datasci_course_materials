import MapReduce
import sys
import os
from sets import Set

mr = MapReduce.MapReduce()

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    for k in range(5):
        if matrix == "a":
            mr.emit_intermediate((i, k), record)
        else:
            mr.emit_intermediate((k, j), record)

def reducer(key, list_of_values):
    a = [0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0]
    for record in list_of_values:
        matrix = record[0]
        i = record[1]
        j = record[2]
        value = record[3]
        if matrix == "a":
            a[j] = value
        else:
            b[i] = value
    result = 0
    for k in range(5):
        result += a[k]*b[k]
    mr.emit((key[0], key[1], result))

if __name__ == '__main__':
  inputdata = open(os.path.join("data", sys.argv[1]))
  mr.execute(inputdata, mapper, reducer)