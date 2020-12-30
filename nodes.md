# Nodes and infrastructures in bfiao


## Context

In an unfolding emergency situation there is always a geospatial zone of interest for situational awareness. However, that zone need not be determined explicitly as a fixed region of space, but it is often (and more conveniently) defined implicitly. 

For example, that determination in a concrete situation may be done via:

* The infrastructure elements that are *close to* the occurence of an adverse event, e.g. a forest fire start.
* A pre-selection of some important infrastructure objects, e.g. a nuclear power plant.

In consequence, the focus (or foci) of interest is/are defined via the concept of a *node*. Introducing a generic term *node* is done to provide a emergency management-specific entity that can be used to relate different kinds of elements of interest flexibly. 

## Nodes are geospatial areas of interest

A node is an *immaterial* entity in the sense of BFO. In our case, these entities are defined by some operator (be it human or software), but this is defined outside of `bfiao`. 

### Nodes as spatial regions

One of the two categories of immaterial objects in BFO are *spatial regions* which exist independently of *material entities*, and which thus do not change.

We are concerned here with two subcategories of spatial regions:
* two-dimensional spatial region (a spatial area)
* three-dimensional spatial region(a spatial volume)

While in the real world the entities affected by an adverse event are three-dimensional, the kind of actions that an emergency management system deals with may deal from a pragmatic viewpoint just with spatial areas, ignoring the *altitude* dimension. 

### Nodes as related to material entities

In some cases, the entity of interest is not defined by a spatial region but defined in relation to some material entity. The following are examples of the two main categories.

* Boundaries (*continuant fiat boundaries* in BFO) are typically infrastructure elements, e.g. a particular power generation plant, or a town. 
* Sites in BFO are three-dimensional immaterial entities that are (partially  or wholly) bounded by a material entity, e.g. the interior of a plant or a tunnel. 

While both boundaries and sites can be used in `bfiao`, two-dimensional or three-dimensional boundaries are the most common ones.

Note that the main pragmatic difference in our case of *boundaries* and *spatial regions* is that the former include regions that move or change size. An example may be the boundaries of a town, but in this case, objects as towns change typically at a very low pace (as compared with the much shorter term time span of the management of an emergency) so in practical terms, many bounded entities may be used interchangeably with their spatial region. 

### Practical definition of nodes

Nodes are considered as such by external determination, e.g. by the interest of an operator. In most cases, nodes have (fixed or changing) Earth coordinates and that is a practical constraint of a model based on `bfiao`. Exceptions might be moving nodes, e.g. a fire extinction vehicle, that has at some moment an unknown location due to failure of communication means. 

The [GeoSPARQL](https://en.wikipedia.org/wiki/OGC_GeoSPARQL) models have been selected due to its association to standards and maturity. Concretely, nodes in `bfiao` can have associated GeoSPARQL instances of *Geometry*, which according to the documentation of the class, "is equivalent to the UML class GM_Object defined in ISO 19107, and it is superclass of all geometry types".

The *geometry* associated to a node may be given explicitly (e.g. when an operator "draws" an area of interest in a map) or be inferred from the geometries of the material entities associated to the nodes. 

###  Determination of the relation of material entities and spatial regions

The material entities and the immaterial entities described can be related in a pragmatic view using 
the coordinate frame of the Earth. In the case of nodes defined as *spatial regions* these have 


## Infrastructures are material objects considered important

The domain of emergency management is specially interested in infrastructures. The CCO contain a *Infrastructure* hierarchy that is reused in `bfiao`. As these are subsumed by CCO class *artifact*, which in 
turn is a BFO *object*, these infrastructures are *material entities* that can be used to define nodes as *boundaries* of those infrastructures.

### Infrastructures can be aggregates

Infrastructures are ofen grouped as collections of elements related by their function, e.g. in the case of the "electricity production" domain or "sector". The BFO *aggregate object* class can be used to represent those. 

