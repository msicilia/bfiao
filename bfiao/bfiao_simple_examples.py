from owlready2 import *

bfiao = get_ontology("bfiao").load()
ogc_gml_location = "gml_32_geometries.rdf.xml" 
ogc_gml_ont = get_ontology(ogc_gml_location).load()
gml = ogc_gml_ont.get_namespace("http://www.opengis.net/ont/gml")
cco_ont = get_ontology("cco.nt").load()
cco = cco_ont.get_namespace("http://www.ontologyrepository.com/CommonCoreOntologies/")
bfo_url = "http://purl.obolibrary.org/obo/bfo.owl"
bfo_ont = get_ontology(bfo_url).load()


def an_infrastructure_node():
    with bfiao:
        a_node = bfiao.Node("Vandellos_nuclear_plant_node")
        some_infra = cco.Infrastructure("Vandellos_nuclear_plant")
        a_node.defined_by = [some_infra]
        a_geom = gml.Point("geoloc1")
        some_infra.geo_location = [a_geom]
    return a_node


def a_spatial_location():
    pass

def a_boundary_related_to_an_infrastructure():
    pass


def an_infrastructure_aggregate():
    pass


def main():
    a_node = an_infrastructure_node()
    print(a_node.is_a)
    # close_world(bfiao.Node)
    sync_reasoner([bfiao])
    print(a_node.is_a)

if __name__ == "__main__":
    main()
