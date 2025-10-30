from flask import Flask, request, jsonify
import json
import pickle

app = Flask(__name__)
#app.model = pickle.load(open('../mlGenerator/model.pickle', 'rb'))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#@app.route("/api/recommend", methods=["POST"])
#def recommend():
#    
#    data = request.get_json()
#    data = json.loads(data)
#    songsSet = set(data["songs"])
#
#    recommendations = []
#    for antecedent, consequent, confid in app.model:
#        if antecedent.issubset(songsSet):
#            recommendations.extend(consequent)
#
#    response = {
#        'songs': list(set(recommendations)),
#        #TODO: deve ser dinamico
#        'version': '1.0.0',
#        'model_date': '2025-10-28'
#    }
#    return jsonify(response)
