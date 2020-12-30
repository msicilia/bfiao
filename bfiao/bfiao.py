from owlready2 import *
from util import *


# Locations of used ontologies and serialization format transforms. 
bfo_url = "http://purl.obolibrary.org/obo/bfo.owl"
cco_url = "https://raw.githubusercontent.com/CommonCoreOntology/CommonCoreOntologies/master/cco-merged/MergedAllCoreOntology_v1.3.ttl"
cco_location = "cco.nt"
turtle_to_nt(cco_location, cco_location)
ogc_gml_location = "gml_32_geometries.rdf.xml" # Local copy removing dc import that raised owlready2 parsing error.

# Load the used ontologies and get the references to the namespaces required. 
bfo_ont = get_ontology(bfo_url).load()
bfo = bfo_ont.get_namespace("http://purl.obolibrary.org/obo/")
cco_ont = get_ontology("cco.nt").load()
cco = cco_ont.get_namespace("http://www.ontologyrepository.com/CommonCoreOntologies/")
ogc_gml_ont = get_ontology(ogc_gml_location).load()
gml = ogc_gml_ont.get_namespace("http://www.opengis.net/ont/gml")
geosparql = ogc_gml_ont.get_namespace("http://www.opengis.net/ont/geosparql")

# The ontology defined here:
bfiao = get_ontology("https://w3id.org/bfiao")
bfiao.base_iri = "https://w3id.org/bfiao/"



#print(list(bfiao.annotation_properties()))
#with bfiao:
#    class my_annotation(AnnotationProperty):
#        pass


#bfiao.my_annotation = "Hello"
#print(list(bfiao.annotation_properties()))
#print(list(bfo_ont.annotation_properties()))


class Node(bfo.BFO_0000141):
    """
       subclass_of: http://purl.obolibrary.org/obo/BFO_0000141 (immaterial entity)
    """
    namespace = bfiao  
    comment = "An immaterial entity defining an area of interest in an unfolding situation."
    editor_note = "Nodes are defined for a purpose of tracking typically under some form of geospatial-based \
                  visualization."

class geo_location(Thing >> geosparql.Geometry):
    """The (current) geospatial location of something
    """
    namespace = bfiao

class defined_by(Thing >> bfo.BFO_0000040):
    """
       range: http://purl.obolibrary.org/obo/BFO_0000040 (material entity)
    """
    namespace = bfiao

class InfrastructureNode(Node):
    namespace = bfiao
    comment = "A Node in the unfolding situation that includes an infrastructural element inside its geospatial \
               boundaries."
    equivalent_to = [Node & defined_by.exactly(1, cco.Infrastructure)] 

class member_part_of(bfo.BFO_0000030 >> bfo.BFO_0000027):
    """
       domain: http://purl.obolibrary.org/obo/BFO_0000030 (object)
       range: http://purl.obolibrary.org/obo/BFO_0000027 (object aggregate)
    """
    namespace = bfiao
    comment = "this is the member part of relation as defined in BFO."

class InfrastructureAggregate(bfo.BFO_0000027):
    """
       subclass_of: http://purl.obolibrary.org/obo/BFO_0000027 (object aggregate)
       used in axiom: 

    """
    namespace = bfiao
    comment = ""
    # equivalent_to = [bfo.BFO_0000027 & member_part_of.all(cco.Infrastructure)]