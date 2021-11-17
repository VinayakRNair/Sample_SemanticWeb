import rdflib

g = rdflib.Graph()
g.parse("..\\data\\PeriodicTable.owl")
print("graph has %s statements." % len(g))

# qres = g.query(
# """
# PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
# PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
# SELECT (str(?c) as ?ID)
# { 
# ?c rdf:type table:Classification
# }""")

# for row in qres:
#   print("%s"% row['ID'].split("#")[1])

qres = g.query(
"""
PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>SELECT (str(?s) as ?SYMBOL){ ?etable:classification table:Metallic;table:standardState table:liquid;table:symbol ?s }""")
for row in qres:
  print("%s"% row["SYMBOL"])


# qres = g.query(
# """
# PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
# PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
# SELECT (str(?s) as ?SYMBOL)
# { 
# ?e rdf:type table:Element.
# ?e table:symbol ?s;
# }""")

# print(len(qres))
# for row in qres:
#   print("%s" % row)

# symbol="He"
# qres = g.query(
# """
# PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
# PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
# SELECT (str(?n) as ?NAME) (str(?aN) as ?ATOMICNUMBER) (str(?aW) as ?ATOMICWEIGHT) (str(?g) as ?GROUP) (str(?p) as ?PERIOD) (str(?b) as ?BLOCK) (str(?ss) as ?STANDARDSTATE) (str(?c) as ?COLOR) (str(?cl) as ?CLASSIFICATION) (str(?cas) as ?CAS) 
# { 
# ?e rdf:type table:Element.
# ?e table:name ?n;
#    table:symbol \""""+symbol+"""\"^^xsd:string;
#    OPTIONAL {?e table:atomicNumber ?aN }
#    OPTIONAL {?e table:atomicWeight ?aW }
#    OPTIONAL {?e table:group ?g }
#    OPTIONAL {?e table:period ?p }
#    OPTIONAL {?e table:block ?b }
#    OPTIONAL {?e table:standardState ?ss }
#    OPTIONAL {?e table:color ?c }
#    OPTIONAL {?e table:classification ?cl }
#    OPTIONAL {?e table:casRegistryID ?cas }.
# }""")

# # qres = g.query(
# # """
# # PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
# # PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# # PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
# # SELECT (str(?n) as ?NAME) (str(?aN) as ?ATOMICNUMBER) (str(?aW) as ?ATOMICWEIGHT) (str(?g) as ?GROUP) (str(?p) as ?PERIOD) (str(?b) as ?BLOCK) (str(?ss) as ?STANDARDSTATE) (str(?c) as ?COLOR) (str(?cl) as ?CLASSIFICATION) (str(?cas) as ?CAS) 
# # { 
# # ?e rdf:type table:Element.
# # ?e table:name ?n;
# #    table:symbol "Uut"^^xsd:string;
# #    table:atomicNumber ?aN;
# #    table:atomicWeight ?aW;
# #    table:group ?g;
# #    table:period ?p;
# #    table:block ?b;
# #    table:standardState ?ss;
# #    table:color ?c;
# #    table:classification ?cl;
# #    table:casRegistryID ?cas.
# # }""")

# for row in qres:
#   print("NAME: ",row["NAME"])
#   print("ATOMICNUMBER: ",row["ATOMICNUMBER"])
#   print("ATOMICWEIGHT: ",row["ATOMICWEIGHT"])
#   print("GROUP: ",row["GROUP"].split("#")[1])
#   print("PERIOD: ",row["PERIOD"].split("#")[1])
#   print("BLOCK: ",row["BLOCK"].split("#")[1])
#   print("STANDARDSTATE: ",row["STANDARDSTATE"].split("#")[1])
#   print("COLOR: ",row["COLOR"])
#   print("CLASSIFICATION: ",row["CLASSIFICATION"].split("#")[1])
#   print("CAS: ",row["CAS"])

