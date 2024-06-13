from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

rf = joblib.load('Contents/model.joblib')
pipeline=joblib.load('Contents/pipeline.joblib')

@app.route('/')
def home():
    return render_template('ccd_.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    query_point = np.array(data['query_point']).reshape(1, -1)
    query_point_transformed = pipeline.transform(query_point)
    prediction = rf.predict(query_point_transformed)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
