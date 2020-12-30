from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

with onto:
    class Drug(Thing):
        def take(self): print("I took a drug")

    class ActivePrinciple(Thing):
        pass

    class has_for_active_principle(Drug >> ActivePrinciple):
        python_name = "active_principles"

    class SingleActivePrincipleDrug(Drug):
        equivalent_to = [Drug & has_for_active_principle.exactly(1, ActivePrinciple)]
        def take(self): print("I took a drug with a single active principle")

acetaminophen   = ActivePrinciple("acetaminophen")
amoxicillin     = ActivePrinciple("amoxicillin")
clavulanic_acid = ActivePrinciple("clavulanic_acid")

# AllDifferent([acetaminophen, amoxicillin, clavulanic_acid])

drug1 = Drug(active_principles = [acetaminophen])
drug2 = Drug(active_principles = [amoxicillin, clavulanic_acid])
drug3 = Drug(active_principles = [])

close_world(Drug)
sync_reasoner()
