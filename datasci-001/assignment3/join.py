import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key_id = record[1]
    table = record[0]
    mr.emit_intermediate(key_id, {table:record})

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # print list_of_values
    order = []
    line = []
    for v in list_of_values:
      # print v ,"\n\n"
      if v.has_key('order'):
        order.append(v["order"])
      else:
        line.append(v["line_item"])
    # print order,"\n", line
    for o in order:
      for l in line:
        mr.emit(o+l)

    # print "----------------------------"


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
