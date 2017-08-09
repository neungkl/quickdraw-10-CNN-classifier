from flask import Flask, render_template, render_template_string, request
import os
import keras
import numpy as np
app = Flask(__name__)

model_path = os.path.join(os.getcwd(), "..", "model/model-v1.h5")
model = keras.models.load_model(model_path)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    img = np.array(request.form['img'].split(","), np.float32).reshape(1, 28, 28, 1)
    img /= 255
    result = model.predict(img)[0]
    return render_template_string(",".join(result.astype(str)))
    # return render_template_string("0.0985102057457,0.0936895906925,0.0623816810548,0.102438829839,0.108508199453,0.180629864335,0.0768260806799,0.0812399238348,0.0883773490787,0.107398249209")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
