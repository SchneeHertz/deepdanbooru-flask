from flask import Flask, request, jsonify
import json, os
import numpy
from deepdanbooru_onnx import DeepDanbooru
danbooru = DeepDanbooru(model_path=os.path.join(os.getcwd(), "deepdanbooru.onnx"), tags_path=os.path.join(os.getcwd(), "tags.txt"))

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyEncoder

@app.route('/predict', methods=['POST'])
def predict():
    p = request.form['filepath']
    print(f"predict picture in: {p}")
    result = danbooru(p)
    print(f"result: {result}")
    return jsonify(result)

@app.route('/predictbatch', methods=['POST'])
def predict_batch():
    pass

@app.route('/predictimage', methods=['POST'])
def predict_image():
    pass

@app.route('/', methods=['GET', 'POST'])
def home():
    pass