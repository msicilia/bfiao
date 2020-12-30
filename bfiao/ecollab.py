from owlready2 import *

bfiao_import = get_ontology("bfiao.nt").load()

bcollab = get_ontology("https://uah.es/ont/bcollab.owl")
bcollab.imported_ontologies.append(bfiao_import)


class Partner(Thing):
    namespace = bcollab  
    comment = "An organization collaborating in the prevention, mitigation or recovery from an emergency situation."

# Nodes are defined by Partners or Persons working for partners. 

class Plan(Thing):
    namespace = bcollab  
    comment = "The specificaction of activities as a reaction to events or information."

