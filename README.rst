=====
bfiao
=====


.. image:: https://img.shields.io/pypi/v/bfiao.svg
        :target: https://pypi.python.org/pypi/bfiao

.. image:: https://img.shields.io/travis/msicilia/bfiao.svg
        :target: https://travis-ci.com/msicilia/bfiao

.. image:: https://readthedocs.org/projects/bfiao/badge/?version=latest
        :target: https://bfiao.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


The Basic Formal Infrastructure Assessment Ontology (BFiaO) is an ontology aimed at representing interoperable 
accounts of emergency management situations. As such, it is application type-specific (but not application-specific
since it is not created for a single concrete application).

The ecollab ontology is a companion ontology that uses the BFiaO and represents the organizations collaborating 
in an unfolding emergency situation. 

This package creates these ontologies programmatically using the owlready2 library and provides utilities for
their use.


* Free software: MIT license
* Documentation: https://bfiao.readthedocs.io.

Features
--------

* Uses the the `Basic Format Ontology (BFO) <https://basic-formal-ontology.org//>`_ and the `Common Core Ontologies (CCO) <https://github.com/CommonCoreOntology/CommonCoreOntologies>`_.
* Two layer modeling: geospatial regions or sites of interest separated from material objects, and implicitly tied by spatial locations.


Documentation
--------------

The following pages describe the main elements  of the `bfiao` ontology.

* Nodes and infrastructures.
* Events of interest.
* Projections of potential future events. 


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
