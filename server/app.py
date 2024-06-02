from flask import Flask, request, jsonify
from PIL import Image
import os
from constants import *
from model.model import Model

app = Flask(__name__)

@app.route('/get_nutrition', methods=['POST'])
def get_nutrition():
    file = request.files['image']
    path = os.path.join(IMAGE_DIR, "temp.jpg")
    file.save(path)
    model = Model()
    return jsonify(model.get_nutrition(path))

@app.route('/get_food', methods=['POST'])
def get_food():
    file = request.files['image']
    path = os.path.join(IMAGE_DIR, "temp.jpg")
    file.save(path)
    model = Model()
    return jsonify(model.identify_food(path))

if __name__ == "__main__":
    app.run(debug=True)