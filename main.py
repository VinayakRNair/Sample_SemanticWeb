from flask import Flask, request, jsonify
from flask_cors import CORS
import rdflib

app = Flask(__name__)
CORS(app)

g = rdflib.Graph()
g.parse("data\\PeriodicTable.owl")


@app.route('/periodictable/classifications/', methods=['GET'])
def allClassifications():
    result = []
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?ID)
        {
        ?c rdf:type table:Classification 
        }""")

    for row in qres:
        result.append(row['ID'].split("#")[1])
    result.sort()
    return jsonify({
        "classifications": {
            "all": result
        }
    })


@app.route('/periodictable/standard_states/', methods=['GET'])
def allStates():
    result = []
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?ID)
        { 
        ?c rdf:type table:StandardState
        }""")

    for row in qres:
        result.append(row['ID'].split("#")[1])
    result.sort()
    return jsonify({
        "states": {
            "all": result
        }
    })


@app.route('/periodictable/blocks/', methods=['GET'])
def allBlocks():
    result = []
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?ID)
        { 
        ?c rdf:type table:Block
        }""")

    for row in qres:
        result.append(row['ID'].split("#")[1])
    result.sort()
    return jsonify({
        "blocks": {
            "all": result
        }
    })


@app.route('/periodictable/groups/', methods=['GET'])
def allGroups():
    result = []
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?ID)
        { 
        ?c rdf:type table:Group
        }""")

    for row in qres:
        result.append(row['ID'].split("#")[1])
    result.sort()
    return jsonify({
        "groups": {
            "all": result
        }
    })


@app.route('/periodictable/periods/', methods=['GET'])
def allPeriods():
    result = []
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?ID)
        { 
        ?c rdf:type table:Period
        }""")

    for row in qres:
        result.append(row['ID'].split("#")[1])
    result.sort()
    return jsonify({
        "periods": {
            "all": result
        }
    })


@app.route('/periodictable/element/<string:sym>', methods=['GET'])
def getElement(sym):
    result = {}
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?n) as ?NAME) (str(?aN) as ?ATOMICNUMBER) (str(?aW) as ?ATOMICWEIGHT) (str(?g) as ?GROUP) 
        (str(?p) as ?PERIOD) (str(?b) as ?BLOCK) (str(?ss) as ?STANDARDSTATE) (str(?c) as ?COLOR) 
        (str(?cl) as ?CLASSIFICATION) (str(?cas) as ?CAS) 
        { 
        ?e rdf:type table:Element.
        ?e table:name ?n;
        table:symbol \"""" + sym + """\"^^xsd:string;
        OPTIONAL {?e table:atomicNumber ?aN }
        OPTIONAL {?e table:atomicWeight ?aW }
        OPTIONAL {?e table:group ?g }
        OPTIONAL {?e table:period ?p }
        OPTIONAL {?e table:block ?b }
        OPTIONAL {?e table:standardState ?ss }
        OPTIONAL {?e table:color ?c }
        OPTIONAL {?e table:classification ?cl }
        OPTIONAL {?e table:casRegistryID ?cas }.
        }""")
    for row in qres:
        result["name"] = row["NAME"] if row["NAME"] else "-"
        result["atomicNumber"] = row["ATOMICNUMBER"] if row["ATOMICNUMBER"] else "-"
        result["atomicWeight"] = row["ATOMICWEIGHT"] if row["ATOMICWEIGHT"] else "-"
        result["block"] = row["BLOCK"].split("#")[1] if row["BLOCK"] else "-"
        result["casRegistryID"] = row["CAS"] if row["CAS"] else "-"
        result["classification"] = row["CLASSIFICATION"].split("#")[1] if row["CLASSIFICATION"] else "-"
        result["color"] = row["COLOR"] if row["COLOR"] else "-"
        result["group"] = row["GROUP"].split("#")[1] if row["GROUP"] else "-"
        result["period"] = row["PERIOD"].split("#")[1] if row["PERIOD"] else "-"
        result["standardState"] = row["STANDARDSTATE"].split("#")[1] if row["STANDARDSTATE"] else "-"
        result["symbol"] = sym
    return jsonify(result)


@app.route('/periodictable/elements/', methods=['GET'])
def getAllElements():
    result = []
    qres = g.query(
        """
            PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
            PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
            SELECT (str(?s) as ?SYMBOL)
            { 
            ?e rdf:type table:Element.
            ?e table:symbol ?s;
            }""")
    for row in qres:
        result.append(row['SYMBOL'])
    
    return jsonify({
        "elements": {
            "all": result
        }
    })


@app.route('/periodictable/element/fetch', methods=['POST'])
def fetchElements():
    request_data = request.get_json(force=True)

    classification = request_data.get("classification", "all")
    standard_state = request_data.get("standardState", "all")
    block = request_data.get("block", "all")
    group = request_data.get("group", "all")
    period = request_data.get("period", "all")

    print(classification, standard_state, block, group, period)

    query_string = 'PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>' \
                   'PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>' \
                   'PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>' \
                   'SELECT (str(?s) as ?SYMBOL)' \
                   '{ ?e'
    result = []

    if not classification == "all":
        query_string += """table:classification table:""" + classification + ";"
    if not standard_state == "all":
        query_string += """table:standardState table:""" + standard_state + ";"
    if not block == "all":
        query_string += """table:block table:""" + block + ";"
    if not group == "all":
        query_string += """table:group table:""" + group + ";"
    if not period == "all":
        query_string += """table:period table:""" + period + ";"

    query_string += """table:symbol ?s }"""
    print(query_string)
    qres = g.query(query_string)

    if request_data == {}:
        return getAllElements

    for row in qres:
        result.append(row["SYMBOL"])

    print(result)
    return jsonify({"elements": {
        "all": result
    }})


if __name__ == '__main__':
    app.run(debug=True)
