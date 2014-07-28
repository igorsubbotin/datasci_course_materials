import MapReduce
import sys
import os
from sets import Set

mr = MapReduce.MapReduce()

def mapper(record):
    nucleotides = record[1][:-10]
    mr.emit_intermediate(nucleotides, 1)

def reducer(nucleotides, list_of_values):
    mr.emit(nucleotides)

if __name__ == '__main__':
  inputdata = open(os.path.join("data", sys.argv[1]))
  mr.execute(inputdata, mapper, reducer)
