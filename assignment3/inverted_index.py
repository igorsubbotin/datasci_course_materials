import MapReduce
import sys
import os
from sets import Set

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    total = Set()
    for v in list_of_values:
      total.add(v)
    mr.emit((key, list(total)))

if __name__ == '__main__':
  inputdata = open(os.path.join("data", sys.argv[1]))
  mr.execute(inputdata, mapper, reducer)
