# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qgWbxuigcG4kDftUWC6FbUSamyBDu4hv

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
from rdflib.plugins.sparql import prepareQuery
#RDFLib
ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

#SPARQL
q1 = prepareQuery('''
  SELECT ?a WHERE { 
    ?a rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = { "ns": ns}
)
for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
#RDFLib
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  print(s)
#SPARQL
q2 = prepareQuery('''
  SELECT ?a WHERE { 
    ?a rdf:type ns:Person. 
  }
  ''',
  initNs = { "ns": ns}
)
# Visualize the results
for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
#RDFLib
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for x, y, z in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s, x) 
#SPARQL
q3 = prepareQuery('''
  SELECT ?a WHERE { {
    ?a rdf:type ns:Person.} 
  UNION{?b rdfs:subClassOf ns:Person. ?a rdf:type ?b}}
  ''',
  initNs = {"rdf":RDF ,"ns": ns}
)
# Visualize the results
for r in g.query(q3):
  print(r)