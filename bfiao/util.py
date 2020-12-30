
from rdflib import Graph


def turtle_to_nt(location, outfile):
    """Transforms the ontology in N3 in the URI location to the local file outfile in NTriples.
    """
    g = Graph()
    g.parse(location, format="n3")
    with open("cco.nt", "wb") as f:
        f.write(g.serialize(format="nt"))

