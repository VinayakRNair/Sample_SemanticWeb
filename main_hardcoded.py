from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/periodictable/standard_states/', methods=['GET'])
def all_state():
    return jsonify({
        "states": {
            "all": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
                    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I",
                    "Xe", "Cs", "Ba", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
                    "At", "Rn", "Fr", "Ra", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
                    "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
                    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"]
        }
    })


@app.route('/periodictable/standard_state/<string:state>/', methods=['GET'])
def specific_state(state):
    return jsonify({
        "states": {
            "solid": ["O", "Cl", "Ar", "H", "He"],
            "liquid": ["C", "Cl", "Ar", "H", "He"],
            "gas": ["C", "N", "O", "H", "He"],
            "unknown": ["Ar", "H", "He"]
        }
    })


@app.route('/periodictable/classifications/', methods=['GET'])
def all_class():
    return jsonify({
        "class": {
            "all": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
                    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I",
                    "Xe", "Cs", "Ba", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
                    "At", "Rn", "Fr", "Ra", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
                    "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
                    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"]
        }
    })


@app.route('/periodictable/classification/<string:clss>/', methods=['GET'])
def specific_class(clss):
    return jsonify({
        "class": {
            "metallic": ["Rb", "Sg", "Hg", "Fm", "H", "He"],
            "non-metallic": ["No", "Og", "As", "Al", "H", "He"],
            "semi-metallic": ["Nb", "Re", "Pu", "Gd", "H", "He"]
        }
    })


@app.route('/periodictable/blocks/', methods=['GET'])
def all_blocks():
    return jsonify({
        "block": {
            "all": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
                    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I",
                    "Xe", "Cs", "Ba", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
                    "At", "Rn", "Fr", "Ra", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
                    "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
                    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"]
        }
    })


@app.route('/periodictable/block/<string:blk>/', methods=['GET'])
def specific_block(blk):
    return jsonify({
        "block": {
            "s-block": ["Rb", "Sg", "Hg", "Fm", "H", "He"],
            "p-block": ["No", "Og", "As", "Al", "H", "He"],
            "d-block": ["Nb", "Re", "Pu", "Gd", "H", "He"],
            "f-block": ["Rb", "Og", "Fm", "Gd", "H", "He"]
        }
    })


@app.route('/periodictable/groups/', methods=['GET'])
def all_groups():
    return jsonify({
        "group": {
            "all": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
                    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I",
                    "Xe", "Cs", "Ba", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
                    "At", "Rn", "Fr", "Ra", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
                    "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
                    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"]
        }
    })


@app.route('/periodictable/group/<int:gnum>/', methods=['GET'])
def specific_group(gnum):
    return jsonify({
        "group": {
            "1": ["Rb", "Sg", "Hg", "Fm"],
            "2": ["No", "Og", "As", "Al", "H", "He"],
            "3": ["Nb", "Re", "Pu", "Gd", "H", "He"],
            "4": ["Rb", "Og", "Fm", "Gd", "H", "He"]
        }
    })


@app.route('/periodictable/periods/', methods=['GET'])
def all_periods():
    return jsonify({
        "period": {
            "all": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
                    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I",
                    "Xe", "Cs", "Ba", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
                    "At", "Rn", "Fr", "Ra", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
                    "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
                    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"]
        }
    })


@app.route('/periodictable/period/<int:pnum>/', methods=['GET'])
def specific_period(pnum):
    return jsonify({
        "period": {
            "1": ["Rb", "Sg", "Hg", "Fm", "H", "He"],
            "2": ["No", "Og", "As", "Al", "H", "He"],
            "3": ["Nb", "Re", "Pu", "Gd", "H", "He"],
            "4": ["Rb", "Og", "Fm", "Gd", "H", "He"]
        }
    })


@app.route('/periodictable/element/<string:sym>/', methods=['GET'])
def element_info(sym):
    return jsonify({
        "elements": {
            "He": [{
                "atomicNumber": 2,
                "atomicWeight": "4.002602",
                "block": "p-block",
                "caseRegistryID": "7440-59-7",
                "classification": "Non-metallic",
                "color": "colorless",
                "group": "group_18",
                "name": "helium",
                "period": "period_1",
                "standardState": "gas",
                "symbol": "He"
            }],
            "H": [{
                "atomicNumber": 1,
                "atomicWeight": "4.002602",
                "block": "p-block",
                "caseRegistryID": "7440-59-7",
                "classification": "Non-metallic",
                "color": "colorless",
                "group": "group_18",
                "name": "hydrogen",
                "period": "period_1",
                "standardState": "gas",
                "symbol": "H"
            }],
            "C": [{
                "atomicNumber": 1,
                "atomicWeight": "4.002602",
                "block": "p-block",
                "caseRegistryID": "7440-59-7",
                "classification": "Non-metallic",
                "color": "colorless",
                "group": "group_18",
                "name": "carbon",
                "period": "period_1",
                "standardState": "gas",
                "symbol": "C"
            }]

        }
    })


if __name__ == '__main__':
    app.run(debug=True)
