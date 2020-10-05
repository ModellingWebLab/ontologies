# Web Lab Ontologies

A central home for ontology definition files which define metadata tags used to label CellML files. The labelled CellML files can then be used by both [Chaste](https://chaste.cs.ox.ac.uk/trac/wiki) and the [ModellingWebLab](www.github.com/ModellingWebLab) by them referring to this central ontology repository.

`oxford_metadata.ttl` is the human-readable file which should be updated.

After updates, run 
`python ttl2rdf.py oxford-metadata.ttl oxford-metadata.rdf`
to update the RDF file to match, and commit both.

This should now work with python3.
