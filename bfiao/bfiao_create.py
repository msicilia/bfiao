from owlready2 import *

bfo = get_ontology("http://purl.obolibrary.org/obo/bfo.owl").load()
onto = get_ontology("https://uah.es/ont/bfiao.owl")
onto.imported_ontologies.append(bfo)

class Domain(Thing):
    namespace = onto  
    comment = "A conceptual space related to some infrastructure."

class Node(Thing):
    namespace = onto
    comment = "A geospatial entity of interest for an unfolding situation."

class Connection(Thing):
    namespace = onto
    comment = "A relation between two nodes that entail some cascading effect in unfolding situations."

class has_domain(ObjectProperty):
    namespace = onto
    domain    = [Node]
    range     = [Domain]

class has_connection(ObjectProperty):
    namespace = onto
    domain    = [Node]
    range     = [Connection]

class Event(Thing):
    namespace = onto    

class Connection(Thing):
    namespace = onto

class Trajectory(Thing):
    namespace = onto



print(list(onto.classes()))
print(list(bfo.classes()))


onto.save("bfiao.nt", "ntriples")
