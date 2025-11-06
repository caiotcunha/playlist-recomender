from flask import Flask, request, jsonify
import json
import pickle
import os

modelpath = os.getenv("MODELPATH",)
version = os.getenv("APP_VERSION", "1.0.0")

app = Flask(__name__)
app.model = pickle.load(open(modelpath, 'rb'))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/recommend", methods=["POST"])
def recommend():
    #print(app.model["rules"])
    
    data = request.get_json()
    songsSet = set(data["songs"])

    recommendations = []
    for antecedent, consequent, confid in app.model["rules"]:
        if antecedent.issubset(songsSet):
            recommendations.extend(consequent)

    response = {
        'songs': list(set(recommendations)),
        'version': version,
        'model_date': app.model["updated_at"]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50033)