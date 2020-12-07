from owlready2 import *

bfo = get_ontology("http://purl.obolibrary.org/obo/bfo.owl").load()
timeo = get_ontology("time-ontology.owl").load()
# sweto = get_ontology("http://data.bioontology.org/ontologies/SWEET/submissions/10/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb").load()

bfiao = get_ontology("https://uah.es/ont/bfiao.owl")
bfiao.imported_ontologies.append(bfo)
bfiao.imported_ontologies.append(timeo)
class Domain(Thing):
    namespace = bfiao  
    comment = "A conceptual space related to some infrastructure."

# Como hacer una regla para nodo critico, que relaciona varios dominios. 
class Node(Thing):
    namespace = bfiao
    # location: bfo.Location
    # location: geonames.Geoposition
    comment = "A geospatial entity of interest for an unfolding situation."

class has_domain(ObjectProperty):
    namespace = bfiao
    domain    = [Node]
    range     = [Domain]


class Relation(Thing):
    namespace = bfiao
    comment = "Relations between nodes that may propagate effects in an unfolding emergency situation."

class has_relation(ObjectProperty):
    namespace = bfiao
    comment = "associates nodes with relations"
    domain    = [Node]
    range     = [Relation]
    # type: 

class has_physical_connection(has_relation):
    namespace = bfiao
    comment = "A kind of relation that entails a physical connection that may be affected or broken in an unfolding emergency situation."
    domain    = [Node]
    range     = [Connection]

class has_geolocated_relation(has_relation):
    pass

class has_connection(has_relation):
    namespace = bfiao
    comment = "[TODO]"
    domain    = [Node]
    range     = [Connection]
 

class Event(Thing): # (bfo.Event , timeo.Event)
    namespace = bfiao  
    comment = "A spatiotemporal ocurrence that is relevant to a situation and may affect nodes and/or some of their relations."

class PossibleEvent(Thing):
    namespace = bfiao    
    # estimatedPossibility: PossibilityEstimation
    comment = "An hypothesis of an event that may ocurr given a state of the situation."

class PossibilityEstimation(Thing):
    # source: Agent
    # event: PossibleEvent
    pass

class realized_in(ObjectProperty):
    namespace = bfiao
    comment = "The realization or materialization of an hypothesised event in an actual event. "
    domain    = [PossibleEvent]
    range     = [Event]
 
