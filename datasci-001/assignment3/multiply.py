import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
i = j = k = 5

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    row = record[1]
    col = record[2]
    value = record[3]
    if matrix == 'a':
        for t in range(0,k):
            mr.emit_intermediate((row,t),(matrix,col,value))
    else:
        for t in range(0,i):
            mr.emit_intermediate((t,col),(matrix,row,value))


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = {}
    b = {}
    for v in list_of_values:
        if v[0] == 'a':
            a[v[1]] = v[2]
        else:
            b[v[1]] = v[2]
    total = 0
    for k1 in a.keys():
        if b.has_key(k1):
            total += a[k1] * b[k1]

    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
