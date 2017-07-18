import rdflib
import sys

source = sys.argv[1]
target = sys.argv[2]

g1 = rdflib.ConjunctiveGraph()
g1.parse(source, format="nt")

g2 = rdflib.ConjunctiveGraph()
g2.parse(target, format="nt")

from rdflib.compare import graph_diff
both, first, second = graph_diff(g1, g2)
print("both: {}, first: {}, second: {}".format(len(both), len(first), len(second)))
